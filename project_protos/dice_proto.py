import random

class Dice:
    
    def __init__(self, num_sides=12):
        """
        Simple class to emulate an n sided dice. The number of sides can
        be set when the dice is instantiated, default sides is 12.
        """
        self.num_sides = num_sides
        self.value = random.randint(1, self.num_sides)
    
    def roll(self):
        """
        Rolls the dice, setting self.value to a new random number
        within its range. Then returns that number.
        """
        pass
    
    def print_value(self):
        """
        Prints a formatted string with the current value of the dice.
        """
        pass

    def get_value(self):
        """
        Returns the current value of the dice.
        """
        pass

