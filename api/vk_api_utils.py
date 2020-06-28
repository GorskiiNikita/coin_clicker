import json

import requests

from coin_clicker import settings


def get_server_access_token():
    url = f'https://oauth.vk.com/access_token?client_id={settings.CLIENT_ID}&client_secret={settings.CLIENT_SECRET}&grant_type=client_credentials&v=5.101'
    resp = requests.get(url)
    server_access_token = json.loads(resp.text)['access_token']
    return server_access_token


def check_user_access_token(user_access_token):
    url = f'https://api.vk.com/method/secure.checkToken?client_secret={settings.CLIENT_SECRET}&token={user_access_token}&access_token=<access_token приложения>&v=5.101'
    resp = requests.get(url)
    return json.loads(resp.text)

