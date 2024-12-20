#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 10:49:25 2023

@author: matthew
"""

import matplotlib.pyplot as plt
import sys

#%% Handle args
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
        X_POS_LIM = int(sys.argv[2])
        X_NEG_LIM = int(sys.argv[1])
        Y_POS_LIM = int(sys.argv[4])
        Y_NEG_LIM = int(sys.argv[3])
    except ValueError:
        print('Invalid arguments, exiting...')
        sys.exit()
    if X_POS_LIM <= X_NEG_LIM or Y_POS_LIM <= Y_NEG_LIM:
        print('Invalid entry, the first value should be the negative x '
              'limit, the second should be the positive x limit, '
              'the third should be the negative y limit, and the '
              'fourth should be the positive y limit.\n'
              'Please try again.')
        sys.exit()
else:
    while True:
        continue_flag = False
        print('Please enter the desired dimensions, with each value separated '
              'by a space. Ex. -10 10 -5 15:')
        try:
            value_string = input('> ')
        except KeyboardInterrupt:
            print('Exiting...')
            sys.exit()
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
            X_NEG_LIM, X_POS_LIM, Y_NEG_LIM, Y_POS_LIM = int_values
        except ValueError:
            print('Invalid entry (too many or too few values entered.\n'
                  'Please try again.')
            continue
        if X_POS_LIM <= X_NEG_LIM or Y_POS_LIM <= Y_NEG_LIM:
            print('Invalid entry, the first value should be the negative x '
                  'limit, the second should be the positive x limit, '
                  'the third should be the negative y limit, and the '
                  'fourth should be the positive y limit.\n'
                  'Please try again.')
            continue

        break

#%% Axis labels
print('Please enter the desired label for the x-axis. Press return to omit.')
try:
    x_label = input('> ')
except KeyboardInterrupt:
    print('Exiting...')
    sys.exit()
print('Please enter the desired label for the y-axis. Press return to omit.')
try:
    y_label = input('> ')
except KeyboardInterrupt:
    print('Exiting...')
    sys.exit()
y_label = ''.join([y_label, ' '])

"""
print('Would you like to invert the labels? (Y/n)')
flip_labels = input('> ')
no_values = ['n', 'N', 'no', 'No', 'NO']
if flip_labels not in no_values:
    y_placeholder = y_label
    y_label = x_label
    x_label = y_placeholder
"""
if -1*X_NEG_LIM == X_POS_LIM and -1*Y_NEG_LIM == Y_POS_LIM:
    # y_placeholder = y_label
    # y_label = x_label
    # x_label = y_placeholder
    x_label, y_label = y_label, x_label
else:
    y_label = ''.join([y_label, ' '*(len(y_label))])

#%% Build the plot
fig, ax = plt.subplots(figsize=(12, 10))

# Note that the x and y axis labels have been reversed, due to how
# matplotlib places labels.
ax.set_xlabel(x_label, fontsize=21)
ax.set_ylabel(y_label, rotation=0, fontsize=21)

ax.get_yaxis().set_label_coords(-0.03, 0.48)

print('Would you like to include tick labels? (y/N)')
try:
    tick_labels = input('> ')
except KeyboardInterrupt:
    print('Exiting...')
    sys.exit()
yes_values = ['y', 'Y', 'yes', 'Yes']
if tick_labels not in yes_values:
    # Remove tick labels
    ax.set_xticklabels([])
    ax.set_yticklabels([])
else:
    # Set the scale on the tick labels
    print('Please enter the desired scale for the x-axis ticks (default=1)')
    try:
        x_scale_input = input('> ')
    except KeyboardInterrupt:
        print('Exiting...')
        sys.exit()
    if x_scale_input == '':
        X_SCALE = 1
    else:
        try:
            X_SCALE = int(x_scale_input)
            x_tick_list = [X_SCALE*i for i in range(X_NEG_LIM, X_POS_LIM + 1)]
            ax.set_xticklabels(x_tick_list)
        except ValueError:
            print('Invalid entry for x scale')
            sys.exit()
    print('Please enter the desired scale for the y-axis ticks (default=1)')
    y_scale_input = input('> ')
    if y_scale_input == '':
        Y_SCALE = 1
    else:
        try:
            Y_SCALE = int(y_scale_input)
            y_tick_list = [Y_SCALE*i for i in range(Y_NEG_LIM, Y_POS_LIM + 1)]
            ax.set_yticklabels(y_tick_list)
        except ValueError:
            print('Invalid entry for y scale')
            sys.exit()

ax.set_xticks(range(X_NEG_LIM, X_POS_LIM + 1, 1))
ax.set_yticks(range(Y_NEG_LIM, Y_POS_LIM + 1, 1))

plt.xlim([X_NEG_LIM, X_POS_LIM])
plt.ylim([Y_NEG_LIM, Y_POS_LIM])

plt.grid(True)

plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')

print('Would you like to save the plot to a file? (y/N)?')
try:
    save_file = input('> ')
except KeyboardInterrupt:
    print('Exiting...')
    sys.exit()
if save_file in yes_values:
    print('Enter a file name for the saved plot, including the file extension.'
          ' Ex. 10x10.png')
    try:
        file_name = input('> ')
    except KeyboardInterrupt:
        print('Exiting...')
        sys.exit()
    print(f'Writing plot to {file_name}...')
    plt.savefig(file_name)
    print('Exiting...')
else:
    plt.show()
