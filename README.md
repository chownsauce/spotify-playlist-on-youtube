# Spotify Playlist on Youtube

## Requirements
- Python 3+ (I've used 3.8)
- [Chrome Webdriver] (https://chromedriver.chromium.org/)
- Create a [Spotify Client API](https://developer.spotify.com/documentation/general/guides/app-settings/)
- Use an YouTube account with 2 factor auth

## Install
First, install the script requirements:
'''
pip install -r requirements/dev.txt
'''

So, create a _env_ file like the sample.env. The _env_ file must be have all variables from sample.env.
Create a env file like the sample.env
'''
mv sample.env env
'''
Fill the variables with your data.

## Run
'''
make
'''
