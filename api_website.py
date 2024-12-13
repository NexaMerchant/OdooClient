import os
from dotenv import load_dotenv
import requests
import json
import xmlrpc.client

# Load environment variables from .env file
load_dotenv()

def get_websites():
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

        # Specify the model you want to inspect
        model_name = 'website'

        print(f"Fields of model: {model_name}")

        # get websites list
        websites = models.execute_kw(
            db, uid, api_key,
            model_name, 'search_read',
            [[]],
            {'fields': ['name', 'domain', 'company_id']}
        )
        print(websites)

        # get company list
        companies = models.execute_kw(
            db, uid, api_key,
            'res.company', 'search_read',
            [[]],
            {'fields': ['name']}
        )

        print(companies)

        # get partner list
        partners = models.execute_kw(
            db, uid, api_key,
            'res.partner', 'search_read',
            [[]],
            {}
        )

        # print(partners)

        # get partner 标签 list
        partner_tags = models.execute_kw(
            db, uid, api_key,
            'res.partner.category', 'search_read',
            [[]],
            {'fields': ['name']}
        )

        print(partner_tags)

        # # update the websites company_id
        # for website in websites:
        #     print(website['id'])
        #     models.execute_kw(
        #         db, uid, api_key,
        #         model_name, 'write',
        #         [[website['id']], {'company_id': 5}]
        #     )

if __name__ == '__main__':
    # get the websites from odoo
    websites = get_websites()