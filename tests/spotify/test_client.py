import pytest

from requests.status_codes import codes as http_status_code
from unittest.mock import patch, Mock

from src.spotify.client import PlaylistClient
from src.spotify.exceptions import SpotifyAPIUnsuccessfulRequestException


def test_playlist_client_has_correct_setup():
	client = PlaylistClient()

	assert client.url == 'https://api.spotify.com/v1/playlists'


@patch('src.spotify.client.requests')
def test_get_playlist_successfully(mocked_requests):
	expected = {'Y.A.L.A': 'Yeah we come come come we come with someone'}
	response = Mock(status_code = http_status_code.OK)
	response.json.return_value = expected
	mocked_requests.get.return_value = response

	client = PlaylistClient()
	result = client.get('id')

	assert result == expected

@patch('src.spotify.client.requests')
def test_get_playlist_raises_exception_correctly(mocked_requests):
	response = Mock(status_code = http_status_code.SERVER_ERROR)

	client = PlaylistClient()
	with pytest.raises(SpotifyAPIUnsuccessfulRequestException):
		client.get('id')
