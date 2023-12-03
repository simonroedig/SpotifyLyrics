import requests
import time

class SpotifyLyrics:
    def __init__(self, sp_dc_cookie):
        if not sp_dc_cookie:
            raise Exception("Missing SP_DC cookie")
        # Access token
        self.cached_access_token = None
        # SP_DC cookie
        self.sp_dc_cookie = sp_dc_cookie

    def getLyrics(self, track_id):
        self.verifyAccessTokenExpire()

        try:
            formatted_url = f"https://spclient.wg.spotify.com/color-lyrics/v2/track/{track_id}?format=json&market=from_token"

            response = requests.get(
                formatted_url, 
                headers={**getBrowserHeader(), **{"Authorization": f"Bearer {self.cached_access_token['accessToken']}"}}
            )
            response.raise_for_status()
            
            return response.json()
        
        except Exception as e:
            raise Exception(f"Failed to get spotify lyrics: {e}")

    def getAccessToken(self):
        # Check if access token already exists
        if self.cached_access_token:
            return self.cached_access_token

        try:
            # Spotify token endpoint
            response = requests.get(
                "https://open.spotify.com/get_access_token?reason=transport&productType=web_player",
                headers={**getBrowserHeader(), **{"cookie": f"sp_dc={self.sp_dc_cookie}"}}
            )
            response.raise_for_status()
            
            self.cached_access_token = response.json()
            return self.cached_access_token
        
        except Exception as e:
            raise Exception(f"Failed to get access token: {e}")

    def verifyAccessTokenExpire(self):
        if self.cached_access_token and self.cached_access_token["accessTokenExpirationTimestampMs"] > int(time.time() * 1000):
            return

        try:
            self.cached_access_token = self.getAccessToken()
            
        except Exception as e:
            raise Exception(f"Failed to refresh spotify access token: {e}")
    
    def convertJsonLyricsToTupelArray(self, lyrics_json):
        try:
            # Extract lyrics part from json
            lyrics_part = lyrics_json['lyrics']['lines']
            # Create tupel array with start time and words
            tupel_array = [(line['startTimeMs'], line['words']) for line in lyrics_part]
            
            return tupel_array
        
        except Exception as e:
            raise Exception(f"Failed to convert json lyrics to tupel array: {e}")

# Simulate request from a browser with headers
def getBrowserHeader():
    return {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36",
        "App-platform": "WebPlayer", # Indicating that the request is coming from a web-based Spotify player
        "content-type": "text/html; charset=utf-8",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.5",
        "Referer": "https://open.spotify.com/", # Adress of previous webpage
        "Connection": "keep-alive", # Typical browser behavior
    }




