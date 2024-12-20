import os
import xmlrpc.client
from dotenv import load_dotenv
import logging

# Set up logging to file
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

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
        print(f"Writing to {model} with ids {ids} and data {data}")
        return self.models.execute_kw(self.db, self.uid, self.api_key, model, 'write', [ids, data])
    
    def create(self, model, data):
        return self.models.execute_kw(self.db, self.uid, self.api_key, model, 'create', [data])
    
    def update(self, model, domain, data):
        ids = self.search(model, domain)
        print(f"Updating {model} with domain {domain} and data {data}")
        print(f"IDs: {ids}")
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