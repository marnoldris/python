import random

class Dice:
    
    def __init__(self, num_sides):
        self.num_sides = num_sides
        self.value = random.randint(1, self.num_sides)
    
    def roll(self) -> int:
        self.value = random.randint(1, self.num_sides)
        return self.value
    
    def print_value(self):
        print(self.value)
        
    def get_value(self) -> int:
        return self.value
    
    def set_value(self, new_value):
        if new_value > self.num_sides or new_value < 1:
            print('Invalid entry, please try again.')
        else:
            self.value = new_value
    
d6 = Dice(6)    # instance of a d6
print(f'Number of sides: {d6.num_sides}')
d6.print_value()
print('Setting new value...')
d6.set_value(-10)
d6.print_value()
