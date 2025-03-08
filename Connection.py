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

def activateSpotifyPlayer():
    import pyautogui
    import pygetwindow as gw

    # pip install pyautogui
    # pip install pygetwindow
    # assist in development????

    # retrieve spotify window by title, activate, then press space
    window = gw.getWindowsWithTitle("Spotify Premium")
    try:
        win = window[0]
        win.activate() 
        pyautogui.press("space")
    except:
        print("Window not found!")

    time.sleep(1.5)


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

spotifyDevices = sp.devices()['devices']

# attempt to open spotify programmatically on local machine if no devices are available
if len(spotifyDevices) == 0:
    print('No Devices With Spotify Open! Attempting to open it for you.')

    # application solution. confirmed solution on windows machines.
    try:
        os.system("spotify")
        startupGracePeriod = 6 
    except:
        # web solution if windows application fails
        webbrowser.open("https://open.spotify.com/")
        startupGracePeriod = 15

    # give time to run based on application time
    time.sleep(startupGracePeriod)
    
# error handling for no active spotify devices
if len(spotifyDevices) > 0:
 
    # sometimes it thinks something is playing when nothing is???
    # ah shit it can sense my smartwatch, can't believe tech these days
    #['is_active': False, 
    # 'is_private_session': False, 
    # 'is_restricted': False, 
    # 'name': 'SM-R940', 
    # 'supports_volume': False, 
    # 'type': 'Smartwatch', 
    # 'volume_percent': 100}]
    print(spotifyDevices)

    # learn how to set a device to be active
    # play on startup
    # app or web better?
    # need of an external server potentially
    
    # can we falsify a play/pause key press
    # hmmmmmmmmmmm
    # sounds neato. note- yup its neato
    

    # as long as one device is active then we can run playback
    anyDevicesActive = any(i['is_active'] for i in spotifyDevices)
    
    if not anyDevicesActive:
        print('No Active Devices Running Spotify! Attempting to activate it for you.')
           
        activateSpotifyPlayer()
        
        # give program time before attempting searches
        time.sleep(0.5)

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
try:
    sp.volume(volume_percent, device_id)
except:
    activateSpotifyPlayer()
    sp.volume(volume_percent, device_id)

# starting playback based on searched field
print('Starting Playback..')
sp.start_playback(device_id, context_uri, uris=None, offset=None, position_ms=None)

print('Shuffling Music..')
sp.shuffle(True, device_id)

print("Process Completed.")
