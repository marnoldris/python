#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 11:34:57 2023

@author: matthew
"""

from pyfiglet import Figlet
from time import sleep
import sys
import os
import random
import cursor
import getpass

home_dir = os.path.expanduser('~')
called_upon = []

yes_vals = ('y', 'yes')
repeat_q = input('Would you like to allow repeats? (y/N)\n> ').lower().strip()
rep = True if repeat_q in yes_vals else False

if len(sys.argv) <= 1:
    print('Invalid arguments, please include a file name for the generator.')
    sys.exit()
if os.path.exists(sys.argv[1]):
    with open(sys.argv[1]) as file:
        raw_lines = file.readlines()
        name_lines = [line for line in raw_lines if line.strip()]
else:
    print('File not found, exiting...')
    sys.exit()

# %% Parse input file
names = []

"""
print('Are the names in <Last name>, <First name> format? (y/N)')
try:
    format_q = input('> ').lower()
except KeyboardInterrupt:
    print('Exiting...')
    sys.exit()
"""

# if format_q in ('y', 'yes'):
if ',' in name_lines[0]:
    for line in name_lines:
        first_name = line.split(',')[1].strip()
        last_name = line.split(',')[0].strip()
        names.append(f'{first_name} {last_name}')
else:
    for line in name_lines:
        names.append(line.strip())

random.shuffle(names)


def print_students(delay) -> None:
    for name in names:
        print('Finding a random selection.')
        print(f.renderText(name.title().center(columns)))
        sleep(delay)
        os.system('cls' if os.name == 'nt' else 'clear')

columns = os.get_terminal_size().columns
# f = Figlet(font='slant')
f = Figlet(justify='center')
f.width = columns

while True:
    try:
        cursor.hide()
        #random_student = random.randint(0, len(names)-1)
        random_student = random.choice(names)

        while random_student in called_upon:
            #random_student = random.randint(0, len(names)-1)
            random_student = random.choice(names)

        called_upon.append(random_student)
        
        if (len(called_upon) > (len(names) // 3)) and rep == True:
            del called_upon[0]

        print_students(0.01)
        print_students(0.1)
        print_students(0.15)

        sleep(0.3)
        # print(f.renderText(f'*=* {names[random_student].title()} *=*'.center(columns)))
        #print(f.renderText(f'{names[random_student].title()}'))
        print(f.renderText(f'{random_student.title()}'))

        repeat = getpass.getpass('Press return to run the program again.\n'
                       'CTRL+C to quit.'
                       )
        if repeat == '':
            continue
        else:
            cursor.show()
            break

    except KeyboardInterrupt:
        print('\nExiting...')
        cursor.show()
        sys.exit()
