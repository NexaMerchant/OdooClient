
import os
from dotenv import load_dotenv
import requests
import json
import xmlrpc.client
import time
from math import ceil
import redis
from odoo_api import OdooApi
import shopify
import datetime
import subprocess
from push import push_feishu_message

# Load environment variables from .env file
load_dotenv()

store_mark = "CZ"


# login the store
def login():
    # Odoo server details
    url = os.getenv(store_mark + '_STORE_URL')
    username = os.getenv(store_mark + '_STORE_USERNAME')
    password = os.getenv(store_mark + '_STORE_PASSWORD')
    device_name = "odoo"

    # Authenticate use http post
    login_url = url + "/api/v1/admin/login"
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
    
def get_token(r):
    # check if the token is cached
    # token = os.getenv(store_mark + '_STORE_TOKEN')
    # token = "11862|jwA0yT6a6T07rUcBdnPZQ62ik1mwM6zUTGWPIv7eee91d1a3"
    # return token
    token = r.get(store_mark + '_STORE_TOKEN')
    if token:
        print("Token found in cache.")
        # string token
        token = token.decode('utf-8')
        print(token)
        return str(token)
    else:
        # if not cached, login and cache the token
        token = login()
        if token:
            r.set(store_mark + '_STORE_TOKEN', token)
        return token
    
def get_orders(token, page=1, limit=10):
    # Odoo server details
    url = os.getenv(store_mark + '_STORE_URL')
    # Authenticate use http post
    orders_url = f'{url}/api/v1/admin/sales/orders'
    
    headers = {
        'Authorization': "Bearer " + str(token),
        'Content-Type': 'application/json'
    }
    data = {
        "page": page,
        "limit": limit,
        "status": "processing",
        "sort": "created_at",
        "order": "desc",
    #    "id": 79606
    }

    print(orders_url + " " + str(data))

    response = requests.get(orders_url, json=data, headers=headers)
    print(response.status_code)
    #print(response.content)
    if response.status_code != 200:
        print("Failed to get orders.")
        #print(response.json())
        return None
    else:
        try:
            print("Get orders successfully.")
            response_data = response.json()
            #print(json.dumps(response_data, indent=4))
            return response_data
        except:
            print("Failed to get orders.")
            # clear the token
            r.delete(store_mark + '_STORE_TOKEN')
            return None
        response_data = response.json()
        # print(json.dumps(response_data, indent=4))
        # print(response_data)
        return response_data

# create a new order to the odoo store   
def create_odoo_order(order, token, r):
    # create a new customer to the odoo store
    url = os.getenv('URL')
    db = os.getenv('DB')
    username = os.getenv('USERNAME')
    api_key = os.getenv('API_KEY')
    website_id = os.getenv(store_mark + '_WEBSITE_ID')
    lang = os.getenv(store_mark + '_LANG')
    common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
    uid = common.authenticate(db, username, api_key, {})

    if not uid:
        print("Authentication failed.")
        exit()
    else:
        print("Authenticated successfully. UID:", uid)
        models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')

        print(order['shipping_address'])

        # check if the customer email is in the redis cache
        customer_id = r.get(order['customer_email'])

        if customer_id:
            print("Customer found in cache.")
            print(customer_id)
        else:
            print("Customer not found in cache.")

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
                state_id = 0
                #push_feishu_message("Order ID: " + str(order['id']) + order['shipping_address']['state']  + " State not found.")
                #return
            else:
                state_id = state_id[0]
                print(state_id)

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
                    #'street2': order['shipping_address']['address2'][0],
                    'city': order['shipping_address']['city'],
                    'zip': order['shipping_address']['postcode'],
                    'country_code': order['shipping_address']['country'],
                    'state_id': state_id[0],
                    'country_id': country_id[0],
                    'website_id': website_id,
                    'lang': lang,
                    'category_id': [8],
                    'type': 'delivery',
                # 'category_id': 8,
                }

                customer_id = models.execute_kw(
                    db, uid, api_key,
                    'res.partner', 'create',
                    [customer_data]
                )

                #return
            else:
                print("Customer found.")
                customer_id = customer_id[0]
            
            # print(customer_id)
            # Save email and customer id to redis
            r.set(order['customer_email'], customer_id)
        # create a new order to the odoo website store
        # check the order has created
        order_search_criteria = [
            ['origin', '=', order['id']],
        ]
        order_prefix = os.getenv(store_mark + '_ORDER_PREFIX')

        order_id = odoo.search('sale.order', order_search_criteria)

        # order_id = None

        currency_id = odoo.search('res.currency', [['name', '=', order['order_currency_code']]])
        print(currency_id)
        if not currency_id:
            print("Currency not found.")
            return
        currency_id = currency_id[0]

        if order_id:
            print("Order already exists.")
            print(order_id)
            order_id = order_id[0]
            print("Order already exists.")

            # update the order currency
            order_data = {
                'currency_id': currency_id,
                'name': order_prefix + str(order['id']),
            }
            odoo.write('sale.order', order_id, order_data)
            #return False
        else:
            
            # print(order['items'])
            #exit()
            # when order_lines is empty
          

            created_at = order['created_at']
            parsed_date = datetime.datetime.strptime(created_at, '%Y-%m-%dT%H:%M:%S.%fZ')
            formatted_date = parsed_date.strftime('%Y-%m-%d %H:%M:%S')

            
            # create a new order
            order_data = {
                'partner_id': int(customer_id),
                'origin': order['id'],
                'date_order': formatted_date,
                'website_id': website_id,
                'state': 'sale',
               # 'payment_term_id': 1,
                'create_date': formatted_date,
                #'order_line': order_lines,
                'invoice_status': 'to invoice',
                "currency_id": currency_id,
                'amount_total': order['grand_total'],
                'amount_tax': order['tax_amount'],
                'name': order_prefix + str(order['id']),
                'warehouse_id': 4,
                'company_id': 5,
                # 'partner_invoice_id': int(customer_id),
                # 'partner_shipping_id': int(customer_id),
                # 'picking_policy': 'direct',
                # 'pricelist_id': 1,
                # 'company_id': 1,
                # 'warehouse_id': 1,
              #  'note': order['note'], 
               #  'warehouse_id': 1,
            }

            print(order_data)

            order_id = odoo.create('sale.order', order_data)
        print(f'Order ID: {order_id}')

        order_lines = []
        for item in order['items']:
            additional_sku = item['additional']['product_sku']
            print(additional_sku)
            additional_sku = additional_sku.split('-')
            print(additional_sku)
            shopify_product_id = additional_sku[0]
            shopify_variant_id = additional_sku[1]

            #print(shopify_product_id)
            #print(shopify_variant_id)

            odoo_product_id = r.get(f'product:{shopify_product_id}')
            if odoo_product_id:
                odoo_product_id = int(odoo_product_id)
            print(odoo_product_id)
            odoo_variant_id = r.get(f'product:{odoo_product_id}:{shopify_variant_id}')
            if odoo_variant_id:
                odoo_variant_id = int(odoo_variant_id)
            print(odoo_variant_id)
            #exit()

            if not odoo_product_id:
                print("Product not found." + str(shopify_product_id))
                push_feishu_message("Order ID: " + str(order['id']) + " Product not found." + str(shopify_product_id))
                continue
                # exit()
            if not odoo_variant_id:
                print("Variant not found." + str(odoo_product_id) + " " + str(shopify_variant_id))
                push_feishu_message("Order ID: " + str(order['id']) + " Variant not found." + str(odoo_product_id) + " " + str(shopify_variant_id))
                continue
                # exit()
                

            print(item)
            # create a new order line
            name = item['name']
            print(type(item['children']))
            if item['children']:
                name = item['children'][0]['name']
            order_line_data = {
                'product_id': int(odoo_variant_id),
                # 'variant_id': odoo_variant_id,
                'product_uom_qty': item['qty_ordered'],
                'price_unit': item['price'],
                'currency_id': currency_id,
                'name': name,
            }

            order_lines.append((order_line_data))
        print(order_lines)

        # create a new order line
        for order_line in order_lines:
            order_line['order_id'] = int(order_id)
            print(order_line)

            # check the order line has created
            order_line_search_criteria = [
                ['order_id', '=', order_id],
                ['product_id', '=', order_line['product_id']],
            ]

            order_line_id = odoo.search('sale.order.line', order_line_search_criteria)

            if order_line_id:
                order_line_id = order_line_id[0]
                print("Order line already exists.")
                continue
            else:
                order_line_id = odoo.create('sale.order.line', order_line)
                print(order_line_id)   


if __name__ == '__main__':
    
    max = 80000
    page = ceil(max / 20)

    redis_host = os.getenv('REDIS_HOST')
    redis_port = os.getenv('REDIS_PORT')
    redis_db = os.getenv('REDIS_DB')
    redis_password = os.getenv('REDIS_PASSWORD')

    # create a connection to the redis server
    r = redis.Redis(host=redis_host, port=redis_port, db=redis_db, password=redis_password)
    odoo = OdooApi(os.getenv('URL'), os.getenv('DB'), os.getenv('USERNAME'), os.getenv('API_KEY'))

    shop_url = os.getenv(store_mark + '_SHOPIFY_HOST')
    api_version = os.getenv(store_mark + '_SHOPIFY_API_VERSION')
    private_app_password = os.getenv(store_mark +'_SHOPIFY_ACCESS_TOKEN')
    session = shopify.Session(shop_url, api_version, private_app_password)
    shopify.ShopifyResource.activate_session(session)
    print("Authenticated successfully." + session.url)

    token = get_token(r)
    print(token)

    
    for i in range(1, page):
        print("page: " + str(i))
        orders = get_orders(token, i, 20)
        if orders is None:
            print("Failed to get orders.")
            exit()
        # create a new order to the odoo store
        for order in orders['data']:
            create_odoo_order(order, token, r)
            # wait for 1 second
            time.sleep(1)
            #exit()

    
    

