#shopify private apps

import os
from dotenv import load_dotenv
import requests
import json
import xmlrpc.client
import time
from math import ceil
import redis
import shopify
from api_store import get_token

# Load environment variables from .env file
load_dotenv()

# shopify private apps
shop_url = os.getenv('USA_SHOPIFY_HOST')
api_version = os.getenv('USA_SHOPIFY_API_VERSION')
private_app_password = os.getenv('USA_SHOPIFY_ACCESS_TOKEN')
session = shopify.Session(shop_url, api_version, private_app_password)
shopify.ShopifyResource.activate_session(session)
print("Authenticated successfully." + session.url)
# find all orders

def get_orders():
    orders = shopify.Order.find()
    return orders

def get_order(order_id):
    order = shopify.Order.find(order_id)
    return order

def get_products():
    products = shopify.Product.find()
    return products

def get_product(product_id):
    product = shopify.Product.find(product_id).to_dict()
    return product

def get_product_variants(product_id):
    product = shopify.Product.find(product_id)
    return product.variants

def get_product_variant(variant_id):
    variant = shopify.Variant.find(variant_id).to_dict()
    return variant

# create a product in odoo
def create_product(product_data, variant_data, option_data, r):
    url = os.getenv('URL')
    db = os.getenv('DB')
    username = os.getenv('USERNAME')
    api_key = os.getenv('API_KEY')
    website_id = os.getenv('WEBSITE_ID')
    common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
    uid = common.authenticate(db, username, api_key, {})

    # check the product id in the redis cache
    product_id = r.get(f'product:{product_data["id"]}')
    if product_id:
        print("Product found in redis cache.")
        return product_id

    if not uid:
        print("Authentication failed.")
        exit()
    else:
        print("Authenticated successfully. UID:", uid)
        models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')

        #print(product_data)

        product_default_code = str(product_data['id'])

        # check if the product exists in the odoo store
        product_id = models.execute_kw(
                db, uid, api_key,
                'product.template', 'search',
                [[('default_code', '=', product_default_code)]]
        )

        print(product_id)

        #print(product_data)

        #exit()

        if product_id:
            print("Product found in odoo.")
            # print(product_id)
            product_id = product_id[0]
            #return product_id[0]
        else:
            print("Product not found in odoo.")
            # create a new product in the odoo store
            product_id = models.execute_kw(
                db, uid, api_key,
                'product.template', 'create',
                [{
                    'name': product_data['name'],
                    'description': product_data['description'],
                    'list_price': product_data['price'],
                    'compare_list_price': product_data['compare_at_price'],
                    'type': 'consu',
                    'default_code': product_default_code,
                    'website_id': website_id,
                    'attribute_line_ids': product_data['attribute_line_ids'],
                    'valid_product_template_attribute_line_ids': product_data['valid_product_template_attribute_line_ids'],
                }]
            )
            print(product_id)
        
        #create product variant in the odoo store
        r.set(f'product:{product_data["id"]}', product_id)
        
        for variant in variant_data:
            # check if the product variant exists in the odoo store
            product_variant_id = models.execute_kw(
                db, uid, api_key,
                'product.product', 'search',
                [[
                    ('default_code', '=', variant['sku']),
                    ('product_tmpl_id', '=', product_id)
                  ]]
            )

            if product_variant_id:
                print("Product variant found in odoo.")
                print(product_variant_id)
                #return product_variant_id[0]
            else:
                print("Product variant not found in odoo.")

                variant_barcode = variant['barcode'] if variant['barcode'] is not None else ''

                print(option_data)

                attribute_value_ids = []
                for option in option_data:
                    values = option['values']
                    for value in values:
                        attribute_value_id = r.get(f'attribute_values:{option["name"]}:{value}')
                        attribute_value_ids.append(int(attribute_value_id))
                
                print(attribute_value_ids)
                #exit()

                # create a new product variant in the odoo store
                product_variant_id = models.execute_kw(
                    db, uid, api_key,
                    'product.product', 'create',
                    [{
                        'name': variant['name'],
                        'default_code': variant['sku'],
                        'list_price': variant['list_price'],
                        'compare_list_price': variant['compare_at_price'],
                        'product_tmpl_id': product_id[0],
                        'barcode': str(variant['default_code']),
                        'combination_indices': attribute_value_ids,
                       # 'requires_shipping': variant['requires_shipping'],
                        # 'sku': variant['sku'],
                        'weight': variant['weight'],
                    }]
                )
                print(product_variant_id)

        #return product_id

# create a product attribute in odoo
def create_attribute(option_data, r):
    url = os.getenv('URL')
    db = os.getenv('DB')
    username = os.getenv('USERNAME')
    api_key = os.getenv('API_KEY')
    website_id = os.getenv('WEBSITE_ID')
    common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
    uid = common.authenticate(db, username, api_key, {})
    if not uid:
        print("Authentication failed.")
        exit()
    else:
        print("Authenticated successfully. UID:", uid)
        models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')

        # check if the attribute exists in the odoo store
        for option in option_data:
            attribute_id = models.execute_kw(
                    db, uid, api_key,
                    'product.attribute', 'search',
                    [[('name', '=', option['name']),
                      ('create_variant', '=', 'always')
                      ]]
            )
            # print(attribute_id)
            if attribute_id:
                print(option['name'] + "Attribute found in odoo." + str(attribute_id[0]))
                # print(attribute_id)

                r.set('attributes', option['name'])

                attribute_id = attribute_id[0]
                
                # check if the attribute value exists in the odoo store
                for value in option['values']:
                    print(value)
                    attribute_value_id = models.execute_kw(
                        db, uid, api_key,
                        'product.attribute.value', 'search',
                        [[('name', '=', value), ('attribute_id', '=', attribute_id)]]
                    )
                    if attribute_value_id:
                        print(value + "Attribute value found in odoo.")
                        # print(attribute_value_id)
                        r.set(f'attribute_values:{option["name"]}:{value}', attribute_value_id[0])
                    else:
                        print(value + "Attribute value not found in odoo.")
                        # create a new attribute value in the odoo store
                        attribute_value_id = models.execute_kw(
                            db, uid, api_key,
                            'product.attribute.value', 'create',
                            [{
                                'name': value,
                                'attribute_id': attribute_id,
                            }]
                        )
                        print(attribute_value_id)
                        # add attribute id and attribute value id to redis sets list
                        r.set(f'attribute_values:{option['name']}:{value}', str(attribute_value_id))
                

                r.set(f'attribute_values:{option['name']}', attribute_id)
            else:
                print(option['name'] + "Attribute not found in odoo.")
                exit()
                return False

if __name__ == '__main__':
    # orders = get_orders()
    # print(orders)
    # order = get_order(orders[0].id)
    # print(order)

    redis_host = os.getenv('REDIS_HOST')
    redis_port = os.getenv('REDIS_PORT')
    redis_db = os.getenv('REDIS_DB')
    redis_password = os.getenv('REDIS_PASSWORD')

    # create a connection to the redis server
    r = redis.Redis(host=redis_host, port=redis_port, db=redis_db, password=redis_password)

    products = get_products()
    for product in products:
        product = get_product(product.id)
        # print(product)
        product_variants = get_product_variants(products[0].id)
        variant_data = []
        option_data = []

        for option in product['options']:
            option_data.append({
                'name': option['name'],
                'values': option['values'],
            })

        create_attribute(option_data, r)
        #continue

        #exit()
        attribute_line_ids = []
        for option in option_data:
            attribute_line_ids.append(
                int(r.get(f'attribute_values:{option["name"]}'))
            )
        #print(attribute_line_ids)

        #exit()
            
        

        for variant in product_variants:
            print(variant)
            variantDetail = get_product_variant(variant.id)
            variant_data.append({
                'name': variantDetail['title'],
                'default_code': variantDetail['id'],
                'list_price': variantDetail['price'],
                'compare_at_price': variantDetail['compare_at_price'],
                'product_tmpl_id': product['id'],
                'barcode': variantDetail['barcode'],
                'requires_shipping': variantDetail['requires_shipping'],
                'sku': variantDetail['sku'],
                'weight': variantDetail['weight'],
            })
            print(variantDetail)
        
        # create a variant product in odoo
        product_data = {
            'name': product['title'],
            'description': product['body_html'],
            'price': product['variants'][0]['price'],
            'compare_at_price': product['variants'][0]['compare_at_price'],
            'id': product['id'],
            'attribute_line_ids': option_data,
            'valid_product_template_attribute_line_ids': attribute_line_ids,
        }
        print(product_data, variant_data)
        #exit()

        create_product(product_data, variant_data, option_data, r)
        exit()