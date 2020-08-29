from collections import namedtuple


Playlist = namedtuple('Playlist', ['name', 'tracks'])
Artist = namedtuple('Artist', ['name'])
Track = namedtuple('Track', ['name', 'artists'])


class ArtistFactory:
	
	@classmethod
	def create(cls, data):
		return Artist(data['name'])


class TrackFactory:
	
	@classmethod
	def create(cls, data):
		artists = [ArtistFactory.create(item) for item in data['artists']]
		return Track(data['name'], artists)