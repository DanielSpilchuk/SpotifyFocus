import sys
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from Credentials import *

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope="user-read-playback-state,user-modify-playback-state"))

#https://api.spotify.com/v1/me/player/devices get request to find all

if len(sp.devices()) == 0:
    print('No Active Device Running Spotify! Please listen to music and try again.')
    exit

# base information to be changed in the future
device_id = None
volume_percent = 100
search_return = sp.search(sys.argv[0], limit=1, type='playlist') # playlist for the user to search for
context_uri = search_return['playlists']['items'][0]['uri']

print('Changing Volume..')
sp.volume(volume_percent, device_id)

print('Starting Playback..')
sp.start_playback(device_id, context_uri, uris=None, offset=None, position_ms=None)

print('Shuffling Music..')
sp.shuffle(True, device_id)

print("Process Completed.")
