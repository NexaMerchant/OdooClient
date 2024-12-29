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
import hashlib

# Load environment variables from .env file
load_dotenv()

if __name__ == '__main__':

    url = os.getenv("BANLINGKIT_API_URL") + "/invoice/lists"

    header = {
        "Content-Type": "application/json;charset=UTF-8",
        "salt": os.getenv("BANLINGKIT_API_SALT"),
    }

    data = {
        "page": 0,
        "limit": 10
    }

    # put request
    response = requests.put(url, headers=header, data=data)

    print(response.text)