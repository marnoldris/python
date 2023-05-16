#!/usr/bin/python

user_function = input('Enter your function in terms of x: ')

def solve_f(f_x, x):
    return eval(f_x)

for x in range(10):
    print(f'f({x}) = {solve_f(user_function, x)}')
