#!/usr/bin/python

import math
##import pdb;pdb.set_trace()

colors = {
    'white': 0,
    'black': 0,
    'red': 0,
    'green': 0,
    'blue': 0,
    }

white_values = ['w', 'W', 'white', 'White']
black_values = ['b', 'B', 'black', 'Black']
red_values = ['r', 'R', 'red', 'Red']
green_values = ['g', 'G', 'green', 'Green']
blue_values = ['u', 'U', 'blue', 'Blue']

last_entry = ''
color_entry = ''

deck_size = 0
while deck_size == 0:
    try:
        deck_size = int(input('Enter the number of cards in the deck: '))
    except ValueError:
        print('Invalid entry, please enter an integer number of cards.')
    else:
        num_lands = math.ceil(deck_size * 0.41)

def add_color(color_string) -> str:
    color_added = ''
    if color_string in white_values:
        colors['white'] += 1
        color_added = 'white'
    elif color_string in black_values:
        colors['black'] += 1
        color_added = 'black'
    elif color_string in red_values:
        colors['red'] += 1
        color_added = 'red'
    elif color_string in green_values:
        colors['green'] += 1
        color_added = 'green'
    elif color_string in blue_values:
        colors['blue'] += 1
        color_added = 'blue'
    return color_added

def calc_colors():
    print()
    num_colors = 0
    color_sum = 0
    ## Count the number of colors that have any entries
    for k, v in colors.items():
        if v > 0:
            num_colors += 1
            color_sum += v

    ## Normalize the numbers of each color to 100 and print
    ## the result.
    for k, v in colors.items():
        if v > 0:
            percentage = v * 100 / color_sum
            print(f'{k.title()}: {math.ceil(percentage)}%')
            print(f'{k.title()} sources: {math.ceil(percentage * num_lands/100)}', end='\n\n')
    print(f'Total number of recommended lands: {num_lands}.')

## Print instructions   
print(
"""Welcome to the MTG color tally and mana calculator.
Enter the color you'd like to add to the tally (w, b, r, g, u),
or q to quit. If you want to repeat the last tally, just press return.
"""
)

## Main loop
while True:
    try:
        color_entry = input('Enter a color to tally: ')
            
        if color_entry == 'q' or color_entry == 'Q':
            break
        if color_entry == '' and last_entry != '':
            add_color(last_entry)
            print(f'{last_entry.title()}: {colors[last_entry]}', end='\n\n')
        else:
            last_entry = add_color(color_entry)
            print(f'{last_entry.title()}: {colors[last_entry]}', end='\n\n')
        
    except (KeyboardInterrupt, KeyError) as e:
        if isinstance(e, KeyError):
            print('Invalid entry.')
        else:
            ## Print tally and recommendation, then quit
            print()
            for color, count in colors.items():
                print(f'{color.title()}: {count}')
            calc_colors()
            quit()

## Print tally and recommendation
print()
for color, count in colors.items():
    print(f'{color.title()}: {count}')
calc_colors()
