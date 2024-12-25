import os
import xmlrpc.client
from dotenv import load_dotenv
import logging

# Set up logging to file
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

class OdooApi:
    def __init__(self, url, db, username, api_key):
        self.url = url
        self.db = db
        self.username = username
        self.api_key = api_key
        self.uid = None
        self.models = None
        self.authenticate()

    def authenticate(self):
        common = xmlrpc.client.ServerProxy(f'{self.url}/xmlrpc/2/common')
        self.uid = common.authenticate(self.db, self.username, self.api_key, {})
        if not self.uid:
            raise Exception("Authentication failed.")
        self.models = xmlrpc.client.ServerProxy(f'{self.url}/xmlrpc/2/object')
        print(f"Authenticated successfully. UID: {self.uid}")

    def search_read(self, model, domain, fields=[]):
        return self.models.execute_kw(self.db, self.uid, self.api_key, model, 'search_read', [domain], {'fields': fields})
    
    def search(self, model, domain):
        return self.models.execute_kw(self.db, self.uid, self.api_key, model, 'search', [domain])
    
    def read(self, model, ids, fields):
        return self.models.execute_kw(self.db, self.uid, self.api_key, model, 'read', [ids], {'fields': fields})
    
    def write(self, model, ids, data):
        # print(f"Writing to {model} with ids {ids} and data {data}")
        return self.models.execute_kw(self.db, self.uid, self.api_key, model, 'write', [ids, data])
    
    def create(self, model, data):
        return self.models.execute_kw(self.db, self.uid, self.api_key, model, 'create', [data])
    
    def delete(self, model, ids):
        return self.models.execute_kw(self.db, self.uid, self.api_key, model, 'unlink', [ids])
    
    def update(self, model, domain, data):
        ids = self.search(model, domain)
        #print(f"Updating {model} with domain {domain} and data {data}")
        #print(f"IDs: {ids}")
        if not ids:
            return None
        return self.write(model, ids, data)
    
    def setUid(self, uid):
        self.uid = uid
    
    def getUid(self):
        return self.uid
    
    def setModels(self, models):
        self.models = models

    def getModels(self):
        return self.models

    def get_customer_by_email(self, email):
        domain = [('email', '=', email)]
        customers = self.search_read('res.partner', domain)
        if customers:
            return customers[0]
        return None
    
    def create_customer(self, customer_dict, website_id=1):
        # Create a new customer in Odoo
        logging.info(f"Creating customer: {customer_dict}")
        country_id = self.search('res.country', [('code', '=', customer_dict['default_address']['country_code'])])
        if not country_id:
            logging.error(f"Country not found: {customer_dict['default_address']['country_code']}")
            return None
        customer_dict['country_id'] = country_id

        # when province is null
        state_id = False
        if customer_dict['default_address']['province_code']:
            state_id = self.search('res.country.state', [('code', '=', customer_dict['default_address']['province_code']), ('country_id', '=', country_id[0])])
            if not state_id:
                logging.error(f"State not found: {customer_dict['default_address']['province_code']}")
                return None
            state_id = state_id[0]
        
        customer_dict['state_id'] = state_id
        customer_dict['is_company'] = False
        customer_dict['category_id'] = [8]
        customer_dict['lang'] = 'en_US'
        customer_dict['website_id'] = website_id

        phone = ""
        if customer_dict['default_address']['phone']:
            phone = customer_dict['default_address']['phone']

        customer_data = {
                    'name': customer_dict['first_name'] + ' ' + customer_dict['last_name'],
                    'email': customer_dict['email'],
                    'phone': phone,
                    'street': customer_dict['default_address']['address1'][0],
                    #'street2': order['shipping_address']['address2'][0],
                    'city': customer_dict['default_address']['city'],
                    'zip': customer_dict['default_address']['zip'],
                    'country_code': customer_dict['default_address']['country_code'],
                    'state_id': state_id,
                    'country_id': country_id[0],
                    'website_id': website_id,
                    'lang': 'en_US',
                    'category_id': [8],
                # 'category_id': 8,
        }

        customer_id = self.create('res.partner', customer_data)
        return customer_id
    
    def update_customer(self, customer_id, customer_dict):
        # Update an existing customer in Odoo
        logging.info(f"Updating customer {customer_id}: {customer_dict}")
        return self.write('res.partner', [customer_id], customer_dict)
    