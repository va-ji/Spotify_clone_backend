from fastapi import FastAPI
from auth_spotify.authenticate_spotify import AuthenticateSpotify
from fastapi.middleware.cors import CORSMiddleware
from spotify_info.spotify_info_api import SpotifyInfoAPI
from tokens.spotify_tokens import spotifyTokens

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

auth_spotify = AuthenticateSpotify()
spotify_info_api = SpotifyInfoAPI()

@app.get("/")
def read_root():
    return {"result":"Hello World"}

@app.get("/authorise")
def get_spotify_url():
    try:
        url = auth_spotify.get_authenticate_url()
        return {"status_code":200,"result":url}
    except Exception as e:
        return {"status_code": 400, "result":str(e)}
    
@app.get("/authorise/token/{code}")
def get_authentication_tokens(code):
    auth_code = code
    try:
        response = auth_spotify.get_spotify_access_token(code=auth_code)
        access_token = response['access_token']
        refresh_token = response['refresh_token']
        spotifyTokens.set_spotify_access_token(access_token=access_token)
        spotifyTokens.set_spotify_refresh_token(refresh_token=refresh_token)
        return {"status_code":200,"result":"logged in"}
    except Exception as e:
        print(str(e))
        return {"status_code":400,"result":str(e)}

@app.get("/getUserInfo")
def get_spotify_user_info():
    access_token = spotifyTokens.access_token
    try:
        response = spotify_info_api.get_user_profile(access_token=access_token)
        print(response)
        return {"status_code":200,"result":response}
    except Exception as e:
        return {"status_code":400,"result":str(e)}