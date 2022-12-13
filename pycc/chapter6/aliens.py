"""
Create a list of alien dictionaries
(list of dictionaries or dictionaries inside a list)
"""

import random

aliens = []

for i in range(10):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens:
    print(alien)

print('----------------------------')

for alien in aliens:
    print(alien['color'])   # note the '' around color

print('----------------------------')

# change the color, points, and speed of the first three aliens
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'

for alien in aliens[:5]:
    print(alien)

print('----------------------------')

# function to change alien color randomly, 
# and change their attributes appropriately
def randomizealien(alien):
    colors = ['green', 'yellow', 'red']
    alien['color'] = random.choice(colors)
    if alien['color'] == 'green':
        alien['points'] = 5
        alien['speed'] = 'slow'
    elif alien['color'] == 'yellow':
        alien['points'] = 10
        alien['speed'] = 'medium'
    else:
        alien['points'] = 15
        alien['speed'] = 'fast'

for alien in aliens:
    randomizealien(alien)
    print(alien)
