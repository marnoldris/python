#!/usr/bin/python

import pyperclip, sys, json, os
import pyautogui

filename = f'{os.path.expanduser("~")}/clipboard_dict.json'

try:
    with open(filename) as f:
        text_outputs = json.load(f)
except FileNotFoundError:
    print('Dictionary file not found, creating new...')
    clipboard_dict = {'1': '','2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':'','0':''}
    with open(filename, 'w') as f:
        output = json.dumps(clipboard_dict, indent=4)
        f.write(output)
    with open(filename) as f:
        text_outputs = json.load(f)

def add_new(position, dictionary, value=pyperclip.paste()) -> None:
##    dictionary[position] = value.strip()
    dictionary[position] = value
    with open(filename, 'w') as f:
        output = json.dumps(dictionary, indent=4)
        f.write(output)

def copy_selected() -> None:
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('win')
    pyautogui.keyUp('shift')
    pyautogui.keyUp(sys.argv[1])
    pyautogui.hotkey('ctrl','c')

def paste_output() -> None:
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('win')
    pyautogui.keyUp(sys.argv[1])
    pyautogui.hotkey('ctrl','v')

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

if sys.argv[1] == '-a':
    if len(sys.argv) < 3:
        print('Please add the position to add the value to (0-9).\nExiting...')
        sys.exit()
    try:
        add_new(sys.argv[2], text_outputs, sys.argv[3])
    except IndexError as e:
##        copy_selected()
        add_new(sys.argv[2], text_outputs)
elif sys.argv[1] != '-a':
    try:
        pyperclip.copy(f'{text_outputs[sys.argv[1]]}')
        paste_output()
    except KeyError as e:
        print(f'Index "{sys.argv[1]}" is invalid, please provide a valid index.\n Exiting...')
        sys.exit()

