#!/usr/bin/python

import dice
from time import sleep

def score(dice, rolls):
    yes = ['y', 'Y', '']
    result = dice.roll()
    sleep(0.3)
    if result == 1:
        rolls['brains'] += 1
        print('You rolled a brain! Yum!')
    elif result == 2:
        print('You rolled an escaped victim! :(')
        sleep(0.3)
        play_again = input('\nWould you like to re-roll this dice? (Y/n)\n')
        if play_again in yes:
            score(dice, rolls)
        else:
            rolls['escape'] += 1
    else:
        rolls['shotgun'] += 1
        print('You rolled a shotgun! D:')
        if rolls['shotgun'] > 2:
            sleep(0.3)
            print(f'\nGame over! You lost all your brains!')
            rolls['brains'] = 0
            exit()
            

dice = [dice.Dice(3), dice.Dice(3), dice.Dice(3)]

yes = ['y', 'Y', '']

rolls = {'brains': 0, 'escape': 0, 'shotgun': 0}


while True:
    play = input('\nWould you like to roll the dice? (Y/n)\n')
    if play in yes:
        for d in dice:
            score(d, rolls)
        sleep(0.3)
        print(f'You currently have {rolls["brains"]} brains,'
              f' {rolls["escape"]} escapes, and {rolls["shotgun"]} shotguns.')

        if rolls['shotgun'] > 2:
            sleep(0.3)
            print(f'\nGame over! You scored lost all your brains!')
            rolls['brains'] = 0
            exit()
     
    else:
        print(f'\nGame over! You scored {rolls["brains"]} brains!')
        exit()
