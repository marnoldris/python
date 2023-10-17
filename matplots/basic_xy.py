#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 10:49:25 2023

@author: matthew
"""

import matplotlib.pyplot as plt

X_POS_LIM = 10
X_NEG_LIM = -10
Y_POS_LIM = 10
Y_NEG_LIM = -10

fig, ax = plt.subplots()

ax.set_xlabel('x')
ax.set_ylabel('y')

ax.set_xticks(range(X_NEG_LIM, X_POS_LIM + 1, 1))
ax.set_yticks(range(Y_NEG_LIM, Y_POS_LIM + 1, 1))

plt.xlim([X_NEG_LIM, X_POS_LIM])
plt.ylim([Y_NEG_LIM, Y_POS_LIM])

plt.grid(True)
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')

plt.show()
