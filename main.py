from fastapi import FastAPI
from auth_spotify.authenticate_spotify import AuthenticateSpotify
from fastapi.middleware.cors import CORSMiddleware

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

@app.get("/")
def read_root():
    return {"result":"Hello World"}

@app.get("/authorise")
def get_spotify_url():
    url = auth_spotify.get_authenticate_url()
    return {"status_code":200,"result":url}

@app.get("/authorise/token/{code}")
def get_access_token(code):
    auth_code = code
    response = auth_spotify.get_spotify_access_token(code=auth_code)
   
    return {"status_code":200,"result":response}