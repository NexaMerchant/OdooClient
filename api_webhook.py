# Webhook Test

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

load_dotenv()

if __name__ == "__main__":
    # Shopify
    odoo = OdooApi(os.getenv('URL'), os.getenv('DB'), os.getenv('USERNAME'), os.getenv('API_KEY'))
    # Get a order
    search_criteria = [
        ['id', '=', 548],
    ]
    order = odoo.search_read('sale.order', search_criteria, ['name', 'partner_id', 'date_order', 'amount_total', 'state'])
    print(order)
    # Update the order
    name = "Hatmeo#79982"
    odoo.update('sale.order', search_criteria, {'name': name})