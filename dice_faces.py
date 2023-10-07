#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 21:20:51 2023

@author: matthew
"""
UL = chr(9484)
UR = chr(9488)
BL = chr(9492)
BR = chr(9496)
H = chr(9472)
V = chr(9474)
C = chr(9532)
CL = chr(9500)
CR = chr(9508)
P = chr(9679)

def print_dice(dice):
    return '\n'.join(dice)

dice = {
        'd6-1': [
            UL+    H*7    +UR,
            V+  '       '  +V,
            V+'   '+P+'   '+V,
            V+  '       '  +V,
            BL+    H*7    +BR,
            ],
        'd6-2a': [
            UL+    H*7    +UR,
            V+'     '+P+' '+V,
            V+  '       '  +V,
            V+' '+P+'     '+V,
            BL+    H*7    +BR,
            ],
        'd6-2b': [
            UL+    H*7    +UR,
            V+' '+P+'     '+V,
            V+  '       '  +V,
            V+'     '+P+' '+V,
            BL+    H*7    +BR,
            ],
        'd6-3a': [
            UL+    H*7    +UR,
            V+'     '+P+' '+V,
            V+'   '+P+'   '+V,
            V+' '+P+'     '+V,
            BL+    H*7    +BR,
            ],
        'd6-3b': [
            UL+    H*7    +UR,
            V+' '+P+'     '+V,
            V+'   '+P+'   '+V,
            V+'     '+P+' '+V,
            BL+    H*7    +BR,
            ],
        'd6-4': [
            UL+      H*7      +UR,
            V+' '+P+'   '+P+' '+V,
            V+    '       '    +V,
            V+' '+P+'   '+P+' '+V,
            BL+      H*7      +BR,
            ],
        'd6-5': [
            UL+      H*7      +UR,
            V+' '+P+'   '+P+' '+V,
            V+  '   '+P+'   '  +V,
            V+' '+P+'   '+P+' '+V,
            BL+      H*7      +BR,
            ],
        'd6-6': [
            UL+      H*7      +UR,
            V+' '+P+'   '+P+' '+V,
            V+' '+P+'   '+P+' '+V,
            V+' '+P+'   '+P+' '+V,
            BL+      H*7      +BR,
            ],
        }

if __name__ == "__main__":
    for k, v in dice.items():
        print(print_dice(dice[k]))
        #print(print_dice(v))
