from src.app.config import Config
from src.spotify.services import get_playlist
from src.youtube.services import create_playlist

def run():
	print('Importando músicas do Spotify:')
	playlist = get_playlist(
		Config.SPOTIFY_CLIENT_ID, Config.SPOTIFY_CLIENT_SECRET, Config.SPOTIFY_PLAYLIST_ID)

	print(f'{len(playlist.tracks)} músicas importadas!')
	search_query = [f'{item.artists[0].name} {item.name}' for item in playlist.tracks]

	print('Criando playlist no arrombado do YouTube...')
	print('.')
	print('.')
	print('.')
	print('....')
	print('Se a autenticação de dois fatores está ativada, não esqueça de confirmar o login.')
	print('Agora vai!')

	create_playlist(Config.YOUTUBE_EMAIL, Config.YOUTUBE_PASSWORD, playlist.name, search_query)

	print('Aee carai! Pode fritar agora sua doida!')
	