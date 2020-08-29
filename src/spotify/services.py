from src.spotify.clients.auth import TokenClient
from src.spotify.clients.playlist import PlaylistClient

def get_playlist(client_id, client_secret, playlist_id):
	auth_client = TokenClient(client_id, client_secret)
	token = auth_client.post()['access_token']

	return PlaylistClient().get(playlist_id, token)