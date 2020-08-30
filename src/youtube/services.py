from pyyoutube import Api

from src.youtube.clients import PlaylistClient
from src.youtube.factories import VideoFactory


def search_video(api_key, search_keywords):
	api = Api(api_key=api_key)
	data = api.search_by_keywords(q=search_keywords, limit=1, search_type='video')
	return VideoFactory.create(data.to_dict()['items'])


def create_playlist(token, playlist_name, videos):
	client = PlaylistClient(token)
	playlist_id = client.create(playlist_name)['id']
	for item in videos:
		client.add_video(playlist_id, item.id)