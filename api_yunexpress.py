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
import base64


# Load environment variables from .env file
load_dotenv()

if __name__ == '__main__':
    api_cid = os.getenv("YUNEXPRESS_API_CID")
    api_secret = os.getenv("YUNEXPRESS_API_SECRET")
    api_url = os.getenv("YUNEXPRESS_API_URL")

    # @link https://yunexpress-uc-down.oss-cn-shenzhen.aliyuncs.com/YT-PRO/UCV2/%E4%BA%91%E9%80%94%E7%89%A9%E6%B5%81API%E6%8E%A5%E5%8F%A3%E5%BC%80%E5%8F%91%E8%A7%84%E8%8C%83OMS-20250207.pdf

    token = api_cid + "&" + api_secret
    print(token)
    # base 64 encode
    base64_token = base64.b64encode(token.encode('utf-8')).decode('utf-8')

    # 2.2 查询运输方式
    url = api_url + "/api/Common/GetCountry"
    print(url)
    headers = {
        "Content-Type": "application/json;charset=UTF-8",
        "Accept": "application/json",
        "Authorization": "Basic " + base64_token
    }

    print(headers)

    data = {
    }
    response = requests.get(url, headers=headers, json=data)
    print(response.text)