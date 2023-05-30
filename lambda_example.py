#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 21 14:33:02 2023

@author: matthew
"""

# Data
txt = ['lambda functions are anonymous functions',
       'anonymous functions do not have a name',
       'functions are objects in Python']

mark = map(lambda s: (True, s) if 'anonymous' in s else (False, s), txt)

print(list(mark))
