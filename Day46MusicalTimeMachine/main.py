from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

CLIENT_ID="9392e8c72b414610ba0aac46cea11104"
CLIENT_SECRET="55fd26340116495fb1e297cacb8cecb1"
REDIRECT="http://example.com"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="",
        client_id="",
        client_secret="",
        show_dialog=True,
        cache_path="token.txt",
        username="Joshua Filer",
    )
)
user_id = sp.current_user()["id"]

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
website_url = f"https://www.billboard.com/charts/hot-100/{date}/"
response = requests.get(website_url)
soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", limit=1, type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")



