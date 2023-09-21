#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 10:37:20 2023

@author: matthew
"""

text = [
        'lambda functions are anonymous functions.',
        'anonymous functions dont have a name.',
        'functions are objects in Python.'
        ]

#mark = map(lambda s: (True, s) if 'anonymous' in s else (False, s), text)
#print(list(mark))

list_mark = [(True, s) if 'anonymous' in s else (False, s) for s in text]
print(list_mark)
