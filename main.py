import json
from fastapi import FastAPI
from auth_spotify.authenticate_spotify import AuthenticateSpotify
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"result":"Hello World"}

@app.get("/authorise")
def get_spotify_url():
    auth_spotify = AuthenticateSpotify()
    url = auth_spotify.get_authenticate_url()
    return {"status_code":200,"result":url}