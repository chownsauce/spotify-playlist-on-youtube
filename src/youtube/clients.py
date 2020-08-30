import json
import requests

from requests.status_codes import codes as http_status_code

from src.youtube.exceptions import YouTubeAPIUnsuccessfulRequestException


class BaseClient:
	BASE_URL = 'https://www.googleapis.com/youtube/v3'


class PlaylistClient(BaseClient):
	BASE_PATH = '/playlists'

	@property
	def url(self):
		return f'{self.BASE_URL}{self.BASE_PATH}?part=snippet&alt=json'

	def post(self, playlist_name, auth_token):
		header = {'Authorization': f'Bearer {auth_token}'}
		body = {
			'snippet': {
				'title': playlist_name
			}
		}
		response = requests.post(self.url, headers=header, json=body)
		
		if response.status_code !=  http_status_code.OK:
			raise YouTubeAPIUnsuccessfulRequestException(
				f'Youtube API Error: {response.status_code} - {response.json()}')

		return response.json()