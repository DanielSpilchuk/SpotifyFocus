import spotipy
import json
from spotipy.oauth2 import SpotifyOAuth
from Credentials import *

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope="user-read-playback-state,user-modify-playback-state"))

#https://api.spotify.com/v1/me/player/devices get request to find all

# base information to be changed in the future
device_id = None
volume_percent = 80


#context_uri="spotify:playlist:3qu09J0oigKWBhPWoRJsjs"
search_return = sp.search("peeing in a pool while it rains", limit=1, type='playlist')
json_parse = json.loads(search_return)
context_uri = json_parse['playlists']['items']['uri']

# search # searches for an item playlist(playlist_id, fields=None, market=None, additional_types=('track',))

print('INTRO')
print(sp.devices()) # how to do this more specifically
print(context_uri)

# Basic Features/Goals
# Get User Inputs for Key and Playlist
# Play Playlist on Key Press (unless already playing?)

# METHODS
#print(sp.currently_playing()) # users currently playing track
#print(sp.current_playback()) # get information about current users currently playing track

print('Changing Volume..')
sp.volume(volume_percent, device_id)

print('Starting Playback..')
sp.start_playback(device_id, context_uri, uris=None, offset=None, position_ms=None)

print('Shuffling Music..')
sp.shuffle(True, device_id)

print("Process Completed.")
