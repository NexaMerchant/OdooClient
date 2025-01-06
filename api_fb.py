import os
import requests
from dotenv import load_dotenv

def fb_apps_ads_view(request):
    access_token = os.getenv('FB_APP_ACCESS_TOKEN')
    app_id = os.getenv('FB_APP_ID')
    url = f"https://graph.facebook.com/v12.0/{app_id}/ads"
    params = {
        'access_token': access_token,
        'fields': 'id,name,status',
    }
    response = requests.get(url, params=params)
    ads = response.json()
    return ads

if __name__ == '__main__':
    load_dotenv()
    ads = fb_apps_ads_view(None)
    print(ads)