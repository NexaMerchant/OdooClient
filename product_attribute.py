import os
import requests
from dotenv import load_dotenv
import redis
from odoo_api import OdooApi

load_dotenv()

store_mark = "CZ"

#find the all warehouses in odoo

if __name__ == '__main__':
    
    redis_host = os.getenv('REDIS_HOST')
    redis_port = os.getenv('REDIS_PORT')
    redis_db = os.getenv('REDIS_DB')
    redis_password = os.getenv('REDIS_PASSWORD')
    lang = os.getenv(store_mark + '_LANG')

    # create a connection to the redis server
    r = redis.Redis(host=redis_host, port=redis_port, db=redis_db, password=redis_password)
    odoo = OdooApi(os.getenv('URL'), os.getenv('DB'), os.getenv('USERNAME'), os.getenv('API_KEY'))

    # get all product attributes
    product_attributes = odoo.search_read('product.attribute', [], ['name', 'display_name','create_date','create_uid','id'], lang=lang)
    print(product_attributes)

    