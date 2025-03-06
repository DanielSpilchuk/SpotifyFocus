import os
import sys
import subprocess
import spotipy    
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

# if web solution used -------------------------------
import webbrowser
import time
# ----------------------------------------------------

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

# find the issue of user key storage, how to request and recieve
load_dotenv()
SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope="user-read-playback-state,user-modify-playback-state"))

#https://api.spotify.com/v1/me/player/devices get request to find all

# attempt to open spotify programmatically on local machine if no devices are available
if len(sp.devices()['devices']) == 0:
    print('No Devices With Spotify Open! Attempting to open it for you.')

    # application solution (semi-finished currently)
    # i personally cannot believe that this works
    # error handle if not successful
    try:
        os.system("spotify")
        startupGracePeriod = 5
    except:
        # web solution (fixes this step of the process)
        webbrowser.open("https://open.spotify.com/")
        startupGracePeriod = 15

    # give time to run
    time.sleep(startupGracePeriod)
    
# error handling for no active spotify devices
if len(sp.devices()['devices']) > 0:

    # learn how to set a device to be active
    # play on startup
    # app or web better?
    # need of an external server potentially
    
    #anyDevicesActive = False
    #for i in sp.devices()['devices']:        
    #    if i['is_active']:
    #        anyDevicesActive = True
    

    # can we falsify a play/pause key press
    # hmmmmmmmmmmm
    # sounds neato 

    # as long as one device is active then we can run playback
    anyDevicesActive = any(i['is_active'] for i in sp.devices()['devices'])
    
    if not anyDevicesActive:
        print('No Active Devices Running Spotify! Please listen to music and try again.')
        sys.exit()

# base information to be changed in the future
device_id = None
volume_percent = 100
#search_return = sp.search(sys.argv[0], limit=1, type='playlist') # playlist for the user to search for
search_return = sp.search('generic search', limit=1, type='playlist')

#print("Argument sys: " + sys.argv[0]) # figure out how to make this smoother
#print(search_return)

if search_return['playlists']['items'][0] == None:
    print('Requested playlist yielded no results.')
    sys.exit()

context_uri = search_return['playlists']['items'][0]['uri']

# volume modification
print('Changing Volume..')
sp.volume(volume_percent, device_id)

# starting playback based on searched field
print('Starting Playback..')
sp.start_playback(device_id, context_uri, uris=None, offset=None, position_ms=None)

print('Shuffling Music..')
sp.shuffle(True, device_id)

print("Process Completed.")
