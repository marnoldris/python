#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 15:46:16 2023

@author: matthew
"""


import json


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


filename = 'pokedex.json'
try:
    with open(filename, 'w') as f:
        json.dump(pokedex, f)
except Exception as e:
    print(e, type(e))

try:
    with open(filename) as f:
        dex = json.load(f)
except FileNotFoundError:
    print('File not found!')
else:
    for k, v in dex.items():
        print(f'{k}:')
        for value in v.values():
            print(f'   {value}')
            
