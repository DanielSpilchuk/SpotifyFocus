# SpotifyFocus

Current State of Application - Development
User Level of Completion - Success on Local, Untested External Users
Active Development - Lock Spotify Until Loaded, Change Only on Hotkey Program Device


TODO

    Add documentation so they can get their own key. Make code pull key from config json file athat they can put in there.
    That way they are only modifying the config.

    Use server for access?

    Add dev mode on code and create mock API response. When activated my code will pull API data out of json.


THIS IS TO BE CHANGED DURING DEVELOPMENT


For Users
You can configure your system or your code editor to run a Python program when you press F7. Here’s how to do it depending on your setup:
    *can we avoid having users having to install python?


Using Windows Batch Files
    Create a batch file (run_python.bat):

'
@echo off
python "C:\path\to\your_script.py"
'

Step 1: Create a Batch File

    TODO: provide base template for a user to download

    Open Notepad (or any text editor).

    Paste the following code (replace "C:\path\to\your_script.py" with the actual path of your Python file):

    @echo off
    python "C:\path\to\your_script.py"
    pause

        The pause command keeps the terminal open so you can see any output before it closes.

    Save the file as run_python.bat (make sure it’s saved as .bat and not .txt).



Use AutoHotkey to bind F7 to run the script:

    TODO: provide base template

    Install AutoHotkey.
    Create a .ahk script:

        F7::Run, "C:\path\to\run_python.bat"
        Run the .ahk script.

OR

Option 2: Use Windows Keyboard Shortcuts

If you prefer not to use AutoHotkey:
    Create a shortcut to run_python.bat:
        Right-click the batch file > Create Shortcut.
    Assign a keyboard shortcut:
        Right-click the shortcut > Properties.
        In the Shortcut Key field, press F7.
        Click Apply and OK.

Now when you press F7, your Python script will run!



For Developers

The purpose of this project is to build a system that users can easily install, access, and operate that connects with Spotify.
Lowering the level of simplicity is a goal for this project. Making a robust program that users feel comfortable using is key
for users to interact with the software.
