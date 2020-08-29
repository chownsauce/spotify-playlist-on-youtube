from src.app.config import Config
from src.spotify.services import get_playlist

def run():
	return get_playlist(
		Config.SPOTIFY_CLIENT_ID, Config.SPOTIFY_CLIENT_SECRET, Config.SPOTIFY_PLAYLIST_ID)
	