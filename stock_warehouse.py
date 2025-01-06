import os
import requests
from dotenv import load_dotenv
import redis
from odoo_api import OdooApi

load_dotenv()

#find the all warehouses in odoo

if __name__ == '__main__':
    
    redis_host = os.getenv('REDIS_HOST')
    redis_port = os.getenv('REDIS_PORT')
    redis_db = os.getenv('REDIS_DB')
    redis_password = os.getenv('REDIS_PASSWORD')

    # create a connection to the redis server
    r = redis.Redis(host=redis_host, port=redis_port, db=redis_db, password=redis_password)
    odoo = OdooApi(os.getenv('URL'), os.getenv('DB'), os.getenv('USERNAME'), os.getenv('API_KEY'))

    # get all warehouses
    warehouses = odoo.search_read('stock.warehouse', [], ['name', 'code','company_id'])
    print(warehouses)

    # get all companies
    companies = odoo.search_read('res.company', [], ['name','id'])
    print(companies)