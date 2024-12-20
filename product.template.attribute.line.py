# product.template.attribute.line model data

import os
from dotenv import load_dotenv
from math import ceil
import shopify
from api_store import get_token
from odoo_api import OdooApi
import json

# Load environment variables from .env file
load_dotenv()

# shopify private apps
shop_url = os.getenv('USA_SHOPIFY_HOST')
api_version = os.getenv('USA_SHOPIFY_API_VERSION')
private_app_password = os.getenv('USA_SHOPIFY_ACCESS_TOKEN')
session = shopify.Session(shop_url, api_version, private_app_password)
shopify.ShopifyResource.activate_session(session)
print(" Authenticated successfully " + session.url)

# get the product template attribute line data

# Odoo API
url = os.getenv('URL')
db = os.getenv('DB')
username = os.getenv('USERNAME')
api_key = os.getenv('API_KEY')

# Connect to Odoo
odoo = OdooApi(url, db, username, api_key)

# Get all product.template.attribute.line records
# search_criteria
search_criteria = [
    ['product_tmpl_id', '=', 73],
    # ['attribute_id', '=', 2],
    # ['value_ids', '=', 29]
]
product_template_attribute_line = odoo.search_read('product.template.attribute.line', search_criteria, [])

print(json.dumps(product_template_attribute_line, indent=4))
#print(product_template_attribute_line)


