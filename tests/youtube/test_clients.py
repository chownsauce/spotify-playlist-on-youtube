import pytest

from requests.status_codes import codes as http_status_code
from unittest.mock import patch, Mock

from src.youtube.clients import PlaylistClient
from src.youtube.exceptions import YouTubeAPIUnsuccessfulRequestException


def test_playlist_client_has_correct_setup():
	client = PlaylistClient('token')

	assert client.header == {'Authorization': 'Bearer token'}
	assert client.get_url('/playlists') == 'https://www.googleapis.com/youtube/v3/playlists?part=snippet&alt=json'


@patch('src.youtube.clients.requests')
def test_create_playlist_successfully(mocked_requests):
	expected = {'Playlist': {'Madonna': 'I\'m gonna break the cycle'}}
	response = Mock(status_code = http_status_code.OK)
	response.json.return_value = expected
	mocked_requests.post.return_value = response

	client = PlaylistClient('token')
	result = client.create('playlist_name')

	assert result == expected
	mocked_requests.post.assert_called_once_with(
		client.get_url('/playlists'), 
		headers = client.header,
		json = {
			'snippet': {
				'title': 'playlist_name',
				'description': 'Playlist created with spotify-playlist-on-youtube'
			}
		}
	)

def test_create_playlist_raises_exception_correctly():
	client = PlaylistClient('token')
	with pytest.raises(YouTubeAPIUnsuccessfulRequestException):
		client.create('playlist_name')


@patch('src.youtube.clients.requests')
def test_add_video_in_playlist_successfully(mocked_requests):
	expected = {'Playlist': {'Die Antwoord': 'Banana brains, you\'re the apple of my eye'}}
	response = Mock(status_code = http_status_code.OK)
	response.json.return_value = expected
	mocked_requests.post.return_value = response

	client = PlaylistClient('token')
	result = client.add_video('playlist_id', 'video_id')

	assert result == expected
	mocked_requests.post.assert_called_once_with(
		client.get_url('/playlistItems'), 
		headers = client.header,
		json = {
			'snippet': {
				'playlistId': 'playlist_id',
				'resourceId': {
					'videoId': 'video_id'
				}
			}
		}
	)

def test_add_video_in_playlist_raises_exception_correctly():
	client = PlaylistClient('token')
	with pytest.raises(YouTubeAPIUnsuccessfulRequestException):
		client.add_video('playlist_id', 'video_id')