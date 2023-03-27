#!/usr/bin/python

import random
import pyperclip


n1 = int(input('\nPlease enter the lower bound: '))
n2 = int(input('Please enter the upper bound: '))
number_of_numbers = int(input('Please enter the desired number of numbers: '))

bounds = (n1, n2)
lower = min(bounds)
upper = max(bounds)

random_numbers = [random.randint(lower, upper) for i in range(number_of_numbers)]

output = ', '.join(str(i) for i in random_numbers)

print('\n\nRandom numbers: ', end='\n\n')
print(output)

pyperclip.copy(output)
print()
print('List has been copied to clipboard.')
