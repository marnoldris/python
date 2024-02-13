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

if len(sys.argv) <= 1:
    print('Invalid arguments, please include a file name for the generator.')
    sys.exit()
if os.path.exists(f'{home_dir}/Documents/student_lists/{sys.argv[1]}'):
    with open(f'{home_dir}/Documents/student_lists/{sys.argv[1]}') as file:
        name_lines = file.readlines()

names = []
for line in name_lines:
    first_name = line.split(',')[1].strip()
    names.append(first_name)

random.shuffle(names)


def print_students(delay) -> None:
    for name in names:
        print('Finding a random student.')
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
        random_student = random.randint(0, len(names)-1)

        while random_student in called_upon:
            random_student = random.randint(0, len(names)-1)

        called_upon.append(random_student)
        
        if len(called_upon) > (len(names) // 3):
            del called_upon[0]

        print_students(0.01)
        print_students(0.1)
        print_students(0.15)

        sleep(0.3)
        # print(f.renderText(f'*=* {names[random_student].title()} *=*'.center(columns)))
        print(f.renderText(f'{names[random_student].title()}'))

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
