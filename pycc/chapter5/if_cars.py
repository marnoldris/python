"""
Basic practice of if statements
"""

car = 'subaru'
print('is car == \'subaru\'? I think so')

print('is car == \'toyota\'? I don\'t think so')

if car == 'subaru':
    print('car is subaru!')


cars = ['subaru','toyota','lexus']
if 'subaru' in cars:
    print('Yay Subaru!')

if 'acura' not in cars:
    print('We own good cars')

count = 0
for car in cars:
    if car == 'subaru':
        break
    else:
        count = count + 1
print(f'Index of subaru: {count}')

count = 0
if 'lexus' not in cars:
    print('lexus not found')
else:
    for car in cars:
        if car.lower() == 'lexus':
            break
        else:
            count = count + 1
    print(f'Index of lexus: {count}')

# taking input with input()
usr_input = input('Name a car brand you like\n')

if usr_input.lower() in cars:
    print('Good choice!')
else:
    print('Try again :)')
