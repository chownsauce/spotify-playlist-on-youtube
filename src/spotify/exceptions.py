class SpotifyAPIUnsuccessfulRequestException(Exception):
	'''
		Exception to be raised when Spotify API response is unsuccessful
	'''

	def __init__(self, message):
		self.message = message
