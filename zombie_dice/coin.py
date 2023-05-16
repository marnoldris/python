import random as r

class Dice:
    """ Simple emulator for an n sided dice. Default is 12 sides. """

    def __init__(self, sides=12):
        """ Initializes a new dice. Takes an integer parameter
            for the number of sides. Default is 12. """
        self.sides = sides
        self.value = r.randint(1, self.sides)
    
    def roll(self) -> int:
        """ Uses random.randint to simulate rolling the dice.
            Returns an integer. """
        self.value = r.randint(1, self.sides)
        return self.value
    
    def get_value(self) -> int:
        """ Returns the current value of the dice (integer). """
        return self.value

    def print_value(self) -> None:
        """ Prints a nicely formatted string with the current value. """
        print(f'The value of the dice is {self.value}')

    def set_value(self, new_value) -> None:
        """ Sets the value of the dice to a specific number.
            Takes an integer for the new value. """
        if new_value > self.sides or new_value < 1:
            print('Invalid dice value.')
        else:
            self.value = new_value
    
    def get_sides(self) -> int:
        """ Returns the number of sides of the dice (integer). """
        return self.sides

    def set_sides(self, new_sides) -> None:
        """ Sets the number of sides of the dice.
            Takes an integer for the new number of sides. """
        if new_sides < 1:
            print('Invalid value for the number of sides')
        else:
            self.sides = new_sides

class Coin(Dice):
    
    def __init__(self):
        super().__init__(2)

    def flip(self):
        return self.roll()


c1 = Coin()
for i in range(50):
    print(c1.flip())
