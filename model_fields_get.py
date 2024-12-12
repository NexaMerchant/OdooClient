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

    # Specify the model you want to inspect
    model_name = 'res.partner'  # Replace with your model name

    print(f"Fields of model: {model_name}")

    # Retrieve the fields of the model
    fields = models.execute_kw(
        db, uid, api_key,
        model_name, 'fields_get',
        [],
        {'attributes': ['string', 'type']}
    )

    # Print the fields
    for field_name, field_info in fields.items():
        print(f"Field: {field_name}, Type: {field_info['type']}, Label: {field_info['string']}")