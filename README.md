<table align="center">
<tr>
<td align="center">
    <img src="/for_readme/spotify_icon.png" alt="Left Image" width="70"/>
</td>

<td align="center">
    <h1>Spotify Lyrics - Python Approach</h1>
</td>

<td align="center">
    <img src="/for_readme/musixmatch_icon.png" alt="Right Image" width="70"/>
</td>
</tr>
</table>


<br>

##  Description

A python approach to fetch Musixmatchs' (synchronized) lyrics via Spotify
  

-  **SP_DC Cookie**:  This cookie is used to obtain the access token required to make requests. A detailed guide on how to find the `SP_DC` cookie was provided by [akashrchandran](https://github.com/akashrchandran/akashrchandran) -> [here](https://github.com/akashrchandran/syrics/wiki/Finding-sp_dc).

  

-  **Access Token**: Once the `SP_DC` cookie is obtained, it is used to request an access token from Spotify. This token is then used to authenticate and authorize requests for fetching lyrics.

  

##  Disclaimer

This approach is not novel and takes inspiration from various GitHub projects that focus on fetching synchronized lyrics via Spotify. Notably, it draws from the work by [akashrchandran](https://github.com/akashrchandran), as seen in his [spotify-lyrics-api](https://github.com/akashrchandran/spotify-lyrics-api) project in PHP where he also provides a Rest API endpoint. This particular implementation offers a local, lightweight python approach.

  

Please note that this method involves accessing Musixmatch API synced lyrics via Spotify and might fall into a legal grey area. It is recommended to use this for personal, educational, or research purposes only, and not in a production environment.

  

##  Usage

To use this project, clone the repository and install the required dependencies. Make sure to obtain your `SP_DC` cookie and set it in your environment variables as `SP_DC_COOKIE`. Example usage can be found in `example_usage.py`.
I recommend using the icecream module for such lyrics projects , as it can structure your print statements and makes reading and debugging lyrics easier.
