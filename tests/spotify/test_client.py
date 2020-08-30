import base64
import pytest

from requests.status_codes import codes as http_status_code
from unittest.mock import patch, Mock

from src.spotify.exceptions import SpotifyAPIUnsuccessfulRequestException
from src.spotify.clients.playlist import PlaylistClient
from src.spotify.clients.auth import TokenClient


def test_playlist_client_has_correct_setup():
	client = PlaylistClient()

	assert client.url == 'https://api.spotify.com/v1/playlists'


@patch('src.spotify.clients.playlist.requests')
def test_get_playlist_successfully(mocked_requests):
	expected = {'Y.A.L.A': 'Yeah we come come come we come with someone'}
	response = Mock(status_code = http_status_code.OK)
	response.json.return_value = expected
	mocked_requests.get.return_value = response

	client = PlaylistClient()
	result = client.get('id', 'token')

	assert result == expected
	mocked_requests.get.assert_called_once_with(
		f'{client.url}/id', headers={'Authorization': 'Bearer token'})

def test_get_playlist_raises_exception_correctly():
	client = PlaylistClient()
	with pytest.raises(SpotifyAPIUnsuccessfulRequestException):
		client.get('id', 'token')


def test_token_client_has_correct_setup():
	client = TokenClient('client', 'secret')
	expected_encoded_client = base64.b64encode('client:secret'.encode()).decode()

	assert client.client_id == 'client'
	assert client.client_secret == 'secret'
	assert client.url == 'https://accounts.spotify.com/api/token'
	assert client.encoded_client == expected_encoded_client
	assert client.header == {
		'Authorization': f'Basic {expected_encoded_client}',
		'Content-Type': 'application/x-www-form-urlencoded'
	}


@patch('src.spotify.clients.auth.requests')
def test_post_gets_token_successfully(mocked_requests):
	expected = {'Vogue': 'Grace Kelly; Harlow, Jean; Picture of a beauty queen'}
	response = Mock(status_code = http_status_code.OK)
	response.json.return_value = expected
	mocked_requests.post.return_value = response

	client = TokenClient('client', 'secret')
	result = client.post()

	assert result == expected
	mocked_requests.post.assert_called_once_with(
		client.url, data={'grant_type': 'client_credentials'}, headers=client.header)

@patch('src.spotify.clients.auth.requests')
def test_post_gets_token_raises_exception_correctly(mocked_requests):
	response = Mock(status_code = http_status_code.SERVER_ERROR)

	client = TokenClient('client', 'secret')
	with pytest.raises(SpotifyAPIUnsuccessfulRequestException):
		client.post()
