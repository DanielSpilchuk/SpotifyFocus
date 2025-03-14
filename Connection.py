import os
import sys
import pygetwindow as gw # used for autoplay and ensuring program paused
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
    # pip install pyautogui
    # pip install pygetwindow
    # assist in development????
    import pyautogui

    # retrieve spotify window by title, activate, then press space
    window = gw.getWindowsWithTitle("Spotify Premium") 
    try:
        window[0].activate() 
        pyautogui.press("space")
    except:
        print("Window not found!")



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

    # application solution. confirmed solution on windows machines.
    try:
        os.system("spotify")

    # web solution if windows application fails
    except:
        webbrowser.open("https://open.spotify.com/")

    # pausing program until program opened
    while not len(sp.devices()['devices']) > 0:
        time.sleep(0.25)    
    
# error handling for no active spotify devices
if len(sp.devices()['devices']) > 0:

    # device variables to potentially sort by. THIS MEANS YOU CAN USE THIS TO CHANGE PHONE/SMARTWATCH PLAYBACK
    # 'is_active': True, 
    # 'is_private_session': False, 
    # 'is_restricted': False, 
    # 'name': 'DeviceName', 
    # 'supports_volume': True, 
    # 'type': 'Computer', 
    # 'volume_percent': 100  # spotify's percentage, not device percentage

    # as long as one device is active then we can run playback
    anyDevicesActive = any(i['is_active'] and i['type'] == 'Computer' for i in sp.devices()['devices'])

    # if devices aren't active then activate the opened player   
    if not anyDevicesActive:
        print('No Active Devices Running Spotify! Attempting to activate it for you.')
        activateSpotifyPlayer()

    # wait until activation is available on the system side
    while not any(i['is_active'] for i in sp.devices()['devices']):
        time.sleep(0.25)

# base information to be changed in the future
device_id = None
volume_percent = 100
search_string = 'Cowboy Saloon Music'
search_type = 'album'

#search_return = sp.search(sys.argv[0], limit=1, type='playlist') # playlist for the user to search for
search_return = sp.search(search_string, limit=1, type=search_type)

#print("Argument sys: " + sys.argv[0]) # figure out how to make this smoother
#print(search_return)

if search_return[search_type+'s']['items'][0] == None:
    print('Requested playlist yielded no results.')
    sys.exit()


# volume modification
print('Changing Volume..')
#try:

# TODO: block on user preference smartphone connectivity
# don't change volume if device blocks functionality
if sp.devices()['devices'][0]['supports_volume']:
    sp.volume(volume_percent, device_id)

# starting playback based on searched field
print('Starting Playback..')
context_uri = search_return[search_type+'s']['items'][0]['uri']
sp.start_playback(device_id, context_uri, uris=None, offset=None, position_ms=None)

# turn shuffle on
print('Shuffling Music..')
sp.shuffle(True, device_id)

# completion message
print("Process Completed.")
