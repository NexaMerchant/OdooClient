import xmlrpc.client
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Odoo server details from .env file
url = os.getenv('URL')
db = os.getenv('DB')
username = os.getenv('USERNAME')
api_key = os.getenv('API_KEY')

# Authenticate with the Odoo server
common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
uid = common.authenticate(db, username, api_key, {})

if not uid:
    print("Authentication failed.")
else:
    print(f"Authenticated successfully. UID: {uid}")

    # Set up the object endpoint
    models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')

    # get all product templates
    product_templates = models.execute_kw(
        db, uid, api_key,
        'product.template', 'search_read',
        [[]],
        {'fields': ['name']}
    )

    print("Product Templates:")

    for product_template in product_templates:
        print(product_template)

    # get all product categories
    product_categories = models.execute_kw(
        db, uid, api_key,
        'product.category', 'search_read',
        [[]],
        {'fields': ['name']}
    )

    print("Product Categories:")
    for product_category in product_categories:
        print(product_category)

    # get all units of measure
    units_of_measure = models.execute_kw(
        db, uid, api_key,
        'uom.uom', 'search_read',
        [[]],
        {'fields': ['name']}
    )

    print("Units of Measure:")
    for uom in units_of_measure:
        print(uom)

    exit()

    # Prepare product data
    products = [
        {
            'name': 'Product A',
            'default_code': 'PROD_A',
            'type': 'product',  # 'product' for storable products, 'consu' for consumables, 'service' for services
            'list_price': 100.0,
            'standard_price': 80.0,
            'categ_id': 1,  # Replace with the actual category ID
            'uom_id': 1,    # Replace with the actual unit of measure ID
            'uom_po_id': 1, # Replace with the actual purchase unit of measure ID
            'product_tmpl_id': 1,  # Replace with the actual product template ID
        },
        {
            'name': 'Product B',
            'default_code': 'PROD_B',
            'type': 'product',
            'list_price': 150.0,
            'standard_price': 120.0,
            'categ_id': 1,
            'uom_id': 1,
            'uom_po_id': 1,
            'height': 10.0,
            'width': 5.0,
            'length': 20.0,
            'weight': 2.0,
            'color': 'Red',
            'product_tmpl_id': 1,  # Replace with the actual product template ID
        },
        # Add more products as needed
    ]

    # Create products
    product_ids = []
    for product in products:
        product_id = models.execute_kw(
            db, uid, api_key,
            'product.product', 'create',
            [product]
        )
        product_ids.append(product_id)
        print(f"Created product {product['name']} with ID: {product_id}")

    print(f"All created product IDs: {product_ids}")