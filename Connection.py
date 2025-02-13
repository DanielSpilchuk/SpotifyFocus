import sys
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

# New rough authorization?? Different language snippet
#authUrl = new URL("https://accounts.spotify.com/authorize")
# generated in the previous step
#window.localStorage.setItem('code_verifier', codeVerifier);

#params =  {
#  response_type: 'code',
#  client_id: clientId,
#  scope,
#  code_challenge_method: 'S256',
#  code_challenge: codeChallenge,
#  redirect_uri: redirectUri
#}
#authUrl.search = new URLSearchParams(params).toString();
#window.location.href = authUrl.toString();

load_dotenv()
SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")

print(SPOTIPY_CLIENT_ID)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope="user-read-playback-state,user-modify-playback-state"))

#https://api.spotify.com/v1/me/player/devices get request to find all

# THIS SECTION IS TO BE ADDED TO. functionality options- open spotify programmatically?
# error handling for no open spotify
if len(sp.devices()['devices']) == 0:
    print('No Devices With Spotify Open! Please start the app and try again.')
    sys.exit()

# error handling for no active spotify devices
elif len(sp.devices()['devices']) > 0:
    for i in sp.devices()['devices']:
        if not i['is_active']:
            print('No Active Devices Running Spotify! Please listen to music and try again.')
            sys.exit()

# base information to be changed in the future
device_id = None
volume_percent = 100
search_return = sp.search(sys.argv[0], limit=1, type='playlist') # playlist for the user to search for

print(sys.argv[0]) # figure out how to make this smoother

if search_return['playlists']['items'][0] == None:
    print('Requested playlist yielded no results.')
    sys.exit()

context_uri = search_return['playlists']['items'][0]['uri']

print('Changing Volume..')
sp.volume(volume_percent, device_id)

print('Starting Playback..')
sp.start_playback(device_id, context_uri, uris=None, offset=None, position_ms=None)

print('Shuffling Music..')
sp.shuffle(True, device_id)

print("Process Completed.")
