#!/usr/bin/python

import sympy as s

""" Take a function from the user in the form of a string, then turn it
    into a sympy function """
fct = s.parse_expr(input('Enter the desired function. Note that symbols '
                         'must be in Python syntax (i.e. instead of x^2, '
                         ' enter x**2).\n> '
))

""" Get the desired domain """
x1 = float(input('Enter the start of the desired domain: '))
x2 = float(input('Enter the end of the desired domain: '))

""" Some important global variables """
NUM_STEPS = 10_000
PRECISION = 2
x = s.symbols('x')
sum_step = (x2 - x1)/NUM_STEPS
reimann_sum = 0

""" Check if the user got the order of the domain wrong and fix it """
if x1 > x2:
    placeholder = x1
    x1 = x2
    x2 = placeholder

""" Calculate the Reimann sum. This equates to multiplying width (sum_step)
    by height (f(n)) and adding it all up """
for i in range(NUM_STEPS):
    reimann_sum += sum_step * fct.subs(x, (x1+i*sum_step))

""" Round to the desired level of precision """
reimann_sum = float('{:0.2f}'.format(round(reimann_sum, PRECISION)))

""" Print the result """
print(f'Area under the curve in the given domain: {reimann_sum}')
