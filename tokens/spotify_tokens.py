class spotifyTokens:
    access_token = None
    refresh_token = None
    expire_time = None

    @staticmethod
    def set_spotify_access_token(access_token = None):
        if access_token is None:
            return
        spotifyTokens.access_token = access_token
    
    @staticmethod
    def set_spotify_refresh_token(refresh_token = None):
        if refresh_token is None:
            return
        spotifyTokens.refresh_token = refresh_token
    
    @staticmethod
    def set_spotify_expire_time(time = None):
        if time is None:
            return
        spotifyTokens.expire_time = time
        