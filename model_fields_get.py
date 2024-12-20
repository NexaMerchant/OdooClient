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
    model_name = 'product.product'  # Replace with your model name
    model_name = 'sale.order'  # Replace with your model name
    model_name = 'res.partner'  # Replace with your model name
    model_name = 'res.country'  # Replace with your model name
    model_name = 'res.country.state'  # Replace with your model name
    model_name = 'res.currency'  # Replace with your model name
    model_name = 'website'  # Replace with your model name
    model_name = 'sale.order'  # Replace with your model name
    model_name = 'product.product'  # Replace with your model name
    model_name = 'sale.order.line'  # Replace with your model name
    model_name = 'product.template'  # Replace with your model name
    model_name = 'payment.provider'  # Replace with your model name
    model_name = 'product.attribute'  # Replace with your model name
    model_name = 'product.attribute.value'  # Replace with your model name
    model_name = 'product.template.attribute.line'  # Replace with your model name

    # create a model fields md file if it does not exist
    # print(f"Creating {model_name}_fields.md")
    # with open(f'{model_name}_fields.md', 'w') as f:
    #     f.write(f"#Fields of model: {model_name}\n\n")

    #     # Retrieve the fields of the model
    #     fields = models.execute_kw(
    #         db, uid, api_key,
    #         model_name, 'fields_get',
    #         [],
    #         {}
    #     )

    #     # Write the fields to the file
    #     for field_name, field_info in fields.items():
    #         f.write(f"#Field: {field_name}\n\n")
    #         for attr, value in field_info.items():
    #             #f.write(f"  {attr}: {value}\n")
    #             #create a table
    #             f.write(f"|{attr}|{value}|\n\n")
    #     f.write("\n\n")

    # print(f"Fields of model: {model_name}")
    # exit()

    # Retrieve the fields of the model
    fields = models.execute_kw(
        db, uid, api_key,
        model_name, 'fields_get',
        [],
        {}
    )

    # Print the fields
    for field_name, field_info in fields.items():
        print(f"Field: {field_name}")
        for attr, value in field_info.items():
            print(f"  {attr}: {value}")