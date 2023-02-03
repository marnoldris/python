#!/usr/bin/python

import dice
from time import sleep


dice_list = [dice.Dice(6), dice.Dice(6), dice.Dice(6)]

yes = ['y', 'Y', '']
brains = [1, 2, 3]
escape = [4, 5]
shotgun = [6]
rolls = {'brains': 0, 'escape': 0, 'shotgun': 0}


def score(dice_obj, rolls):
    result = dice_obj.roll()
    if result in brains:
        rolls['brains'] += 1
        print('You rolled a brain! Yum!')
    elif result in escape:
        print('You rolled an escaped victim! :o')
    else:
        rolls['shotgun'] += 1
        print('You rolled a shotgun! :(')

def reroll(dice_obj, rolls):
    print(f'\nYou currently have {rolls["brains"]} brain(s),'
          f' {rolls["escape"]} escape(s), and {rolls["shotgun"]} shotgun(s).')
    question = input('Would you like to reroll one of your escapes? (Y/n)\n')
    if question in yes:
        result = dice_obj.roll()
        while result in escape:
            result = dice_obj.roll()
        if result in brains:
            rolls['brains'] += 1
            print('You caught the escapee and rolled some brains! :D')
        elif result in shotgun:
            rolls['shotgun'] += 1
            print('Your escapee lured you into a shotgun trap! :(')
    else:
        print('You let your victim escape! :v')
        rolls['escape'] += 1

def game_over_check():
    if rolls['shotgun'] > 2:
        sleep(0.3)
        print(f'\nGame over! You lost all your brains!')
        rolls['brains'] = 0
        exit()

print('In this game, you are a zombie trying to get some yummy, yummy brains.'
      '\nTo start, you roll three dice. Depending on the outcome of each roll,'
      ' you can get a brain, an escapee, or a shotgun.\nIf you accumulate 3'
      ' shotguns, it is game over and you lose all of your brains. If you'
      ' roll an escapee, you can choose to "give chase" and roll again.\nThe'
      ' goal is to get as many brains as you can, then quit while you\'re'
      ' "ahead"!'
)

while True:
    play = input('\nWould you like to roll the dice? (Y/n)\n')
    if play in yes:
        for d in dice_list:
            score(d, rolls)
            sleep(0.3)

        game_over_check()

        for d in dice_list:
            if d.get_value() in escape:
                reroll(d, rolls)
                sleep(0.3)
        
        game_over_check()
        
        print(f'\nYou currently have {rolls["brains"]} brain(s),'
              f' {rolls["escape"]} escape(s), and {rolls["shotgun"]} shotgun(s).')
     
    else:
        print(f'\nGame over! You scored {rolls["brains"]} brain(s)!')
        exit()
