import os



def test_load_config_correctly():
	expected = "PLAYLIST_ID"
	os.environ['SPOTIFY_PLAYLIST_ID'] = expected


	from src.app.config import Config
	assert Config.SPOTIFY_PLAYLIST_ID == expected

	