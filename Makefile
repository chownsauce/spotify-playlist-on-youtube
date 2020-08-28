include config.env

$(eval export $(shell sed 's/=.*//' config.env))


all: 
	echo $$SPOTIFY_PLAYLIST_ID
