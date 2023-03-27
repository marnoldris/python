#!/usr/bin/python

import random, sys
import pyperclip

if len(sys.argv) == 1:
    n1 = int(input('\nPlease enter the lower bound: '))
    n2 = int(input('Please enter the upper bound: '))
    number_of_numbers = int(input('Please enter the desired number of numbers: '))
elif len(sys.argv) == 4:
    n1 = int(sys.argv[1])
    n2 = int(sys.argv[2])
    number_of_numbers = int(sys.argv[3])
else:
    print(f'Usage: $ {sys.argv[0]} with no arguments to interactively '
          f'add upper and lower bounds, as well as a length for the list. '
          f'\n\nOr $ {sys.argv[0]} <lower bound> <upper bound> <length> to '
          f'specify bounds at run time.'
)
    exit()

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
