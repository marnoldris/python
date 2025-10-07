#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  7 13:58:26 2025

@author: matthew
"""

import sys
import os
import random


# %% Read input file
home_dir = os.path.expanduser('~')

if len(sys.argv) <= 1:
    print('Invalid arguments, please include a file name for the generator.')
    sys.exit()
if os.path.exists(sys.argv[1]):
    with open(sys.argv[1]) as file:
        name_lines = file.readlines()
else:
    print('File not found, exiting...')
    sys.exit()


# %% Parse input file
names = []

print('Are the names in <Last name>, <First name> format? (y/N)')
try:
    format_q = input('> ').lower()
except KeyboardInterrupt:
    print('Exiting...')
    sys.exit()

if format_q in ('y', 'yes'):
    for line in name_lines:
        first_name = line.split(',')[1].strip()
        last_name = line.split(',')[0].strip()
        names.append(f'{first_name} {last_name}')
else:
    for line in name_lines:
        names.append(line.strip())

random.shuffle(names)


# %% Generate and print the pairs

pairs = []

while names:
    tmp = (names.pop(), names.pop())
    pairs.append(tmp)

output_list = []
for pair in pairs:
    output_list.append(pair[0].title() + ' and ' + pair[1].title())

output_string = '\n'.join(output_list)
print('\n\n' + output_string + '\n\n')

print('Would you like to save the list to a file? (y/N)')
try:
    save_file = input('> ').lower()
except KeyboardInterrupt:
    print('Exiting...')
    sys.exit()
if save_file in ('y', 'yes'):
    print('Enter a file name for the list.'
          ' Ex. student_pairs')
    try:
        file_name = input('> ') + '.txt'
    except KeyboardInterrupt:
        print('Exiting...')
        sys.exit()

    if os.path.exists(file_name):
        overwrite = input('File already exists, overwrite? (y/N)\n> ').lower()
        if overwrite in ('y', 'yes'):
            print(f'Overwriting list to {file_name}...')
            with open(file_name, 'w') as f:
                f.write(output_string)
        else:
            print('File not written, exiting...')
            sys.exit()
    else:
        print(f'Writing list to {file_name}...')
        with open(file_name, 'w') as f:
            f.write(output_string)
    print('Exiting...')
