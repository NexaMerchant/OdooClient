import os
from dotenv import load_dotenv
from math import ceil
import shopify
from api_store import get_token
from odoo_api import OdooApi
import json

# Load environment variables from .env file
load_dotenv()

# Odoo API
url = os.getenv('URL')
db = os.getenv('DB')
username = os.getenv('USERNAME')
api_key = os.getenv('API_KEY')

# Connect to Odoo
odoo = OdooApi(url, db, username, api_key)

# Get all res.partner records

# search_criteria
search_criteria = [
    ['id', '=', 3663],
]
partners = odoo.search_read('res.partner', search_criteria, [])

print(json.dumps(partners, indent=4))