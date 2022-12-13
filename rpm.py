#!/usr/bin/python

n1 = int(input('Enter an integer: '))
n2 = int(input('Enter an integer to multiply by: '))

halving = [n1]
while(min(halving) > 1):
    halving.append(min(halving) // 2)

doubling = [n2]
while len(doubling) < len(halving):
    doubling.append(max(doubling) * 2)

for i in range(len(halving)):
    if halving[i] % 2 == 0:
       doubling[i] = 0 

print(sum(doubling))
