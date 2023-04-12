import json
from dotenv import load_dotenv
import os

import requests
class SpotifyInfoAPI:
    def __init__(self) -> None:
        load_dotenv()
        self.base_url = os.getenv('SPOTIFY_API_URL')
    
    def get_user_profile(self,access_token = None):
        if access_token is None:
            return
        url = self.base_url + '/me'
        auth = f"Bearer {access_token}"
        headers= {'Authorization': auth}

        try:
            response = requests.get(url=url,headers=headers)
            response = json.loads(response.content.decode('utf-8'))
            return response
        except Exception as e:
            raise Exception(str(e))

