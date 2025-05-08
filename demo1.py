#shopify private apps

import os
import shopify
from dotenv import load_dotenv

load_dotenv()

store_mark = "DE"

params = {'limit': 1}

shop_url = os.getenv(store_mark + '_SHOPIFY_HOST')
api_version = os.getenv(store_mark + '_SHOPIFY_API_VERSION')
private_app_password = os.getenv(store_mark + '_SHOPIFY_ACCESS_TOKEN')
session = shopify.Session(shop_url, api_version, private_app_password)
shopify.ShopifyResource.activate_session(session)

responses = shopify.Product.find(**params)

print(responses)

for response in responses:
    product = shopify.Product.find(response.id)
    print(product.to_dict())
