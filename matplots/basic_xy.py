#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 10:49:25 2023

@author: matthew
"""

import matplotlib.pyplot as plt

X_POS_LIM = 15
X_NEG_LIM = -15
Y_POS_LIM = 15
Y_NEG_LIM = -15

fig, ax = plt.subplots(figsize=(12, 10))

ax.set_xlabel('x', fontsize=21)
ax.set_ylabel('y', rotation=0, fontsize=21)

ax.get_yaxis().set_label_coords(-0.03,0.48)

# Remove labels
ax.set_xticklabels([])
ax.set_yticklabels([])

ax.set_xticks(range(X_NEG_LIM, X_POS_LIM + 1, 1))
ax.set_yticks(range(Y_NEG_LIM, Y_POS_LIM + 1, 1))

plt.xlim([X_NEG_LIM, X_POS_LIM])
plt.ylim([Y_NEG_LIM, Y_POS_LIM])

plt.grid(True)

plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')

plt.show()
