<table align="center">
<tr>
<td align="center">
    <img src="/for_readme/spotify_icon.png" alt="Spotify icon" width="70"/>
</td>

<td align="center">
    <h1>Spotify Lyrics - Python Approach</h1>
</td>

<td align="center">
    <img src="/for_readme/musixmatch_icon.png" alt="Musixmatch icon" width="70"/>
</td>
</tr>
</table>

<br>

##  Description
A python approach to fetch Musixmatchs' (synchronized) lyrics via Spotify

##  Usage
-  **spotify_lyrics.py**: Main module
-  **example_usage.py**: Demonstrating its usage

```
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
```
```
ic| lyrics_json: {'colors': {'background': -16745031, 'highlightText': -1, 'text': -16777216},
                  'hasVocalRemoval': False,
                  'lyrics': {'alternatives': [],
                             'capStatus': 'NONE',
                             'fullscreenAction': 'FULLSCREEN_LYRICS',
                             'isDenseTypeface': False,
                             'isRtlLanguage': False,
                             'language': 'en',
                             'lines': [{'endTimeMs': '0',
                                        'startTimeMs': '20530',
                                        'syllables': [],
                                        'words': 'Psychic spies from China try to steal your '
                                                 "mind's elation"},
                                       {'endTimeMs': '0',
                                        'startTimeMs': '25400',
                                        'syllables': [],
                                        'words': 'And little girls from Sweden dream of '     
                                                 'silver-screen quotation'},
                                       {'endTimeMs': '0',
                                        'startTimeMs': '30420',
                                        'syllables': [],
                                        'words': 'And if you want these kind of dreams'},
                                       {'endTimeMs': '0',
```
``` 
        lyrics_tupel_array = spotify.convertJsonLyricsToTupelArray(lyrics_json)
        ic(lyrics_tupel_array)
``` 
```
ic| lyrics_tupel_array: [('20530', "Psychic spies from China try to steal your mind's elation"),
                         ('25400', 'And little girls from Sweden dream of silver-screen quotation'),
                         ('30420', 'And if you want these kind of dreams'),
                         ('33030', "It's Californication"),
                         ('36460', '♪'),
                         ('45180', "It's the edge of the world, end all of western civilization"),
                         ('50570',
                          "The Sun may rise in the East, at least it's settled in the final location"),
                         ('55650', "It's understood that Hollywood sells Californication"),
                         ('61380', '♪'),
                         ('70890', 'Pay your surgeon very well to break the spell of aging'),
                         ('75430', "Celebrity skin, is this your chin, or is that war you're waging?"),
                         ('81770', 'Firstborn unicorn'),
                         ('85860', 'Hardcore soft-porn'),
                         ('90450', 'Dream of Californication'),
```
``` 
    except Exception as e:
        print(f"An error occurred: {e}")
        
if __name__ == '__main__':
    load_dotenv()
    main()
```   



Clone the repository or simple copy 'spotify_lyrics.py' into your project and install the required dependencies. Make sure to obtain your `SP_DC` cookie and set it in your environment variables as `SP_DC_COOKIE`. Example usage can be found in `example_usage.py`.
I recommend using the icecream module for such lyrics projects as it can structure your print/log statements and makes reading and debugging lyrics easier.

## Further Exmplanation
-  **SP_DC Cookie**:  This cookie is used to obtain the access token required to request lyrics via Spotify. A detailed guide on how to find the `SP_DC` cookie was provided by [akashrchandran](https://github.com/akashrchandran/akashrchandran) -> [here](https://github.com/akashrchandran/syrics/wiki/Finding-sp_dc).
You need to manually retrieve this cookie from a browser session, where you are logged into Spotify. (Cookie is valid for about a year).
There are no straightforward methods to retrieve the SP_DC cookie programmatically due to the way web cookies are managed.

-  **Access Token**: Once the `SP_DC` cookie is obtained, it is used to request an access token from Spotify. This token is then used to authenticate and authorize requests for fetching lyrics.

  

##  Disclaimer
This approach is not novel and takes inspiration from various GitHub projects that focus on fetching synchronized lyrics via Spotify. Notably, it draws from the work by [akashrchandran](https://github.com/akashrchandran), as seen in his [spotify-lyrics-api](https://github.com/akashrchandran/spotify-lyrics-api) project in PHP where he also provides a Rest API endpoint. This particular implementation offers a local, lightweight python approach.

Please note that this method involves accessing Musixmatch API synced lyrics via Spotify and might fall into a legal grey area. It is recommended to use this for personal, educational, or research purposes only, and not in a production environment.

  


