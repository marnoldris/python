#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 21:30:37 2023

@author: bard
"""

def get_sevseg_str(number, min_width=0):
    
    number = str(number).zfill(min_width)
    
    rows = ['', '', '']
    for i, numeral in enumerate(number):
        if numeral == '.':
            rows[0] = ''.join([rows[0], ' '])
            rows[1] = ''.join([rows[1], ' '])
            rows[2] = ''.join([rows[2], chr(9632)])
            continue
        elif numeral == '-':
            rows[0] = ''.join([rows[0], '    '])
            rows[1] = ''.join([rows[1], ' __ '])
            rows[2] = ''.join([rows[2], '    '])
        elif numeral == '0':
            rows[0] = ''.join([rows[0], ' __ '])
            rows[1] = ''.join([rows[1], '|  |'])
            rows[2] = ''.join([rows[2], '|__|'])
        elif numeral == '1':
            rows[0] = ''.join([rows[0], '    '])
            rows[1] = ''.join([rows[1], '   |'])
            rows[2] = ''.join([rows[2], '   |'])
        elif numeral == '2':
            rows[0] = ''.join([rows[0], ' __ '])
            rows[1] = ''.join([rows[1], ' __|'])
            rows[2] = ''.join([rows[2], '|__ '])
        elif numeral == '3':
            rows[0] = ''.join([rows[0], ' __ '])
            rows[1] = ''.join([rows[1], ' __|'])
            rows[2] = ''.join([rows[2], ' __|'])
        elif numeral == '4':
            rows[0] = ''.join([rows[0], '    '])
            rows[1] = ''.join([rows[1], '|__|'])
            rows[2] = ''.join([rows[2], '   |'])
        elif numeral == '5':
            rows[0] = ''.join([rows[0], ' __ '])
            rows[1] = ''.join([rows[1], '|__ '])
            rows[2] = ''.join([rows[2], ' __|'])
        elif numeral == '6':
            rows[0] = ''.join([rows[0], ' __ '])
            rows[1] = ''.join([rows[1], '|__ '])
            rows[2] = ''.join([rows[2], '|__|'])
        elif numeral == '7':
            rows[0] = ''.join([rows[0], ' __ '])
            rows[1] = ''.join([rows[1], '   |'])
            rows[2] = ''.join([rows[2], '   |'])
        elif numeral == '8':
            rows[0] = ''.join([rows[0], ' __ '])
            rows[1] = ''.join([rows[1], '|__|'])
            rows[2] = ''.join([rows[2], '|__|'])
        elif numeral == '9':
            rows[0] = ''.join([rows[0], ' __ '])
            rows[1] = ''.join([rows[1], '|__|'])
            rows[2] = ''.join([rows[2], ' __|'])
        
        if i != len(number) - 1:
            rows[0] = ''.join([rows[0], ' '])
            rows[1] = ''.join([rows[1], ' '])
            rows[2] = ''.join([rows[2], ' '])
    return '\n'.join(rows)


if __name__ == '__main__':
    print(get_sevseg_str(36, 3))
    print(get_sevseg_str(36, 2))
