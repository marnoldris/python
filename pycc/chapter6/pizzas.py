"""
Create a list inside a dictionary, alongside non-list data
"""

pizza = {
    'crust': 'thin',
    'toppings': ['mushrooms', 'pepperoni'],
    }

# note the double quotes inside the single quotes
print(f'The pizza is a {pizza["crust"]}-crust pizza with '
       'these toppings: ')

for topping in pizza['toppings']:
    print(f'\t{topping}')
