# Example: Fetch product information from 1688 using environment variables and requests

import os
import hashlib
import time
import requests
import hmac
import json
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

ALI1688_APPKEY = os.getenv('ALI1688_APPKEY')
ALI1688_APPSECRET = os.getenv('ALI1688_APPSECRET')
ALI1688_ACCESS_TOKEN = os.getenv('ALI1688_ACCESS_TOKEN')

def generate_1688_signature(url_path: str, params: dict, secret_key: str) -> str:
    """
    生成 1688 API 签名
    
    :param url_path: 不带协议和域名的路径部分（例如：param2/1/system/currentTime/1000000）
    :param params: 查询参数（例如：{'b': '2', 'a': '1'}）
    :param secret_key: 对应 appKey 的签名密钥
    :return: 签名字符串（大写十六进制）
    """
    # 步骤1：拼接参数，key + value，然后按 key 的字典序排序
    sorted_items = sorted(params.items())
    param_string = ''.join([f"{k}{v}" for k, v in sorted_items])
    
    # 步骤2：拼接签名因子
    sign_factor = f"{url_path}{param_string}"
    
    # 步骤3：使用 HMAC-SHA1 加密
    hmac_obj = hmac.new(secret_key.encode('utf-8'), sign_factor.encode('utf-8'), hashlib.sha1)
    signature = hmac_obj.hexdigest().upper()

    return signature

#link https://open.1688.com/api/apidocdetail.htm?spm=1688open.api-list.0.0.257f55edurLMtG&aopApiCategory=product_new&id=com.alibaba.product%3Aalibaba.product.get-1
def fetch_ali1688_product_info(product_id: str):

    url ="https://gw.open.1688.com/openapi/"
    # 目标接口：alibaba.product.get
    apiInfo = "param2/1/com.alibaba.product/alibaba.product.simple.get/"+ALI1688_APPKEY
    # 公共参数
    params = {
        "access_token": ALI1688_ACCESS_TOKEN,
        "productID": product_id,
        "webSite": "1688",
        "_aop_timestamp": str(int(time.time() * 1000)),
        "appKey": ALI1688_APPKEY,
        "v": "1.0"
    }
    # 生成签名
    #params["_aop_signature"] = make_sign(params, ALI1688_APPSECRET)

    signature = generate_1688_signature(apiInfo, params, ALI1688_APPSECRET)
    params["_aop_signature"] = signature
    print(signature) 
    print("请求url：", url + apiInfo)

    try:
        resp = requests.post(url + apiInfo, params=params, timeout=60)
        # print("请求 URL：", resp.url)
        # print("请求参数：", params)
        # print("请求头：", resp.request.headers)
        # print("请求体：", resp.request.body)
        # print("响应头：", resp.headers)
        # print("响应体：", resp.text)
        resp.raise_for_status()
        data = resp.json()
        #print("API 返回数据：", data)
        return data 
    except requests.RequestException as e:
        print("请求 1688 接口出错：", e)
        return None
    
#alibaba.trade.getBuyerOrderList
def fetch_ali1688_order_list():
    url ="https://gw.open.1688.com/openapi/"
    # 目标接口：alibaba.product.get
    apiInfo = "param2/1/com.alibaba.trade/alibaba.trade.getBuyerOrderList/"+ALI1688_APPKEY
    # 公共参数
    params = {
        "access_token": ALI1688_ACCESS_TOKEN,
        "webSite": "1688",
        "_aop_timestamp": str(int(time.time() * 1000)),
        "appKey": ALI1688_APPKEY,
        "v": "1.0"
    }
    # 生成签名
    #params["_aop_signature"] = make_sign(params, ALI1688_APPSECRET)

    signature = generate_1688_signature(apiInfo, params, ALI1688_APPSECRET)
    params["_aop_signature"] = signature
    print(signature) 
    print("请求url：", url + apiInfo)
    try:
        resp = requests.post(url + apiInfo, params=params, timeout=60)
        # print("请求 URL：", resp.url)
        # print("请求参数：", params)
        # print("请求头：", resp.request.headers)
        # print("请求体：", resp.request.body)
        # print("响应头：", resp.headers)
        # print("响应体：", resp.text)
        resp.raise_for_status()
        data = resp.json()
        #print("API 返回数据：", data)
        return data 
    except requests.RequestException as e:
        print("请求 1688 接口出错：", e)
        return None
    
# product.keywords.search
def fetch_ali1688_product_search():
    url ="https://gw.open.1688.com/openapi/"
    # 目标接口：alibaba.product.get
    apiInfo = "param2/1/com.alibaba.fenxiao/product.keywords.search/"+ALI1688_APPKEY
    # 公共参数
    params = {
        "access_token": ALI1688_ACCESS_TOKEN,
        "webSite": "1688",
        "_aop_timestamp": str(int(time.time() * 1000)),
        "appKey": ALI1688_APPKEY,
        "param": json.dumps({"keywords": "内衣"}),
        "v": "1.0"
    }
    # 生成签名
    #params["_aop_signature"] = make_sign(params, ALI1688_APPSECRET)

    signature = generate_1688_signature(apiInfo, params, ALI1688_APPSECRET)
    params["_aop_signature"] = signature
    print(signature) 
    print("请求url：", url + apiInfo)
    try:
        resp = requests.post(url + apiInfo, params=params, timeout=60)
        # print("请求 URL：", resp.url)
        # print("请求参数：", params)
        # print("请求头：", resp.request.headers)
        # print("请求体：", resp.request.body)
        # print("响应头：", resp.headers)
        # print("响应体：", resp.text)
        resp.raise_for_status()
        data = resp.json()
        print("API 返回数据：", data)
        return data 
    except requests.RequestException as e:
        print("请求 1688 接口出错：", e)
        return None


if __name__ == "__main__":
    pid = "713730241172"
    pid = "575619858008"
    #pid = "824680340761"
    #info = fetch_ali1688_product_info(pid)
    #print(json.dumps(info, indent=4, ensure_ascii=False))
    items = fetch_ali1688_order_list()
    print(json.dumps(items, indent=4, ensure_ascii=False))
    # items = fetch_ali1688_product_search()
    # print(json.dumps(items, indent=4, ensure_ascii=False))