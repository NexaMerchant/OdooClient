# products modules

import os
from dotenv import load_dotenv
import requests
import json
import xmlrpc.client
import time
from math import ceil
import redis
from odoo_api import OdooApi

# Load environment variables from .env file
load_dotenv()

# products get all from odoo

def get_products(page=1, limit=10):
    url = os.getenv('URL')
    db = os.getenv('DB')
    username = os.getenv('USERNAME')
    api_key = os.getenv('API_KEY')
    website_id = os.getenv('WEBSITE_ID')
    common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
    uid = common.authenticate(db, username, api_key, {})

    print("Authenticated successfully. UID:", uid)

    models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')

    odoo = OdooApi(url, db, username, api_key)

    # Define the search criteria for the product.template.attribute.line
    search_criteria = [
        ['product_tmpl_id', '=', 73]
    ]

    # Search for the products template
    product_template_ids = models.execute_kw(
        db, uid, api_key,
        'product.template.attribute.line', 'search_read',
        [search_criteria],
        {}
    )

    # print(product_template_ids)

    # exit()

    # Define the search criteria
    search_criteria = [
        ['id', '=', 75]
    ]


    # update the product template
    # odoo.update('product.template', search_criteria, {
    #     'cost_currency_id': [1],
    # })

    #print(product_ids)
    product_ids = odoo.search_read('product.template', search_criteria, [])
    #print(product_ids)

    #exit()


    # search for the product product.product
    search_criteria = [
        ['product_tmpl_id', '=', 75],
        ['is_product_variant', '=', True]
    ]

    fields = [
        'id',
        'name',
        'default_code',
        'attribute_line_ids',
    ]

    

    product_product_ids = odoo.search_read('product.product', search_criteria, fields)

    for product in product_product_ids:
        print(product)
        #continue
        # update the product product.product default code
        # odoo.update('product.product', [['id', '=', product['id']]], {
        #     'default_code': '123456789'
        # })
        

    

if __name__ == '__main__':
    get_products()