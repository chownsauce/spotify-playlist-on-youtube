from src.spotify.clients.auth import TokenClient
from src.spotify.clients.playlist import PlaylistClient
from src.spotify.factories import TrackFactory, PlaylistFactory

def get_playlist(client_id, client_secret, playlist_id):
	auth_client = TokenClient(client_id, client_secret)
	token = auth_client.post()['access_token']

	playlist_client = PlaylistClient()
	data = playlist_client.get(playlist_id, token)
	playlist = data['tracks']
	tracks = []

	while True:
		tracks += [TrackFactory.create(item['track']) for item in playlist['items']]
		
		next_page = playlist['next']
		if not next_page: break

		playlist = playlist_client.next(next_page, token)
		
	
	return PlaylistFactory.create(data, tracks)
	