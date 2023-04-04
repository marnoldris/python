#!/usr/bin/python

import dice

d12 = dice.Dice()

print(d12.get_value())
print(d12.roll())

for i in range(70):
    print(d12.roll())

d100 = dice.Dice(100)
print(d100.roll())
