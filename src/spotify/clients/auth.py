import base64
import requests

from requests.status_codes import codes as http_status_code

from src.spotify.exceptions import SpotifyAPIUnsuccessfulRequestException


class BaseClient:
	BASE_URL = 'https://accounts.spotify.com'


class TokenClient(BaseClient):
	PATH = '/token'

	def __init__(self, client_id, client_secret):
		self.client_id = client_id
		self.client_secret = client_secret

	@property
	def encoded_client(self):
		data = f'{self.client_id}:{self.client_secret}'.encode('ascii')
		return base64.b64encode(data)

	@property
	def header(self):
		return {
			'Authorization': f'Basic {self.encoded_client}',
			'Content-Type': 'application/x-www-form-urlencoded'
		}

	@property
	def url(self):
		return f'{self.BASE_URL}{self.PATH}'

	def post(self):
		body = {'grant_type': 'client_credentials'}

		response = requests.post(self.url, data=body, headers=self.header)
		if response.status_code !=  http_status_code.OK:
			raise SpotifyAPIUnsuccessfulRequestException(
				f'Spotify API Error: {response.status_code} - {response.json()}')

		return response.json()
