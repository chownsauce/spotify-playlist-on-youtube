import os

class Config:
    SPOTIFY_PLAYLIST_ID = os.environ.get('SPOTIFY_PLAYLIST_ID', '')
    SPOTIFY_CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID', '')
    SPOTIFY_CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET', '')
    YOUTUBE_CLIENT_ID = os.environ.get('YOUTUBE_CLIENT_ID', '')
    YOUTUBE_CLIENT_SECRET = os.environ.get('YOUTUBE_CLIENT_SECRET', '')