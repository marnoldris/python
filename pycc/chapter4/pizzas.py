"""
Prints out names of pizzas and a sentence about them
by iterating through with for loops
"""

# 4-1 Pizzas
pizzas = ['pepperoni','cowboy','hawaiian']

for pizza in pizzas:
    print(pizza)
print('\n')

for pizza in pizzas:
    print(f'I really like {pizza}')
print('\n')

print('I like pizza a little too much.')

# 4-11 My Pizzas, Your Pizzas
friend_pizzas = pizzas[:]

pizzas.append('bbq chicken')

friend_pizzas.append('margharita')

print('\nMy favorite pizzas are:')
for pizza in pizzas:
    print(pizza)

print('\nMy friend\'s favorite pizzas are:')
for pizza in friend_pizzas:
    print(pizza)
