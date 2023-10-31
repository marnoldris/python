#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 10:49:25 2023

@author: matthew
"""

import matplotlib.pyplot as plt
import sys

if len(sys.argv) == 3:
    try:
        X_POS_LIM = int(sys.argv[1])
        X_NEG_LIM = -1*int(sys.argv[1])
        Y_POS_LIM = int(sys.argv[2])
        Y_NEG_LIM = -1*int(sys.argv[2])
    except ValueError:
        print('Invalid arguments, exiting...')
        sys.exit()

elif len(sys.argv) == 5:
    try:
        X_POS_LIM = int(sys.argv[1])
        X_NEG_LIM = int(sys.argv[2])
        Y_POS_LIM = int(sys.argv[3])
        Y_NEG_LIM = int(sys.argv[4])
    except ValueError:
        print('Invalid arguments, exiting...')
        sys.exit()
    if X_POS_LIM <= X_NEG_LIM or Y_POS_LIM <= Y_NEG_LIM:
        print('Invalid entry, the first value should be the x positive '
              'limit, the second should be the x negative limit, '
              'the third should be the y positive limit, and the '
              'fourth should be the y negative limit.\n'
              'Please try again.')
        sys.exit()
else:
    while True:
        continue_flag = False
        print('Please enter the desired dimensions, with each value separated '
              'by a space. These should be four values:')
        value_string = input('> ')
        values = value_string.split(' ')
        int_values = []
        for value in values:
            try:
                int_values.append(int(value))
            except ValueError:
                print('Invalid entry, please try again')
                continue_flag = True
                break
        if continue_flag:
            continue
        try:
            X_POS_LIM, X_NEG_LIM, Y_POS_LIM, Y_NEG_LIM = int_values
        except ValueError:
            print('Invalid entry (too many or too few values entered.\n'
                  'Please try again.')
            continue
        if X_POS_LIM <= X_NEG_LIM or Y_POS_LIM <= Y_NEG_LIM:
            print('Invalid entry, the first value should be the x positive '
                  'limit, the second should be the x negative limit, '
                  'the third should be the y positive limit, and the '
                  'fourth should be the y negative limit.\n'
                  'Please try again.')
            continue

        break


fig, ax = plt.subplots(figsize=(12, 10))

ax.set_xlabel('x', fontsize=21)
ax.set_ylabel('y', rotation=0, fontsize=21)

ax.get_yaxis().set_label_coords(-0.03, 0.48)

# Remove labels
ax.set_xticklabels([])
ax.set_yticklabels([])

ax.set_xticks(range(X_NEG_LIM, X_POS_LIM + 1, 1))
ax.set_yticks(range(Y_NEG_LIM, Y_POS_LIM + 1, 1))

plt.xlim([X_NEG_LIM, X_POS_LIM])
plt.ylim([Y_NEG_LIM, Y_POS_LIM])

plt.grid(True)

plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')

plt.show()
