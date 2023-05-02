#!/usr/bin/python

import math, sys

colors = {
    'white': 0,
    'blue': 0,
    'black': 0,
    'red': 0,
    'green': 0,
    }

white_values = ['w', 'W', 'white', 'White']
blue_values = ['u', 'U', 'blue', 'Blue']
black_values = ['b', 'B', 'black', 'Black']
red_values = ['r', 'R', 'red', 'Red']
green_values = ['g', 'G', 'green', 'Green']

last_entry = ''
color_entry = ''

print()
deck_size = 0
while deck_size <= 0:
    try:
        deck_size = int(input('Enter the number of cards in the deck: '))
        if deck_size < 1:
            print('Please enter a positive integer greater than 0.')
            continue
    except ValueError:
        print('Invalid entry, please enter an integer number of cards.')
    else:
        num_lands = math.ceil(deck_size * 0.41)

def add_color(color_string) -> str:
    color_added = ''
    if color_string in white_values:
        colors['white'] += 1
        color_added = 'white'
    elif color_string in blue_values:
        colors['blue'] += 1
        color_added = 'blue'
    elif color_string in black_values:
        colors['black'] += 1
        color_added = 'black'
    elif color_string in red_values:
        colors['red'] += 1
        color_added = 'red'
    elif color_string in green_values:
        colors['green'] += 1
        color_added = 'green'
    return color_added

def calc_colors():
    print()
    num_colors = 0
    color_sum = 0
    color_total = 0
    ## Count the number of colors that have any entries
    for k, v in colors.items():
        if v > 0:
            num_colors += 1
            color_sum += v

    ## Normalize the numbers of each color to 100 and print the result.
    for k, v in colors.items():
        if v > 0:
            color_percent = v * 100 / color_sum
            color_sources = math.ceil(color_percent * num_lands/100)
            color_total += color_sources
            print(f'{k.title()}: {math.ceil(color_percent)}%')
            print(f'{k.title()} sources: {color_sources}', end='\n\n')

    print(f'Total number of recommended lands: {color_total}.')

def print_totals() -> None:
    print('\n------------------------')
    for color, count in colors.items():
        if count > 0:
            print(f'{color.title():<5}: {count}')
    

## Print instructions   
print(
"""
Welcome to the MTG color tally and mana calculator.
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
        elif isinstance(e, KeyboardInterrupt):
            break

## Print tally and recommendation
print_totals()
calc_colors()
