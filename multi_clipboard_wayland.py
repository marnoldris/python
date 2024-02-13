#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 15:37:13 2024

@author: matthew
"""

#!/usr/bin/python

try:
    from datetime import datetime
    import sys
    import json
    import os
    import subprocess
except ImportError as e:
    print(str(e))
    with open(f'{os.path.expanduser("~")}/multi_clipboard.py.log', 'a') as f:
        f.write(f'\n{datetime.now()}: {str(e)}\n')
    sys.exit()

# File name for our dictionary; it should be stored in the user's home folder.
filename = f'{os.path.expanduser("~")}/clipboard_dict.json'

# Load in the dictionary, or create the file and data if it isn't found.
try:
    with open(filename) as f:
        clipboard_dict = json.load(f)
except FileNotFoundError:
    print('Dictionary file not found, creating a new file and dictionary...')
    new_dict = {
        '1': '', '2': '', '3': '',
        '4': '', '5': '', '6': '',
        '7': '', '8': '', '9': '',
        '0': '',
        }
    with open(filename, 'w') as f:
        json.dump(new_dict, f, indent=4)
    with open(filename) as f:
        clipboard_dict = json.load(f)

def change_value(position, dictionary, value) -> None:
    """
Changes the value at a given key in the dictionary.
Defaults to using the current clipboard contents.
    """
#    dictionary[position] = value.strip()      # Not sure if I want to strip
    dictionary[position] = value
    with open(filename, 'w') as f:
        json.dump(dictionary, f, indent=4)

def ydotool_command(command) -> None:
    cmd = command.split(' ')
    cmd.insert(0, 'ydotool')
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(e)
        with open(f'{os.path.expanduser("~")}/multi_clipboard.py.log', 'a') as f:
            f.write(f'\n{datetime.now()}:\n{e}\n')
        sys.exit()
        
def wl_copy(data) -> None:
    try:
        subprocess.run(['wl-copy', data], check=True)
    except subprocess.CalledProcessError as e:
        print(e)
        with open(f'{os.path.expanduser("~")}/multi_clipboard.py.log', 'a') as f:
            f.write(f'\n{datetime.now()}:\n{e}\n')
        sys.exit()

def wl_paste() -> str:
    try:
        result = subprocess.run(['wl-paste'], capture_output=True, text=True, check=True)
        return result.stdout.rstrip()
    except subprocess.CalledProcessError as e:
        print(e)
        with open(f'{os.path.expanduser("~")}/multi_clipboard.py.log', 'a') as f:
            f.write(f'\n{datetime.now()}:\n{e}\n')
        sys.exit()

def copy_selected() -> None:
    """
Copies the selected text to the clipboard when the program runs.
    """
    ydotool_command('key 29:0 125:0 42:0 29:1 110:1 110:0 29:0')

def paste_output() -> None:
    """
Function to paste the clipboard contents.
keyUp() is used to free up the keys when this is used as a shortcut.
    """
    ydotool_command('key 29:0 125:0 42:1 110:1 110:0 42:0')

# Usage warning in case arguments are not provided.
if len(sys.argv) < 2:
    usage_instructions = (
        'Please include arguments\n'
        'To copy from the dictionary: $ multi_clipboard.py <position (0-9)>\n'
        'To add a new entry to the dictionary: $ multi_clipboard.py -a '
        '<position (0-9)>\n <value (optional)>\n'
        '    Note: if value is not included, the script will copy the '
        'currently selected text.\n'
        )
    print(usage_instructions)
    with open(f'{os.path.expanduser("~")}/multi_clipboard.py.log', 'a') as f:
        f.write(f'\n{datetime.now()}: {usage_instructions}\n')
    sys.exit()

# Sort through the arguments and copy text into the dictionary at the given key
if sys.argv[1] == '-a':
    if len(sys.argv) < 3:
        print('Please add the position to add the value to (0-9).\nExiting...')
        sys.exit()
    if len(sys.argv) == 4:
        # If a value is included as an argument, use it.
        change_value(sys.argv[2], clipboard_dict, sys.argv[3])
    elif len(sys.argv) == 3:
        # If no value is included, default to using the current
        # clipboard contents.
        copy_selected()
        clipboard_contents = wl_paste()
        change_value(sys.argv[2], clipboard_dict, clipboard_contents)

# If the only argument is a key, grab the value and paste it.
elif sys.argv[1] != '-a':
    try:
        wl_copy(clipboard_dict[sys.argv[1]])
        paste_output()
    except KeyError:
        print(f'Index "{sys.argv[1]}" is invalid, please provide a valid '
              'index.\n Exiting...')
        sys.exit()
