from unittest.mock import patch

from src.spotify.services import get_playlist


@patch('src.spotify.services.PlaylistFactory')
@patch('src.spotify.services.PlaylistClient')
@patch('src.spotify.services.TokenClient')
def test_get_playlist_successfully(mocked_token_client, mocked_playlist_client, mocked_factory):
	expected = [{'Liquorice': 'Tell me if you like your lady in my-my color. Can I be your type? yeah'}]
	token_response = {'access_token': 'token'}
	playlist_response = {'play': 'list'}

	mocked_token_client().post.return_value = token_response
	mocked_playlist_client().get.return_value = playlist_response
	mocked_factory.create.return_value = expected

	playlist = get_playlist('id', 'secret', 'playlist')

	assert expected == playlist
	mocked_token_client.assert_called_with('id', 'secret')
	mocked_playlist_client().get.assert_called_once_with('playlist', 'token')
	mocked_factory.create.assert_called_once_with(playlist_response)
