from dotenv import load_dotenv
import os
from auth_spotify.code_challenge import CodeChallenge
from urllib.parse import urlencode

class AuthenticateSpotify:

    def __init__(self):
        load_dotenv()
    
    def get_authenticate_url(self):
        code_challenge = CodeChallenge.generate_code_challenge()
        client_id = os.getenv("CLIENT_ID")

        redirect_uri = os.getenv("REDIRECT_URI")
        base_url = 'https://accounts.spotify.com/authorize'
        scope = 'user-read-private user-read-email streaming user-read-playback-state user-modify-playback-state user-read-current-playing playlist-modify-private playlist-modify-public'
        params = {
            "response_type": 'code',
            "client_id": client_id,
            "scope": scope,
            "redirect_uri": redirect_uri,
            "code_challenge_method": 'S256',
            "code_challenge": code_challenge
        }

        url = base_url + '?' + urlencode(params)

        print('url: ' + url)

        return url


