from fastapi import FastAPI
from auth_spotify.authenticate_spotify import AuthenticateSpotify

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello":"World"}

@app.get("/authorise")
def get_spotify_url():
    auth_spotify = AuthenticateSpotify()
    url = auth_spotify.get_authenticate_url()
    return {"status_code":200,"result":url}