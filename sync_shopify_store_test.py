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
from api_shopify_cz import get_products
from api_shopify_cz import get_product

# Load environment variables from .env file
load_dotenv()

store_mark = "UK"

if __name__ == '__main__':

    shop_url = os.getenv(store_mark + '_SHOPIFY_HOST')
    api_version = os.getenv(store_mark + '_SHOPIFY_API_VERSION')
    private_app_password = os.getenv(store_mark + '_SHOPIFY_ACCESS_TOKEN')
    session = shopify.Session(shop_url, api_version, private_app_password)
    shopify.ShopifyResource.activate_session(session)
    print("Authenticated successfully." + session.url)

    # Connect to Redis
    r = redis.Redis(host=os.getenv("REDIS_HOST"), port=os.getenv("REDIS_PORT"), db=0)


   # GET ALL PRODUCTS
    products = []
    products = get_products()
    i = 1
    for product in products:
        print(product)
        # post product to custom url for odoo
        url = os.getenv(store_mark + '_STORE_URL') + "/api/v1/odooapi/products/shopify"
        headers = {
            "Content-Type": "application/json",
        }
        # if(str(product.id) != "8846711455974"):
        #     continue
        # product = get_product(product.id)
        product = get_product("8216266997978")
        print(product)
        exit()

        data = {
            "product": product
        }
        # print(data)
        # exit()
        print("Sending product to odoo: " + str(i))
        print("Sending product to url: " + url)


        # response = requests.post(url, headers=headers, json=data)
        # print(response.status_code)

        # image_url = os.getenv(store_mark + '_STORE_URL') + "/api/v1/odooapi/products/shopify-images"
        # print("Sending product to image url: " + image_url)
        # response = requests.post(image_url, headers=headers, json=data)
        # print(response.status_code)
        # for debugging
        exit() 
        #print(response.html)

        i += 1

        # if i > 20:
        #     exit()

        sleep(2)

