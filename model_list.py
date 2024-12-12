import xmlrpc.client
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Odoo server details
url = os.getenv('URL')
db = os.getenv('DB')
username = os.getenv('USERNAME')
api_key = os.getenv('API_KEY')

# Authenticate
common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
uid = common.authenticate(db, username, api_key, {})

if not uid:
    print("Authentication failed.")
else:
    print("Authenticated successfully. UID:", uid)
    
    # Object endpoint
    models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')

    # Retrieve the list of models
    model_list = models.execute_kw(
        db, uid, api_key,
        'ir.model', 'search_read',
        [[]],  # Empty domain to retrieve all models
        {'fields': ['model', 'name']}  # Fields to retrieve
    )

    # Print the models
    for model in model_list:
        print(f"Model: {model['model']}, Name: {model['name']}")