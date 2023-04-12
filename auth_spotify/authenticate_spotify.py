import json
from dotenv import load_dotenv
import os
from auth_spotify.code_challenge import CodeChallenge
from urllib.parse import urlencode
import requests

class AuthenticateSpotify:

    def __init__(self):
        load_dotenv()
        self.client_id = os.getenv("CLIENT_ID")
        self.redirect_uri = os.getenv("REDIRECT_URI")
        self.base_url = os.getenv("SPOTIFY_BASE_URL")
    
    def get_authenticate_url(self):
        code_challenge = CodeChallenge.generate_code_challenge()
        
        url_path = self.base_url + '/authorize'
        scope = 'user-read-private user-read-email streaming user-read-playback-state user-modify-playback-state user-read-currently-playing playlist-modify-private playlist-modify-public'
        params = {
            "response_type": 'code',
            "client_id": self.client_id,
            "scope": scope,
            "redirect_uri": self.redirect_uri,
            "code_challenge_method": 'S256',
            "code_challenge": code_challenge
        }

        query_string = urlencode(params)
        url = f'{url_path}?{str(query_string)}'

        print('url: ' + url)

        return url
    
    def get_spotify_access_token(self,code=''):
        
        code_verifier = CodeChallenge.code_verifier
        print(f'code verifier: {CodeChallenge.code_verifier}')
        body = {
            "grant_type": 'authorization_code',
            "code": code,
            "redirect_uri": self.redirect_uri,
            "client_id": self.client_id,
            "code_verifier": code_verifier
        }
        headers= {'Content-Type': 'application/x-www-form-urlencoded'}
        url = self.base_url + '/api/token'
        try:
            response = requests.post(url=url,headers=headers,data=body)
            response = json.loads(response.content.decode('utf-8'))
            
            data = {
                "access_token" : response['access_token'],
                "refresh_token": response['refresh_token'],
                "expires_in":response['refresh_token']
            }
            return data
        except Exception as e:
            raise Exception(str(e))
        


