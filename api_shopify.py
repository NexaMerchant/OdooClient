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
import base64
from time import sleep

# Load environment variables from .env file
load_dotenv()

def get_orders():
    orders = shopify.Order.find()
    return orders

def get_order(order_id):
    order = shopify.Order.find(order_id)
    return order

# get all products use the shopify api
# use next page url to get all products

def get_products(limit=50):
    products = []
    page_info = None

    while True:
        params = {'limit': limit}
        if page_info:
            params['page_info'] = page_info

        response = shopify.Product.find(**params)
        products.extend(response)
        print(response.next_page_url)

        if not response:
            break
        if response.next_page_url is None:
            break

        page_info = response.next_page_url.split('page_info=')[1]

    # products = shopify.Product.find()
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

        compare_at_price  = "0.00"
        if product_data['compare_at_price']:
            compare_at_price = product_data['compare_at_price']

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
                    'compare_list_price': compare_at_price,
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
            # covert the option name to capitalize
            option['name'] = option['name'].capitalize()
            attribute_id = models.execute_kw(
                    db, uid, api_key,
                    'product.attribute', 'search',
                    [[('name', '=', option['name']),
                      ('create_variant', '=', 'always')
                      ]]
            )
            # print(attribute_id)
            if attribute_id:
                # print(option['name'] + "Attribute found in odoo." + str(attribute_id[0]))
                # print(attribute_id)

                r.set('attributes', option['name'])

                attribute_id = attribute_id[0]
                
                # check if the attribute value exists in the odoo store
                for value in option['values']:
                    # print(value)
                    attribute_value_id = models.execute_kw(
                        db, uid, api_key,
                        'product.attribute.value', 'search',
                        [[('name', '=', value), ('attribute_id', '=', attribute_id)]]
                    )
                    if attribute_value_id:
                        #print(value + "Attribute value found in odoo.")
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
                # exit()
                return False

def update_product_variants(product_id, option_data, attribute_line_ids, variant_data, images, r):
    print("Updating product variants.")
    print(product_id)
    print(option_data)
    print(attribute_line_ids)
    print(variant_data)

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
        'combination_indices',
    ]

    

    template_attribute_line_ids = odoo.search_read('product.product', search_criteria, fields)

    for template_attribute_line in template_attribute_line_ids:
        # if template_attribute_line['default_code'] is not None:
        #     continue
        print(template_attribute_line)
        attribute_line_ids = template_attribute_line['product_template_attribute_value_ids']


        product_variants_values = []
        for attribute_line in attribute_line_ids:
            print(attribute_line)
            # get the attribute value from the odoo store
            attribute_value = odoo.search_read('product.template.attribute.value', [['id', '=', attribute_line]], ['name'])
            print(attribute_value)
            product_variants_values.append(attribute_value[0]['name'])

        
        default_code = search_default_code(product_variants_values, variant_data)
        default_variant_id = search_default_id(product_variants_values, variant_data)
        print(default_variant_id, default_code, product_variants_values)

        if default_variant_id is not None:
            r.set(f'product:{product_id}:{default_variant_id}', template_attribute_line['id'])

        image_src = search_image_url(default_variant_id, images)
        if image_src is None:
            #exit()
            continue
        #print(image_src)
        #exit()

        # copy the image to the local 
        image_path = f'images/{default_variant_id}.jpg'
        print(image_src)
        print(image_path)
        # when the image is not file exists
        if not os.path.exists(image_path):
            sleep(5)
            image = requests.get(image_src)
            with open(image_path, 'wb') as file:
                file.write(image.content)

        image_base64 = None
        with open(image_path, 'rb') as file:
            image_base64 = base64.b64encode(file.read()).decode('utf-8')
        

        if default_code:
            print("Product variant found in odoo.")
            # update the product variant
            odoo.write('product.product', template_attribute_line['id'], {
                'default_code': default_code,
                'image_1920': image_base64,
            })
        else:
            print("Product variant not found in odoo.")
            # create a new product variant
            return False

def search_image_url(image_id, images):
    print(image_id)
    print(images)
    image_url = None
    for image in images:
        if image_id in image['variant_ids']:
            image_url = image['src']
            break
        if image_id == image['id']:
            image_url = image['src']
            break
    return image_url                

def search_default_id(product_variants_values, variant_data):
    default_id = None
    product_variants_values_count = len(product_variants_values)
    for variant in variant_data:
        if product_variants_values_count == 2:
            if variant['option1'] in product_variants_values and variant['option2'] in product_variants_values:
                default_id = variant['default_code']
                break
        elif product_variants_values_count == 3:
            if variant['option1'] in product_variants_values and variant['option2'] in product_variants_values and variant['option3'] in product_variants_values:
                default_id = variant['default_code']
                break
        elif product_variants_values_count == 1:
            if variant['option1'] in product_variants_values:
                default_id = variant['default_code']
                break
        
    return default_id
        
def search_default_code(product_variants_values, variant_data):
    default_code = None
    product_variants_values_count = len(product_variants_values)
    for variant in variant_data:
        if product_variants_values_count == 2:
            if variant['option1'] in product_variants_values and variant['option2'] in product_variants_values:
                default_code = variant['sku']
                break
        elif product_variants_values_count == 3:
            if variant['option1'] in product_variants_values and variant['option2'] in product_variants_values and variant['option3'] in product_variants_values:
                default_code = variant['sku']
                break
        elif product_variants_values_count == 1:
            if variant['option1'] in product_variants_values:
                default_code = variant['sku']
                break
        
    return default_code
           

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
        # product.id = "8395617403110"

        # when the product is saved in the redis cache then skip the product
        product_id = r.get(f'product:{product.id}')
        if product_id:
            print("Product found in redis cache.")
            continue

        print(f"{product.id} starting processing.")
        product_variants = get_product_variants(product.id)
        product = get_product(product.id)
        # print(product)

        
        
        variant_data = []
        option_data = []
        images = []

        for option in product['options']:
            option_data.append({
                'name': option['name'].capitalize(),
                'values': option['values'],
            })

        create_attribute_result = create_attribute(option_data, r)
        if create_attribute_result is False:
            continue
        #continue

        for image in product['images']:
            images.append({
                'src': image['src'],
                'id': image['id'],
                'position': image['position'],
                "variant_ids": image['variant_ids'],
            })
        
        #print(images)
        #exit()
        

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
        # if product['variants'][0]['compare_at_price'] is None:
        #     continue
            
        

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
        update_product_variants(product_id, option_data, attribute_line_ids,  variant_data, images, r) 

        # exit()

        sleep(5)
        