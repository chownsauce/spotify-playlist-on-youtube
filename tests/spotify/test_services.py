from unittest.mock import call, patch

from src.spotify.services import get_playlist


@patch('src.spotify.services.PlaylistFactory')
@patch('src.spotify.services.TrackFactory')
@patch('src.spotify.services.PlaylistClient')
@patch('src.spotify.services.TokenClient')
def test_get_playlist_successfully(mocked_token_client, mocked_playlist_client, mocked_track_factory, mocked_playlist_factory):
	expected = {
		'name': 'Playlist',
		'items': [{'Liquorice': 'Tell me if you like your lady in my-my color. Can I be your type? yeah'}]
	}
	token_response = {'access_token': 'token'}
	playlist_response = {
		'tracks': {
			'items': [{'track': 'list'}], 
			'next': None
		}
	}

	mocked_token_client().post.return_value = token_response
	mocked_playlist_client().get.return_value = playlist_response
	mocked_track_factory.create.return_value = expected['items'][0]
	mocked_playlist_factory.create.return_value = expected

	playlist = get_playlist('id', 'secret', 'playlist')

	assert playlist == expected
	mocked_token_client.assert_called_with('id', 'secret')
	mocked_playlist_client().get.assert_called_once_with('playlist', 'token')
	mocked_track_factory.create.assert_called_once_with(playlist_response['tracks']['items'][0]['track'])
	mocked_playlist_factory.create.assert_called_once_with(playlist_response, expected['items'])


@patch('src.spotify.services.PlaylistFactory')
@patch('src.spotify.services.TrackFactory')
@patch('src.spotify.services.PlaylistClient')
@patch('src.spotify.services.TokenClient')
def test_get_playlist_with_next_page_successfully(mocked_token_client, mocked_playlist_client, mocked_track_factory, mocked_playlist_factory):
	expected_tracks = [
		{'Liquorice': 'Tell me if you like your lady in my-my color. Can I be your type? yeah'},
		{'Hello Bitches': '뛰자뛰자 방방방 디스코 팡팡팡 hello Bitcheeeees'}
	]
	expected = {
		'name': 'Playlist',
		'items': list(expected_tracks)
	}
	token_response = {'access_token': 'token'}
	playlist_response = [{
		'tracks': {
			'items': [{'track': 'list'}], 
			'next': 'next_page'
		},
	}, {
		'items': [{'track': 'list'}],
		'next': None
	}]

	mocked_token_client().post.return_value = token_response
	mocked_playlist_client().get.return_value = playlist_response[0]
	mocked_playlist_client().next.return_value = playlist_response[1]
	mocked_track_factory.create.side_effect = expected_tracks
	mocked_playlist_factory.create.return_value = expected

	playlist = get_playlist('id', 'secret', 'playlist')

	assert playlist == expected
	mocked_token_client.assert_called_with('id', 'secret')
	mocked_playlist_client().get.assert_called_once_with('playlist', 'token')
	mocked_track_factory.create.assert_has_calls([
		call(playlist_response[0]['tracks']['items'][0]['track']), 
		call(playlist_response[1]['items'][0]['track'])
	])
	mocked_playlist_factory.create.assert_called_once_with(playlist_response[0], expected_tracks)
