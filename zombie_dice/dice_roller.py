#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 14:05:12 2023

@author: matthew
"""

import dice

# Make a dice
d8 = dice.Dice(8)

# Roll the dice 50 times
for i in range(500):
    print(d8.roll())
