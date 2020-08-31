include env

$(eval export $(shell sed 's/=.*//' env))


all: 
	python -m src.start
