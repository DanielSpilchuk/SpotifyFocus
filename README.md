# SpotifyFocus

THIS IS TO BE CHANGED DURING DEVELOPMENT

You can configure your system or your code editor to run a Python program when you press F7. Here’s how to do it depending on your setup:

Using Windows Batch Files
    Create a batch file (run_python.bat):

'
@echo off
python "C:\path\to\your_script.py"
'

Step 1: Create a Batch File
    Open Notepad (or any text editor).

    Paste the following code (replace "C:\path\to\your_script.py" with the actual path of your Python file):

    @echo off
    python "C:\path\to\your_script.py"
    pause

        The pause command keeps the terminal open so you can see any output before it closes.

    Save the file as run_python.bat (make sure it’s saved as .bat and not .txt).



Use AutoHotkey to bind F7 to run the script:
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

Now, whenever you press F7, your Python script will run!

THIS NEEDS TO BE TESTED FURTHER TO SEE POTENTIAL TO EXPAND ON.