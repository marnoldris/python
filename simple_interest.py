#!/usr/bin/python

def calc_interest(p, r, t):
    return (p * r * t)

def monthly_interest_payment(p, r, t):
    return (p * r * t / (t * 12))

def calc_simple_interest(p, r, t):
    return (p * (1 + r * t))


print('\nCase 1: ')
print(f'Monthly interest payment on $135,000 down: ${monthly_interest_payment(135_000, 0.089, 0.5)}')

total1 = 135_000 * 0.089 * 0.5 + calc_simple_interest(375_000, 0.05875, 30)
print(f'Total amount paid over the life of the loan: ${total1}', end='\n\n')

print('Case 2: ')
print(f'Monthly interest payment on $270,000 down: ${monthly_interest_payment(270_000, 0.089, 0.5)}')
total2 = 270_000 * 0.089 * 0.5 + calc_simple_interest(375_000, 0.0575, 30)
print(f'Total amount paid over the life of the loan: ${total2}', end='\n\n')

print(f'Difference between total amount paid: ${total1 - total2}')
