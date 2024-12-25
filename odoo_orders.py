# Odoo Order 
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

    # get all the orders from odoo
    orders = odoo.search_read('sale.order', [], ['name', 'partner_id', 'state', 'date_order','origin','website_id'])

    for order in orders:
        print(order)
        # delete the order from odoo
        # odoo.delete('sale.order', order['id'])
        odoo.update('sale.order', [('id', '=', order['id'])], {'origin': False, 'website_id': 3})
        