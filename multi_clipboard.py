#!/usr/bin/python

import pyperclip, sys, json, os
import pyautogui    ## Optional for automatic pasting.

## File name for our dictionary; it should be stored in the user's home folder.
filename = f'{os.path.expanduser("~")}/clipboard_dict.json'

## Load in the dictionary, or create the file and data if it isn't found.
try:
    with open(filename) as f:
        clipboard_dict = json.load(f)
except FileNotFoundError:
    print('Dictionary file not found, creating a new file and dictionary...')
    new_dict = {'1': '','2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':'','0':''}
    with open(filename, 'w') as f:
        json.dump(new_dict, f, indent=4)
    with open(filename) as f:
        clipboard_dict = json.load(f)

def change_value(position, dictionary, value=pyperclip.paste()) -> None:
    """ Changes the value at a given key in the dictionary. Defaults to using the current clipboard contents. """
##    dictionary[position] = value.strip()      ## Not sure if I want to strip whitespace tbh.
    dictionary[position] = value
    with open(filename, 'w') as f:
        json.dump(dictionary, f, indent=4)

def copy_selected() -> None:
    """
Attempt at having the program copy selected text to clipboard when the program runs.
I think there is an issue being caused by the ctrl+c running on Linux killing the program.
keyUp() is used to free up the keys when this is used as a shortcut.
    """
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('win')
    pyautogui.keyUp('shift')
    pyautogui.keyUp(sys.argv[1])
    pyautogui.hotkey('ctrl','c')

def paste_output() -> None:
    """ Function to paste the clipboard contents. keyUp() is used to free up the keys when this is used as a shortcut. """
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('win')
    pyautogui.keyUp(sys.argv[1])
    pyautogui.hotkey('ctrl','v')

## Usage warning in case arguments are not provided.
if len(sys.argv) < 2:
    print(
        """
Please include arguments.
To copy from the dictionary: $ multi_clipboard.py <position (0-9)>
To add a new entry to the dictionary: $ multi_clipboard.py <position (0-9)> -a <value (optional)>
   Note: if value is not included, the script will take the contents of the clipboard.
        """
    )
    sys.exit()

## Sort through the arguments and copy text into the dictionary at the given key.
if sys.argv[1] == '-a':
    if len(sys.argv) < 3:
        print('Please add the position to add the value to (0-9).\nExiting...')
        sys.exit()
    try:
        ## If a value is included as an argument, use it.
        change_value(sys.argv[2], clipboard_dict, sys.argv[3])
    except IndexError as e:
        ## If no value is included, default to using the current clipboard contents.
##        copy_selected()
        change_value(sys.argv[2], clipboard_dict)
        
## If the only argument is a key, grab the value and paste it.
elif sys.argv[1] != '-a':
    try:
        pyperclip.copy(f'{clipboard_dict[sys.argv[1]]}')
        paste_output()
    except KeyError as e:
        print(f'Index "{sys.argv[1]}" is invalid, please provide a valid index.\n Exiting...')
        sys.exit()

