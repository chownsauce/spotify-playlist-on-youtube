from pyyoutube import Api

from src.youtube.factories import VideoFactory


def search_video(api_key, search_keywords):
	api = Api(api_key=api_key)
	data = api.search_by_keywords(q=search_keywords, limit=1, search_type='video')
	
	return VideoFactory.create(data)


def create_playlist(token):
	pass


def add_video_in_playlist(playlist_id, video_id, token):
	pass