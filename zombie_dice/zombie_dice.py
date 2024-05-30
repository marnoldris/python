#!/usr/bin/python

import sys
import dice

# a list containing the dice needed for the game
dice_list = [dice.Dice(6), dice.Dice(6), dice.Dice(6)]

yes_values = ['y', 'Y', '']   # values that will be considered a "yes"
brain_values = [1, 2, 3]      # dice values that count as a brain
escape_values = [4, 5]        # dice values that count as an escape
shotgun_values = [6]          # dice values that count as a shotgun

# dictionary to track brains, escapes, and shotguns
score_tracker = {
    'brains': 0,
    'escapes': 0,
    'shotguns': 0,
}


def score(dice_obj):
    """ Function that takes a dice object and our score tracker
        dictionary and adds points to the corresponding score
        based on the value of the dice roll """
    result = dice_obj.roll()

    if result in brain_values:
        score_tracker['brains'] += 1
        print('You rolled a brain! Yum!')
    elif result in escape_values:
        print('You rolled an escaped victim! :o')
    else:
        score_tracker['shotguns'] += 1
        print('You rolled a shotgun! :(')

def reroll(dice_obj):
    """ Function for rerolling an 'escaped' dice. """
    score_report()
    print('Would you like to reroll one of your escapes? (Y/n)\n')
    try:
        question = input('> ')
    except KeyboardInterrupt:
        print('Keyboard interrupt received, exiting...')
        sys.exit()
    if question in yes_values:
        result = dice_obj.roll()

        while result in escape_values:
            result = dice_obj.roll()
        if result in brain_values:
            score_tracker['brains'] += 1
            print('You caught the escapee and rolled some brains! :D')
        elif result in shotgun_values:
            score_tracker['shotguns'] += 1
            print('Your escapee lured you into a shotgun trap! :(')
    else:
        print('\nYou let your victim escape! :v')
        score_tracker['escapes'] += 1

def game_over_check():
    """ Function that checks if the user has gotten three shotguns, thus losing """
    if score_tracker['shotguns'] > 2:
        print(f'\nGame over! You lost all your brains!')
        score_tracker['brains'] = 0
        sys.exit()

def score_report():
    """ Function that prints a score report for the player """
    print(f'\nYou currently have {score_tracker["brains"]}'
          f' {"brains" if score_tracker["brains"] != 1 else "brain"},'
          f' {score_tracker["escapes"]}'
          f' {"escapes" if score_tracker["escapes"] != 1 else "escape"},'
          f' and {score_tracker["shotguns"]}'
          f' {"shotguns" if score_tracker["shotguns"] != 1 else "shotgun"}.'
    )

""" Print the rules of the game """
print('In this game, you are a zombie trying to get some yummy, yummy brains.'
      '\nEach round you roll three dice. Depending on the outcome of each roll,'
      ' you can get a brain, an escapee, or a shotgun.\nIf you accumulate 3'
      ' shotguns, it is game over and you lose all of your brains. If you'
      ' roll an escapee, you can choose to "give chase" and roll again.\nThe'
      ' goal is to get as many brains as you can, then quit while you\'re'
      ' "ahead"!'
)

# Main gameplay loop starts here
while True:
    try:
        print('\nWould you like to roll the dice? (Y/n)\n')
        print('CTRL+C to quit')
        play = input('> ')

    except KeyboardInterrupt:
        print('Exiting...')
        sys.exit()
        
    if play in yes_values:
        for dice in dice_list:
            score(dice)

        game_over_check()

        for dice in dice_list:
            if dice.get_value() in escape_values:
                reroll(dice)
        
        game_over_check()
        score_report()
    else:
        print(f'\nGame over! You scored {score_tracker["brains"]}'
              f' {"brains" if score_tracker["brains"] != 1 else "brain"}!')
        sys.exit()
