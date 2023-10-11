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
    
    def print_dice(self) -> str:
        """ Pretty prints a representation of the dice. """
        # Temp solution to restrict it to d6
        if self.sides != 6:
            return None
        
        UL = chr(9484)
        UR = chr(9488)
        BL = chr(9492)
        BR = chr(9496)
        H = chr(9472)
        V = chr(9474)
        C = chr(9532)
        CL = chr(9500)
        CR = chr(9508)
        P = chr(9679)
        
        dice_list = {
            'd6': {
                1: [
                    UL+    H*7    +UR,
                    V+  '       '  +V,
                    V+'   '+P+'   '+V,
                    V+  '       '  +V,
                    BL+    H*7    +BR,
                ],
                2: [
                    UL+    H*7    +UR,
                    V+' '+P+'     '+V,
                    V+  '       '  +V,
                    V+'     '+P+' '+V,
                    BL+    H*7    +BR,
                ],
                3: [
                    UL+    H*7    +UR,
                    V+'     '+P+' '+V,
                    V+'   '+P+'   '+V,
                    V+' '+P+'     '+V,
                    BL+    H*7    +BR,
                ],
                4: [
                    UL+      H*7      +UR,
                    V+' '+P+'   '+P+' '+V,
                    V+    '       '    +V,
                    V+' '+P+'   '+P+' '+V,
                    BL+      H*7      +BR,
                ],
                5: [
                    UL+      H*7      +UR,
                    V+' '+P+'   '+P+' '+V,
                    V+  '   '+P+'   '  +V,
                    V+' '+P+'   '+P+' '+V,
                    BL+      H*7      +BR,
                ],
                6: [
                    UL+      H*7      +UR,
                    V+' '+P+'   '+P+' '+V,
                    V+' '+P+'   '+P+' '+V,
                    V+' '+P+'   '+P+' '+V,
                    BL+      H*7      +BR,
                ],
            }
        }
        
        return '\n'.join(dice_list['d6'][self.value])
