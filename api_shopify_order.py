# base use shopify admin api get the order data use filter

import requests

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

store_mark = "USA"

#lang
lang = os.getenv(store_mark + '_LANG')

if __name__ == '__main__':
    print('lang:', lang)
    shop_url = os.getenv(store_mark + '_SHOPIFY_HOST')
    api_version = os.getenv(store_mark + '_SHOPIFY_API_VERSION')
    private_app_password = os.getenv(store_mark + '_SHOPIFY_ACCESS_TOKEN')
    session = shopify.Session(shop_url, api_version, private_app_password)
    shopify.ShopifyResource.activate_session(session)
    print("Authenticated successfully. " + session.url)

    # get all orders filter by delivery status
    orders = shopify.Order.find(fulfillment_status='unshipped', limit=10)
    print('orders:', orders)