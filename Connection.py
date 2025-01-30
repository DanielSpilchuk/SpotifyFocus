import spotipy
from spotipy.oauth2 import SpotifyOAuth
from Credentials import *

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope="user-library-read"))

# base information to be changed in the future
device_id = 90
volume_percent = 20

# Basic Features/Goals
# Get User Inputs for Key and Playlist
# Play Playlist on Key Press (unless already playing?)

# METHODS
# search # searches for an item playlist(playlist_id, fields=None, market=None, additional_types=('track',))
#playlist(playlist_id, fields=None, market=None, additional_types=('track',)) get playlist by id
#print(sp.currently_playing()) # users currently playing track
#print(sp.current_playback()) # get information about current users currently playing track
# user_playlist(user, playlist_id=None, fields=None, market=None)

sp.volume(volume_percent, device_id)
sp.start_playback(device_id, context_uri=None, uris=None, offset=None, position_ms=None)
sp.shuffle(True, device_id)

#https://open.spotify.com/playlist/3qu09J0oigKWBhPWoRJsjs?si=NMX6BIKeQ5Ob1GhQVaawfQ

# generic code for  
results = sp.current_user_saved_tracks() # liked songs
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " - ", track['name'])