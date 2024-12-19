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

# Load environment variables from .env file
load_dotenv()

# shopify private apps
shop_url = os.getenv('USA_SHOPIFY_HOST')
api_version = os.getenv('USA_SHOPIFY_API_VERSION')
private_app_password = os.getenv('USA_SHOPIFY_ACCESS_TOKEN')
session = shopify.Session(shop_url, api_version, private_app_password)
shopify.ShopifyResource.activate_session(session)
print("Authenticated successfully.")
# find all orders

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

if __name__ == '__main__':
    # orders = get_orders()
    # print(orders)
    # order = get_order(orders[0].id)
    # print(order)
    products = get_products()
    print(products)
    product = get_product(products[0].id)
    print(product)
    product_variants = get_product_variants(products[0].id)
    for variant in product_variants:
        print(variant)
        variantDetail = get_product_variant(variant.id)
        print(variantDetail)