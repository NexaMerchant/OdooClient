# sync customer to odoo
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
from time import sleep

# Load environment variables from .env file
load_dotenv()

def get_customers(limit=50, odoo=None, website_id=None):
    customers = []
    page_info = None

    while True:
        params = {'limit': limit}
        if page_info:
            params['page_info'] = page_info

        response = shopify.Customer.find(**params)
        customers.extend(response)

        for customer in response:
            customer_dict = customer.to_dict()

            print(f"Checking customer: {customer_dict}")

            if customer_dict['email'] == None:
                continue

            customer_id = r.get(customer_dict['email'])
            if customer_id:
                continue
            
            # check if the customer exists in odoo
            odoo_customer = odoo.get_customer_by_email(customer_dict['email'])
            if not odoo_customer:
                # create the customer
                print(f"Creating customer: {customer_dict}")
                customer_id = odoo.create_customer(customer_dict, website_id)
                r.set(customer_dict['email'], customer_id)
                sleep(1)




        if not response:
            break

        page_info = response.next_page_url.split('page_info=')[1]

    return customers

if __name__ == "__main__":
    
    shop_url = os.getenv('USA_SHOPIFY_HOST')
    api_version = os.getenv('USA_SHOPIFY_API_VERSION')
    private_app_password = os.getenv('USA_SHOPIFY_ACCESS_TOKEN')
    session = shopify.Session(shop_url, api_version, private_app_password)
    shopify.ShopifyResource.activate_session(session)

    website_id = os.getenv('WEBSITE_ID')

    odoo = OdooApi(os.getenv('URL'), os.getenv('DB'), os.getenv('USERNAME'), os.getenv('API_KEY'))

    redis_host = os.getenv('REDIS_HOST')
    redis_port = os.getenv('REDIS_PORT')
    redis_db = os.getenv('REDIS_DB')
    redis_password = os.getenv('REDIS_PASSWORD')

    # create a connection to the redis server
    r = redis.Redis(host=redis_host, port=redis_port, db=redis_db, password=redis_password)

    # get the last time the customer was synced
    customers = get_customers(limit=50, odoo=odoo, website_id=website_id)
    for customer in customers:
        customer_dict = customer.to_dict()
        print(customer_dict)
        exit()

