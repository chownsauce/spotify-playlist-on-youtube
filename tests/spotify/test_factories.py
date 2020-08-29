from src.spotify.factories import PlaylistFactory

def test_parse_playlist_correctly():
	data = {
		'name': 'frita que passa',
		'tracks': {
			'items': [{
				'track': {
					'artists': [{
						'name': 'Lady Gaga',
					}],
					'name': 'Poker Face',
				},
			}]
		}
	}

	playlist = PlaylistFactory.create(data)

	assert len(playlist.tracks) == 1
	assert playlist.name == 'frita que passa'

	assert len(playlist.tracks[0].artists) == 1
	assert playlist.tracks[0].name == 'Poker Face'

	assert playlist.tracks[0].artists[0].name == 'Lady Gaga'
