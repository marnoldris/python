#!/usr/bin/python

import dice
from time import sleep

def score(dice, rolls):
    yes = ['y', 'Y', '']
    brains = [1, 2, 3]
    escape = [4, 5]
    shotgun = [6]
    result = dice.roll()
    sleep(0.3)
    if result in brains:
        rolls['brains'] += 1
        print('You rolled a brain! Yum!')
    elif result in escape:
        print('You rolled an escaped victim! :o')
        sleep(0.3)
        play_again = input('\nWould you like to chase them '
                           '(re-roll this dice)? (Y/n)\n')
        if play_again in yes:
            score(dice, rolls)
        else:
            rolls['escape'] += 1
    else:
        rolls['shotgun'] += 1
        print('You rolled a shotgun! :(')
        if rolls['shotgun'] > 2:
            sleep(0.3)
            print(f'\nGame over! You lost all your brains!')
            rolls['brains'] = 0
            exit()
            

dice = [dice.Dice(6), dice.Dice(6), dice.Dice(6)]

yes = ['y', 'Y', '']

rolls = {'brains': 0, 'escape': 0, 'shotgun': 0}


while True:
    play = input('\nWould you like to roll the dice? (Y/n)\n')
    if play in yes:
        for d in dice:
            score(d, rolls)
        sleep(0.3)
        print(f'You currently have {rolls["brains"]} brain(s),'
              f' {rolls["escape"]} escape(s), and {rolls["shotgun"]} shotgun(s).')

        if rolls['shotgun'] > 2:
            sleep(0.3)
            print(f'\nGame over! You scored lost all your brains!')
            rolls['brains'] = 0
            exit()
     
    else:
        print(f'\nGame over! You scored {rolls["brains"]} brain(s)!')
        exit()
