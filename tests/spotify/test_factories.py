from src.spotify.factories import TrackFactory

def test_parse_playlist_correctly():
	data = {'artists': [{
			'name': 'Lady Gaga',
		}],
		'name': 'Poker Face',
	}

	playlist = TrackFactory.create(data)

	assert len(playlist.artists) == 1
	assert playlist.name == 'Poker Face'

	assert playlist.artists[0].name == 'Lady Gaga'
