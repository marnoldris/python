#!/usr/bin/python

import dice
from time import sleep


dice_list = [dice.Dice(6), dice.Dice(6), dice.Dice(6)]

yes = ['y', 'Y', '']
brains = [1, 2, 3]
escape = [4, 5]
shotgun = [6]
score_tracker = {'brains': 0, 'escape': 0, 'shotgun': 0}


def score(dice_obj, score_tracker_dict):
    result = dice_obj.roll()
    if result in brains:
        score_tracker_dict['brains'] += 1
        print('You rolled a brain! Yum!')
    elif result in escape:
        print('You rolled an escaped victim! :o')
    else:
        score_tracker_dict['shotgun'] += 1
        print('You rolled a shotgun! :(')

def reroll(dice_obj, score_tracker):
    score_report()
    question = input('Would you like to reroll one of your escapes? (Y/n)\n')
    if question in yes:
        result = dice_obj.roll()
        while result in escape:
            result = dice_obj.roll()
        if result in brains:
            score_tracker['brains'] += 1
            print('You caught the escapee and rolled some brains! :D')
        elif result in shotgun:
            score_tracker['shotgun'] += 1
            print('Your escapee lured you into a shotgun trap! :(')
    else:
        print('You let your victim escape! :v')
        score_tracker['escape'] += 1

def game_over_check():
    if score_tracker['shotgun'] > 2:
        sleep(0.3)
        print(f'\nGame over! You lost all your brains!')
        score_tracker['brains'] = 0
        exit()

def score_report():
    brain_report = ''
    escape_report = ''
    shotgun_report = ''
    if score_tracker['brains'] == 1:
        brain_report = '1 brain'
    else:
        brain_report = f'{score_tracker["brains"]} brains'
    if score_tracker['escape'] == 1:
        escape_report = '1 escape'
    else:
        escape_report = f'{score_tracker["escape"]} escapes'
    if score_tracker['shotgun'] == 1:
        shotgun_report = '1 shotgun'
    else:
        shotgun_report = f'{score_tracker["shotgun"]} shotguns'

    print(f'\nYou currently have {brain_report},'
          f' {escape_report}, and {shotgun_report}.')


print('In this game, you are a zombie trying to get some yummy, yummy brains.'
      '\nEach round you roll three dice. Depending on the outcome of each roll,'
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
            score(d, score_tracker)
            sleep(0.3)

        game_over_check()

        for d in dice_list:
            if d.get_value() in escape:
                reroll(d, score_tracker)
                sleep(0.3)
        
        game_over_check()
        score_report()
    else:
        print(f'\nGame over! You scored {score_tracker["brains"]}'
              f' {"brains" if score_tracker["brains"] != 1 else "brain"}!')
        exit()
