from dotenv import load_dotenv          # environment variables
import os                               # cont.
import spotipy                          # general spotify functions
from spotipy.oauth2 import SpotifyOAuth # spotify authorization
import sys                              # opening spotify on windows machines
import webbrowser                       # for websolution backup
import pygetwindow as gw                # find spotify window
import pyautogui                        #  and click window to begin activation
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


# open spotify player if none are available
def openSpotifyPlayer():
    # application solution. confirmed solution on windows machines.
    try:
        os.system("spotify")

    # web solution if windows application fails
    except:
        webbrowser.open("https://open.spotify.com/")

    # pausing program until program opened
    while not len(sp.devices()['devices']) > 0:
        time.sleep(0.25)    


# retrieve spotify window by title, activate, then press space
def activateSpotifyPlayer():
    window = gw.getWindowsWithTitle("Spotify Premium") 
    while len(window) == 0:
        time.sleep(0.25)
        window = gw.getWindowsWithTitle("Spotify Premium") 

    try:
        window[0].activate() 
        pyautogui.press("space")
    except:
        print("Window still not found!")


# find the issue of user key storage, how to request and recieve
load_dotenv()
SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               scope="user-read-playback-state,user-modify-playback-state"))


# attempt to open spotify programmatically on local machine if no devices (computer only) are available
if not any(i['type'] == 'Computer' for i in sp.devices()['devices']):
    print('No Computers With Spotify Open! Attempting to open it for you.')
    openSpotifyPlayer()
    
# error handling for no active spotify devices
if len(sp.devices()['devices']) > 0:

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

# search type addition allows for different types
if search_return[search_type+'s']['items'][0] == None:
    print('Requested playlist yielded no results.')
    sys.exit()


# volume modification- don't change volume if device blocks functionality
if sp.devices()['devices'][0]['supports_volume']:
    print('Changing Volume..')
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
