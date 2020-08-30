import json
import requests

from requests.status_codes import codes as http_status_code

from src.youtube.exceptions import YouTubeAPIUnsuccessfulRequestException


class BaseClient:
	BASE_URL = 'https://www.googleapis.com/youtube/v3'

	def __init__(self, auth_token):
		self.auth_token = auth_token

	@property
	def header(self):
		return {'Authorization': f'Bearer {self.auth_token}'}

	def post(self, url, *args, **kwargs):
		response = requests.post(url, **kwargs)
		
		if response.status_code !=  http_status_code.OK:
			raise YouTubeAPIUnsuccessfulRequestException(
				f'Youtube API Error: {response.status_code} - {response.json()}')

		return response.json()


class PlaylistClient(BaseClient):

	def get_url(self, base_path):
		return f'{self.BASE_URL}{base_path}?part=snippet&alt=json'

	def create(self, playlist_name):
		base_path = '/playlists'
		body = {
			'snippet': {
				'title': playlist_name,
				'description': 'Playlist created with spotify-playlist-on-youtube'
			}
		}
		return self.post(
			self.get_url(base_path), headers=self.header, json=body)

	def add_video(self, playlist_id, video_id):
		base_path = '/playlistItems'
		body = {
			'snippet': {
				'playlistId': playlist_id,
				'resourceId': {
					'videoId': video_id
				}
			}
		}
		return self.post(
			self.get_url(base_path), headers=self.header, json=body)