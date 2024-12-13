
import os
from dotenv import load_dotenv
import requests
import json
import xmlrpc.client

# Load environment variables from .env file
load_dotenv()

# login the store
def login():
    # Odoo server details
    url = os.getenv('USA_STORE_URL')
    username = os.getenv('USA_STORE_USERNAME')
    password = os.getenv('USA_STORE_PASSWORD')
    device_name = "odoo"

    # Authenticate use http post
    login_url = f'{url}/api/v1/admin/login'
    login_data = {
        "email": username,
        "password": password,
        "device_name": device_name
    }
    response = requests.post(login_url, json=login_data,headers={'Content-Type': 'application/json'})
    
    # response_data to array
    # http status code 200 means success
    if response.status_code != 200:
        print("Failed to authenticate.")
        return None
    else:
        print("Authenticated successfully.")
        response_data = response.json()
        print(response_data)
        # set the token to be cached
        return response_data['token']
    
def get_token():
    # check if the token is cached
    token = os.getenv('USA_STORE_TOKEN')
    if token:
        return token
    else:
        # if not cached, login and cache the token
        token = login()
        return token
    
def get_orders(token):
    # Odoo server details
    url = os.getenv('USA_STORE_URL')
    # Authenticate use http post
    orders_url = f'{url}/api/v1/admin/sales/orders'
    headers = {
        'Authorization': "Bearer " + token,
        'Content-Type': 'application/json'
    }
    data = {
        "page": 1,
        "limit": 1,
        "status": "processing",
    }
    response = requests.get(orders_url, json=data, headers=headers)
    if response.status_code != 200:
        print("Failed to get orders.")
        return None
    else:
        print("Get orders successfully.")
        response_data = response.json()
        print(json.dumps(response_data, indent=4))
        #print(response_data)
        return response_data
    
def create_odoo_order(order, token):
    # create a new customer to the odoo store
    url = os.getenv('URL')
    db = os.getenv('DB')
    username = os.getenv('USERNAME')
    api_key = os.getenv('API_KEY')
    website_id = os.getenv('WEBSITE_ID')
    common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
    uid = common.authenticate(db, username, api_key, {})

    if not uid:
        print("Authentication failed.")
        exit()
    else:
        print("Authenticated successfully. UID:", uid)
        models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')

        print(order['shipping_address'])

        # get the country id
        country_id = models.execute_kw(
            db, uid, api_key,
            'res.country', 'search',
            [[('code', '=', order['shipping_address']['country'])]]
        )

        print(country_id)
        if not country_id:
            print("Country not found.")
            return
        state_id = models.execute_kw(
            db, uid, api_key,
            'res.country.state', 'search',
            [[('code', '=', order['shipping_address']['state']
               ), ('country_id', '=', country_id[0])]]
        )

        print(state_id)
        if not state_id:
            print("State not found.")
            return

        # Define the order customer search criteria
        customer_search_criteria = [
            ['email', '=', order['customer_email']],
        ]

        # Search for the customer
        customer_id = models.execute_kw(
            db, uid, api_key,
            'res.partner', 'search',
            [customer_search_criteria]
        )

        if not customer_id:
            print("Customer not found.")

            # create a new customer
            customer_data = {
                'name': order['shipping_address']['first_name'] + ' ' + order['shipping_address']['last_name'],
                'email': order['customer_email'],
                'phone': order['shipping_address']['phone'],
                'street': order['shipping_address']['address1'][0],
                'city': order['shipping_address']['city'],
                'zip': order['shipping_address']['postcode'],
                'state_id': state_id[0],
                'country_id': country_id[0],
                'website_id': website_id,
            }

            customer_id = models.execute_kw(
                db, uid, api_key,
                'res.partner', 'create',
                [customer_data]
            )

            return
        
        print(customer_id)
        

    # create a new order to the odoo website store

    

    


if __name__ == '__main__':
    token = get_token()
    print(token)
    orders = get_orders(token)
    # create a new order to the odoo store
    for order in orders['data']:
        create_odoo_order(order, token)
    

