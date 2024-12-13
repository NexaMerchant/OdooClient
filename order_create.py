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
    exit()
else:
    print("Authenticated successfully. UID:", uid)

    # Object endpoint
    models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')

    # Define the order customer search criteria
    customer_search_criteria = [
        ['name', '=', 'Agrolait'],
    ]

    # Search for the customer
    customer_id = models.execute_kw(
        db, uid, api_key,
        'res.partner', 'search',
        [customer_search_criteria]
    )


    # define the order data
    sale_order_data = {
        'partner_id': customer_id[0], 
        'order_line': [
            (0, 0, {
                'product_id': 1,
                'product_uom_qty': 1,
                'price_unit': 100,
            }),
            (0, 0, {
                'product_id': 2,
                'product_uom_qty': 2,
                'price_unit': 200,
            }),
        ]
    }

    # Create a new order
    # Create the sale order
    sale_order_id = models.execute_kw(
        db, uid, api_key,
        'sale.order', 'create',
        [sale_order_data]
    )

    print(f"New Sale Order ID: {sale_order_id}")
