from unittest.mock import patch, Mock

from src.youtube.services import search_video


@patch('src.youtube.services.VideoFactory')
@patch('src.youtube.services.Api')
def test_search_video_correctly(mocked_api, mocked_factory):
	expected = Mock()
	data = {'Eva Simons': 'Silly Boy'}
	mocked_api().search_by_keywords.return_value = data
	mocked_factory.create.return_value = expected

	video = search_video('api', 'keyword')

	assert video == expected
	mocked_api.assert_called_with(api_key='api')
	mocked_api().search_by_keywords.assert_called_with(
		q='keyword', limit=1, search_type='video'
	)
	mocked_factory.create.assert_called_once_with(data)
