#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 13:10:54 2023

@author: matthew
"""

import pathlib

words = {}

try:
    """
    with open('dictionary.txt') as d:
        for line in d.readlines():
            tokens = line.strip().split(' ')
            max_word = max(tokens)
            for token in tokens:
                for i in range(1, len(max_word) + 1):
                    if len(token) == i:
                        if i not in words.keys():
                            words[i] = []
                        words[i].append(token)
    """
    path = pathlib.Path('dictionary.txt')
    contents = path.read_text()     # this returns a string
    lines = contents.split('\n')    # split the string into a list of lines
    for line in lines:
        tokens = line.strip().split(' ')
        max_word = max(tokens)
        for token in tokens:
            for i in range(1, len(max_word) + 1):
                if len(token) == i:
                    if i not in words.keys():
                        words[i] = []
                    words[i].append(token)
    
except FileNotFoundError:
    print('File not found!')
    
            
