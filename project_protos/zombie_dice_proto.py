import dice
import sys

# a list containing the dice needed for the game
dice_list = (dice.Dice(6), dice.Dice(6), dice.Dice(6))

yes_values = ('y', 'Y', '')   # values that will be considered a "yes"
brain_values = (1, 2, 3)      # dice values that count as a brain
escape_values = (4, 5)        # dice values that count as an escape
shotgun_values = (6)          # dice values that count as a shotgun

# dictionary to track brains, escapes, and shotguns
score_tracker = {
    'brains': 0,
    'escapes': 0,
    'shotguns': 0,
}


def score(dice_obj):
    """
    Function that takes a dice object, rolls it, then
    adds points to the corresponding score
    based on the value of the dice roll.
    """
    # TODO
    # Roll the dice object
    # Based on the value of the roll, add one to brains,
    # escapes, or shotguns (escapes will be handled in another function).
    # Each time a die is scored it should print a cute message
    # to the player so they know what they rolled (brain,
    # escape, or shotgun)
    pass

def reroll(dice_obj):
    """
    Function for rerolling an 'escaped' dice.
    """
    # TODO
    # Print a score_report()
    # Ask if the player wants to reroll an escape.
    # If the player answers yes, reroll the dice.
    # If the dice rolls an escape, keep rolling until it rolls a
    # brain or a shotgun, then add the score appropriately.
    pass

def game_over_check():
    """
    Function that checks if the user has gotten three shotguns, 
    thus losing the game.
    """
    # TODO
    # Check the number of shotguns
    # If the number of shotguns is 3 or more, set brains
    # to zero, print a message to the player, and end the game.
    pass

def score_report():
    """
    Function that prints a score report for the player.
    """
    # TODO
    # Print a message to the player that tells them how many
    # brains, escapes, and shotguns they have. Remember to 
    # account for the "one case." For example, if they have
    # 3 brains, you would print "You currently have 3 brains..."
    # However, if they have one brain, you would print
    # "You currently have 1 brain..."
    # Note the plural "brains" compared to "brain."
    pass


# TODO: Print the rules to the user


# TODO: Main gameplay loop starts here
while True:
    yes_or_no = input('Would you like to play the game (Y/n)?: ')

    if yes_or_no in yes_values:
        # TODO
        # Roll each of the three dice with your score() function
        # Check if the player loses the game
        # Run your reroll function for each of the dice
        # Check if the player loses the game
        # Run a score_report()
        pass
    else:
        # TODO
        # Run a score_report()
        sys.exit()
