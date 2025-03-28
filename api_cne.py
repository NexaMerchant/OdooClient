import os
from dotenv import load_dotenv
import requests
import time
import hashlib

# Load environment variables from .env file
load_dotenv()

def get_secret(timestamp):
    api_token = os.getenv("CNE_API_TOKEN")
    api_cid = os.getenv("CNE_API_CID")
    

    print(api_cid)
    print(timestamp)
    print(api_token)

    combined = (api_cid + timestamp + api_token).encode('utf-8')

    # md5 hash
    secret = hashlib.md5(combined).hexdigest()
    # unlowercase
    return secret.lower()


if __name__ == '__main__':
    timestamp = str(int(time.time()*1000))
    secret = get_secret(timestamp)
    
    url = os.getenv("CNE_API_URL") + "/cgi-bin/EmsData.dll?DoApi"
    headers = {
        "Content-Type": "application/json;charset=UTF-8"
    }

    # @link https://apifox.com/apidoc/shared-6eba6d59-905d-4587-810b-607358a30aa3/doc-2909519
    data = {
        "RequestName": "EmsKindList",
        "icID": os.getenv("CNE_API_CID"),
        "TimeStamp": timestamp,
        "MD5": secret
    }

    response = requests.post(url, headers=headers, json=data)

    print(response.text)