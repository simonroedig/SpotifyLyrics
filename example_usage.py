from dotenv import load_dotenv
import os
from icecream import ic

from spotify_lyrics import SpotifyLyrics

def main():
    # Track id for Red Hot Chili Peppers - Californication
    track_id = "48UPSzbZjgc449aqz8bxox"

    try:
        sp_dc_cookie = os.getenv("SP_DC_COOKIE")
        spotify = SpotifyLyrics(sp_dc_cookie)
        
        lyrics_json = spotify.getLyrics(track_id)
        ic(lyrics_json)
        
        lyrics_tupel_array = spotify.convertJsonLyricsToTupelArray(lyrics_json)
        ic(lyrics_tupel_array)
        
    except Exception as e:
        print(f"An error occurred: {e}")
        
if __name__ == '__main__':
    load_dotenv()
    main()
    