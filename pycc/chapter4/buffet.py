"""
Example of tuples (immutable lists) and their usage
"""

foods = ('pizza','filet mignon','halibut','cod','quinoa')

for food in foods:
    print(food)
print()

#foods[0] = 'blt'    # this won't work due to immutability

# To "change" a tuple, you need to change the variable to point
# to a new tuple
foods = ('blt','parm. chicken','halibut','cod','quinoa')

for food in foods:
    print(food)
print()
