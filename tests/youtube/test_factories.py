from src.youtube.factories import VideoFactory

def test_creates_video_correctly():
	data = {
		'id': {
			'videoId': 'XS088Opj9o0',
		},
		'snippet': {
			'title': 'Madonna - Frozen(Official Music Video)'
		}
	}

	video = VideoFactory.create(data)

	assert video.id == 'XS088Opj9o0'
	assert video.name == 'Madonna - Frozen(Official Music Video)'