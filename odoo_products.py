# Odoo Products
import os
from odoo_api import OdooApi
import redis

if __name__ == "__main__":
    
    odoo = OdooApi(os.getenv('URL'), os.getenv('DB'), os.getenv('USERNAME'), os.getenv('API_KEY'))

    redis_host = os.getenv('REDIS_HOST')
    redis_port = os.getenv('REDIS_PORT')
    redis_db = os.getenv('REDIS_DB')
    redis_password = os.getenv('REDIS_PASSWORD')

    # create a connection to the redis server
    r = redis.Redis(host=redis_host, port=redis_port, db=redis_db, password=redis_password)

    # get all the products from odoo
    products = odoo.search_read('product.product', [], ['name', 'default_code', 'list_price', 'standard_price','is_storable'])
    for product in products:
        if product['is_storable'] is True:
            #print(product)
            search_criteria = [
                ['id', '=', product['id']]
            ]
            print(search_criteria)
            odoo.update('product.product', search_criteria, {'responsible_id': 17})