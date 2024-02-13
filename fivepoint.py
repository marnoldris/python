#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 12:41:42 2024

@author: matthew
"""

import statistics
import sys
import math

#%% Generate a list with the five point summary
def get_fivepoint(data) -> list:
    data.sort()
    fivepoint = []
    
    data_min = data[0]
    data_max = data[-1]
    fivepoint.append(data_min)
    
    q1 = find_middle_value(data[:(len(data) // 2)])
    fivepoint.append(q1)
    
    median = find_middle_value(data)
    fivepoint.append(median)
    
    if len(data) % 2 == 0:
        q3 = find_middle_value(data[(len(data) // 2):])
    else:
        q3 = find_middle_value(data[(len(data) // 2 + 1):])
    fivepoint.append(q3)
    
    fivepoint.append(data_max)
    
    return fivepoint

#%% Find the middle value
def find_middle_value(data) -> float:
    data.sort()
    if len(data) % 2 == 0:
        low_mid = len(data) // 2 - 1
        high_mid = low_mid + 1
        return statistics.mean([data[low_mid], data[high_mid]])
    else:
        output = data[math.ceil(len(data) / 2) - 1]
        return output

#%% Neatly print the five point summary
def print_fivepoint(data) -> None:
    print(f'Min: {data[0]}')
    print(f'Q1: {data[1]}')
    print(f'Median: {data[2]}')
    print(f'Q3: {data[3]}')
    print(f'Max: {data[4]}')
        

#%% Main
def main():
    
    if len(sys.argv) > 1:
        data_strings = sys.argv[1:]
        data = []
        for string in data_strings:
            data.append(float(string))
            
    else:
        print('Please enter the data set, with each value separated by a space:')
        raw_data = input('> ')
        data_strings = raw_data.split(' ')
        data = []
        for string in data_strings:
            data.append(float(string))
    
    fivepoint = get_fivepoint(data)
    print_fivepoint(fivepoint)

if __name__ == '__main__':
    main()
