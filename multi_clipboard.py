#!/usr/bin/python

import pyperclip, sys, json

try:
    with open('clipboard_dict.json') as f:
        text_outputs = json.load(f)
except FileNotFoundError:
    print('Dictionary file not found, creating new...')
    clipboard_dict = {'1': '','2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':'','0':''}
    with open('clipboard_dict.json', 'w') as f:
        json.dump(clipboard_dict, f)
    with open('clipboard_dict.json') as f:
        text_outputs = json.load(f)

def add_new(position, dictionary, value=pyperclip.paste()) -> None:
##    concat_list = ['"""', value, '"""']
##    new_value = ''.join(concat_list)
    new_value = value
    dictionary[position] = new_value
    with open('clipboard_dict.json', 'w') as f:
        json.dump(dictionary, f)

if len(sys.argv) < 2:
    print('Please include arguments')
    sys.exit()

if sys.argv[1] == '-a':
    try:
        add_new(sys.argv[2], text_outputs, sys.argv[3])
    except IndexError as e:
        add_new(sys.argv[2], text_outputs)
elif sys.argv[1] != '-a':
    try:
        pyperclip.copy(f'{text_outputs[sys.argv[1]]}')
    except KeyError as e:
        print(f'Index "{sys.argv[1]}" is invalid, please provide a valid index.\n Exiting...')
        sys.exit()

