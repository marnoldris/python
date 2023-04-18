
import os, pdb
import json

#pdb.set_trace()
numbers = [i**i for i in range(10)]

pokedex = {
    'charmander': {
        'move0': 'slash',
        'move1': 'flamethrower',
        'move2': 'fire blast',
        'move3': 'fly',
        },
    'bulbasaur': {
        'move0': 'razor leaf',
        'move1': 'solar beam',
        'move2': 'synthesis',
        'move3': 'bite',
        },
    }

## This only stores the data from these structures,
## not the names of the structures themselves. You
## assign the variable name to the data structures
## when you read it in again.
data_to_save = {
    'number list': numbers,
    'pokedex': pokedex,       
    }

filename = 'stuff.json'
try:
    with open(filename, 'w') as file:
        json.dump(data_to_save, file)
except Exception as e:
    print(e, type(e))
else:
    print(os.listdir())

try:
    with open(filename, 'r') as file:   # the 'r' is optional, default behavior is read
        stuff = json.load(file)
except FileNotFoundError:
    print('File not found!')
else:
    pokedex = stuff['pokedex']
    for k, v in pokedex.items():
        print(f'{k}:')
        for value in v.values():
            print(f'   {value}')
            
