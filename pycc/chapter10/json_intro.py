#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 14:49:26 2024

@author: matthew
"""

# Working with JSON files

import json


data_to_save = {
    'thing0': 0,
    'thing1': 1,
    }

filename = 'save_data.json'

with open(filename, 'w') as f:
    json.dump(data_to_save, f, indent=4)
    
other_data = {
    'test': 0,
    }

with open(filename, 'w') as f:
    json.dump(other_data, f, indent=4)
    

with open(filename) as f:
    opened_data = json.load(f)
print(type(opened_data))
