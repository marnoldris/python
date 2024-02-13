#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 09:03:58 2023

@author: matthew
"""

def gcd(larger, smaller):
    if larger < smaller:
        larger, smaller = smaller, larger
    
    r = larger % smaller
    
    if r == 0:
        return smaller
    else:
        return gcd(smaller, r)

print(gcd(100, 40))
