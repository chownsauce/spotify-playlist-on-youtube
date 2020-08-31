from src.spotify.factories import PlaylistFactory, Track, TrackFactory

def test_parse_track_correctly():
	data = {'artists': [{
			'name': 'Lady Gaga',
		}],
		'name': 'Poker Face',
	}

	video = TrackFactory.create(data)

	assert len(video.artists) == 1
	assert video.name == 'Poker Face'

	assert video.artists[0].name == 'Lady Gaga'


def test_parse_playlist_correctly():
	tracks = [
		Track('Sorry For Party Rocking', ['LMFAO']),
		Track('Love Profusion', ['Madonna'])
	]
	data = {
		'name': 'Playlist Name'
	}

	playlist = PlaylistFactory.create(data, tracks)

	assert playlist.tracks == tracks
	assert playlist.name == 'Playlist Name'
