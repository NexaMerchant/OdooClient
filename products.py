# products modules

import os
from dotenv import load_dotenv
import requests
import json
import xmlrpc.client
import time
from math import ceil
import redis

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

    # Define the search criteria for the product.template.attribute.line
    search_criteria = [
        ['product_tmpl_id', '=', 71]
    ]

    # Search for the products template
    product_template_ids = models.execute_kw(
        db, uid, api_key,
        'product.template.attribute.line', 'search_read',
        [search_criteria],
        {}
    )

    print(product_template_ids)

    exit()

    # Define the search criteria
    search_criteria = [
        ['id', '=', 71]
    ]

    # Search for the products
    product_ids = models.execute_kw(
        db, uid, api_key,
        'product.template', 'search_read',
        [search_criteria],
        {}
    )

    print(product_ids)

if __name__ == '__main__':
    get_products()