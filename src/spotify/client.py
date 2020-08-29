import requests

from requests.status_codes import codes as http_status_code

from src.spotify.exceptions import SpotifyAPIUnsuccessfulRequestException


class BaseClient:
	BASE_URL = 'https://api.spotify.com/v1'


class PlaylistClient(BaseClient):
	PATH = '/playlists'

	@property
	def url(self):
		return f'{self.BASE_URL}{self.PATH}'

	def get(self, playlist_id):
		url = f'{self.url}/{playlist_id}'
		response = requests.get(url)
		if response.status_code !=  http_status_code.OK:
			raise SpotifyAPIUnsuccessfulRequestException(
				f'Spotify API Error: {response.status_code} - {response.json()}')

		return response.json()
