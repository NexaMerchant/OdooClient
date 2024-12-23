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
from odoo_api import OdooApi
from RedisEnums import RedisEnums

# Load environment variables from .env file
load_dotenv()

# get all customers from shopify store using the shopify api
# params: [page, limit]
def get_customers(r, shopify, limit=50):
    customers = []
    page_info = None

    while True:
        params = {
            'limit': limit
        }
        if page_info:
            params['page_info'] = page_info
        # get the customers from the shopify store
        customers_data = shopify.Customer.find(**params)
        for customer in customers_data:
            customers.append(customer)
        if not customers_data.has_next_page():
            break
        page_info = customers_data.next_page_url

    return customers

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

        if product_id:
            print("Product found in odoo.")
            # print(product_id)
            product_id = product_id[0]
            return product_id
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
                    'barcode': str(product_data['id']),
                    'website_id': website_id,
                   # 'attribute_line_ids': product_data['attribute_line_ids'],
                   # 'valid_product_template_attribute_line_ids': product_data['valid_product_template_attribute_line_ids'],
                }]
            )
            print(product_id)

        # create a product attribute line in odoo
        attribute_line_ids = []
        #attribute_value_ids = []
        for option in option_data:
            attribute_value_ids = []
            values = option['values']
            for value in values:
                attribute_value_id = r.get(f'attribute_values:{option["name"]}:{value}')
                attribute_value_ids.append(int(attribute_value_id))
                attribute_line_ids.append({
                    "attribute_id": int(r.get(f'attribute_values:{option["name"]}')),
                    "value_ids" : attribute_value_ids
                }
            )


        # Connect to Odoo
        odoo = OdooApi(url, db, username, api_key)

        # create a new product attribute line for product template in the odoo store

        for attribute_line in attribute_line_ids:

            # check if the attribute line exists in the odoo store
            attribute_line_id = odoo.search('product.template.attribute.line', [
                ('product_tmpl_id', '=', product_id),
                ('attribute_id', '=', attribute_line['attribute_id']),
                ('value_ids', '=', attribute_line['value_ids']),
            ])

            if attribute_line_id:
                print("Attribute line found in odoo.")
                print(attribute_line_id)
            else:
                attribute_line_id = odoo.create('product.template.attribute.line', {
                    'product_tmpl_id': product_id,
                    'attribute_id': attribute_line['attribute_id'],
                    'value_ids': attribute_line['value_ids'],
                })
            print(attribute_line_id)



        
        #create product variant in the odoo store
        r.set(f'product:{product_data["id"]}', product_id)
        return product_id

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

def update_product_variants(product_id, option_data, attribute_line_ids, variant_data, r):
    print("Updating product variants.")
    print(product_id)
    print(option_data)
    print(attribute_line_ids)

    odoo = OdooApi(os.getenv('URL'), os.getenv('DB'), os.getenv('USERNAME'), os.getenv('API_KEY'))

    print("Updating product variants." + str(product_id))

    fields = ['id', 'name']

    search_criteria = [
        ['product_tmpl_id', '=', int(product_id)],
        ['is_product_variant', '=', True]
    ]

    fields = [
        'id',
        'name',
        'default_code',
        'attribute_line_ids',
        'product_template_attribute_value_ids',
    ]

    

    template_attribute_line_ids = odoo.search_read('product.product', search_criteria, fields)

    for template_attribute_line in template_attribute_line_ids:
        print(template_attribute_line)
        attribute_line_ids = template_attribute_line['attribute_line_ids']

        for attribute_line in attribute_line_ids:
            print(attribute_line)
            # get the attribute value from the odoo store
            attribute_value = odoo.search_read('product.attribute.value', [['id', '=', attribute_line]], ['name'])
            print(attribute_value)    

        exit()
        # check if the product variant exists in the odoo store
        


    # product.template.attribute.line = attribute_line_ids

    for variant in variant_data:
        print(variant)
        # search option1, option2, option3  in the odoo store
        # base use option1, option2 and option3 to search the product variant in odoo
        # if the product variant exists in odoo, update the product variant

        

        
            
        





if __name__ == '__main__':
    # shopify private apps
    shop_url = os.getenv('USA_SHOPIFY_HOST')
    api_version = os.getenv('USA_SHOPIFY_API_VERSION')
    private_app_password = os.getenv('USA_SHOPIFY_ACCESS_TOKEN')
    session = shopify.Session(shop_url, api_version, private_app_password)
    shopify.ShopifyResource.activate_session(session)
    print("Authenticated successfully." + session.url)
    # find all orders

    odoo = OdooApi(os.getenv('URL'), os.getenv('DB'), os.getenv('USERNAME'), os.getenv('API_KEY'))

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
        
        # for option in option_data:
        #     attribute_line_ids.append(
        #         int(r.get(f'attribute_values:{option["name"]}'))
        #     )
        for option in option_data:
            values = option['values']
            value_ids = []
            attribute_id = r.get(f'attribute_values:{option["name"]}')
            for value in values:
                attribute_value_id = r.get(f'attribute_values:{option["name"]}:{value}')
                value_ids.append(int(attribute_value_id))
            attribute_line_ids.append(({
                'attribute_id': int(attribute_id),
                'value_ids': [(value_ids)],
            }))
        #print(attribute_line_ids)

        #exit()
            
        

        for variant in product_variants:
            # print(variant)
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
                'option1': variantDetail['option1'],
                'option2': variantDetail['option2'],
                'option3': variantDetail['option3'],
            })
            #print(variantDetail)
        
        # create a variant product in odoo
        product_data = {
            'name': product['title'],
            'description': product['body_html'],
            'price': product['variants'][0]['price'],
            'compare_at_price': product['variants'][0]['compare_at_price'],
            'id': product['id'],
            'attribute_line_ids': option_data,
            # 'valid_product_template_attribute_line_ids': attribute_line_ids,
        }
        # print(product_data, variant_data)
        #exit()

        product_id = create_product(product_data, variant_data, option_data, r)

        #print(product_id)

        # update the product variants
        update_product_variants(product_id, option_data, attribute_line_ids,  variant_data, r) 

        exit()
        