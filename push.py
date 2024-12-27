import os
from dotenv import load_dotenv
import requests

load_dotenv()

def push_feishu_message(content):
    url = os.getenv("FEISHU_WEBHOOK")
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "msg_type": "post",
        "content": {
            "post": {
                "zh_cn": {
                    "title": "Sync Execution",
                    "content": [
                        [
                            {
                                "tag": "text",
                                "text": content
                            }
                        ]
                    ]
                }
            }
        }
    }
    requests.post(url, headers=headers, json=data)