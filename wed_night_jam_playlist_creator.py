import pandas
from spotify_search import SpotifySearch
import os

# Instantiate SpotifySearch object

sp = SpotifySearch()

# Get user input date

date = input("Enter jam date (M_D_YY): ")

# Open csv and put songs into dictionary

with open(f"song_lists/Wednesday night Jam songs - {date}.csv") as file:
    df = pandas.read_csv(file)
    song_dict = df.to_dict('records')
    print(song_dict)

# Create URI list

uri_list = []
for song in song_dict:
    try:
        uri = sp.search(q=f"track: {song['title']}, artist: {song['artist']}")["tracks"]["items"][0]["uri"]
        uri_list.append(uri)
    except IndexError:
        pass

# Create playlist and add songs

playlist_create = sp.user_playlist_create(
    user=os.environ.get("SPOTIFY_USER_ID"),
    name=f"{date} KK jam",
    public=True,
    collaborative=False,
    description='')

playlist_add = sp.playlist_add_items(playlist_id=playlist_create['id'], items=uri_list, position=None)
