import os

class Config:
    SPOTIFY_PLAYLIST_ID = os.environ.get('SPOTIFY_PLAYLIST_ID', '')
