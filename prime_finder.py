#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 22:56:28 2023

@author: bard
"""

import math

def is_prime(n) -> bool:
    if n < 2:
        return False
    print(range(2, int(math.sqrt(n) + 1)))
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

def find_primes(numbers) -> list:
    primes = []
    for number in numbers:
        if is_prime(number):
            primes.append(number)
    return primes

nums = [i for i in range(0, 101)]
print(find_primes(nums))
