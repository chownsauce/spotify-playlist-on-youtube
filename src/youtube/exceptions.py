class YouTubeAPIUnsuccessfulRequestException(Exception):
	'''
		Exception to be raised when Youtube API response is unsuccessful
	'''

	def __init__(self, message):
		self.message = message
