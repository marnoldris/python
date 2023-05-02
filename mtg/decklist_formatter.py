#!/usr/bin/python

import shutil
import pyperclip
import sys

def print_columns(string_list, width=shutil.get_terminal_size().columns):
    max_length = len(max(string_list, key=len)) + 4
    num_columns = width // (max_length)
    for i in range(0, len(string_list), num_columns):
        for s in string_list[i:i+num_columns]:
            print('{:<{}}'.format(s, max_length), end='')
        print()

def copy_columns(string_list, width=shutil.get_terminal_size().columns):
    max_length = len(max(string_list, key=len)) + 4
    num_columns = width // (max_length)
    formatted_strings = []

    for i in range(0, len(string_list), num_columns):
        formatted_row = ['{:<{}}'.format(s, max_length) for s in string_list[i:i+num_columns]]
        formatted_strings.append(''.join(formatted_row))

    output = '\n'.join(formatted_strings)

    print(output, end='\n\n')
    pyperclip.copy(output)
    print(f'{len(string_list)} card names copied to clipboard...')
    

decklist = []

with open(sys.argv[1]) as f:
    for line in f.readlines():
        decklist.append(line.strip())

if len(sys.argv) == 3:
    try:
        copy_columns(decklist, int(sys.argv[2]))
    except TypeError:
        print('Invalid entry for total width, defaulting to console width...')
        copy_columns(decklist)
else:
    print(
        'Desired width not included, defaulting to console width...',
        end='\n\n'
    )
    copy_columns(decklist)
