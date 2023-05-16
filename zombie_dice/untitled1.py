#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 15 12:51:44 2023

@author: matthew
"""

import dice

d6 = dice.Dice(6)
d100 = dice.Dice(100)

for i in range(20):
    print(d6.roll())

for i in range(20):
    print(d100.roll())
