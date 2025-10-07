#!/usr/bin/python
"""
A simple algorithm that calculates the greatest common 
divisor for two numbers, based on \"Euclid's Algorithm\"
"""

def gcd(a, b):
    larger = max(a, b)
    smaller = min(a, b)

    remainder = larger % smaller

    if remainder == 0:
        return smaller
    else:
        return gcd(smaller, remainder)

n1 = int(input('Enter a number: '))
n2 = int(input('Enter another number: '))

print(f'Greatest common divisor between {n1} and {n2} is:'
      f' {gcd(n1, n2)}')
