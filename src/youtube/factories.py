from collections import namedtuple

Video = namedtuple('Video', ['id', 'name'])


class VideoFactory:

	@classmethod
	def create(cls, data):
		return Video(
			data['id']['videoId'], 
			data['snippet']['title']
		)