import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

# Available scopes:

# Images
# ugc-image-upload

# Spotify Connect
# user-read-playback-state
# user-modify-playback-state
# user-read-currently-playing

# Playback
# app-remote-control
# streaming

# Playlists
# playlist-read-private
# playlist-read-collaborative
# playlist-modify-private
# playlist-modify-public

# Follow
# user-follow-modify
# user-follow-read

# Listening History
# user-read-playback-position
# user-top-read
# user-read-recently-played

# Library
# user-library-modify
# user-library-read

# Users
# user-read-email
# user-read-private


class SpotifySearch(spotipy.Spotify):

    def __init__(self):
        super().__init__()
        scope = "user-library-read,playlist-modify-public"
        self.scope = scope
        self.auth_manager = SpotifyOAuth(scope=self.scope,
                                         client_secret=os.environ.get("SPOTIFY_CLIENT_SECRET"),
                                         client_id=os.environ.get("SPOTIFY_CLIENT_ID"),
                                         redirect_uri="https://localhost:8888/callback")

    def get_artist_uri(self, artist_name):
        return self.search(q=f"artist: {artist_name}")["tracks"]["items"][0]["artists"][0]["uri"]

    def get_song_uri(self, song_name):
        return self.search(q=f"song: {song_name}")["tracks"]["items"][0]["uri"]

    def get_related_artists(self, artist_name):
        artist_uri = self.get_artist_uri(artist_name)
        related_artists = [artist["name"] for artist in self.artist_related_artists(artist_uri)["artists"]]
        return related_artists

    def get_top_tracks(self, artist_name):
        top_tracks = [track["name"] for track in self.artist_top_tracks(self.get_artist_uri(artist_name), country='US')["tracks"]]
        return top_tracks
