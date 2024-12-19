# Model Data Search
import xmlrpc.client
from dotenv import load_dotenv
import os
import json

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

    models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')

    model_name = 'product.attribute'
    model_name = 'product.attribute.value'

    # Search all records limit and 
    search_result = models.execute_kw(
        db, uid, api_key,
        model_name, 'search_read',
        [[]],
        {'fields': ['name','attribute_id','sequence','create_date','write_date','display_type']}
    )

    # Print the search result
    print(json.dumps(search_result))