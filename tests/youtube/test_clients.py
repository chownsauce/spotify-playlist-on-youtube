import pytest

from requests.status_codes import codes as http_status_code
from unittest.mock import patch, Mock

from src.youtube.clients import PlaylistClient
from src.youtube.exceptions import YouTubeAPIUnsuccessfulRequestException


def test_playlist_client_has_correct_setup():
	client = PlaylistClient()

	assert client.url == 'https://www.googleapis.com/youtube/v3/playlists?part=snippet&alt=json'


@patch('src.youtube.clients.requests')
def test_create_playlist_successfully(mocked_requests):
	expected = {'Playlist': {'Madonna': 'I\'m gonna break the cycle'}}
	response = Mock(status_code = http_status_code.OK)
	response.json.return_value = expected
	mocked_requests.post.return_value = response

	client = PlaylistClient()
	result = client.post('playlist_name', 'token')

	assert result == expected
	mocked_requests.post.assert_called_once_with(
		client.url, 
		headers = {'Authorization': 'Bearer token'},
		json = {
			'snippet': {
				'title': 'playlist_name'
			}
		}
	)

def test_get_playlist_raises_exception_correctly():
	client = PlaylistClient()
	with pytest.raises(YouTubeAPIUnsuccessfulRequestException):
		client.post('playlist_name', 'token')