#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 21:50:26 2023

@author: bard
"""

import os
import sys
import time
import sevseg

seconds_left = int(sys.argv[1])

try:
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        hours = str(seconds_left // 3600)
        minutes = str((seconds_left % 3600) // 60)
        seconds = str(seconds_left % 60)
        
        h_digits = sevseg.get_sevseg_str(hours, 2)
        h_top_row, h_mid_row, h_bot_row = h_digits.splitlines()
        
        m_digits = sevseg.get_sevseg_str(minutes, 2)
        m_top_row, m_mid_row, m_bot_row = m_digits.splitlines()
        
        s_digits = sevseg.get_sevseg_str(seconds, 2)
        s_top_row, s_mid_row, s_bot_row = s_digits.splitlines()
        
        print(h_top_row + '     ' + m_top_row + '     ' + s_top_row)
        print(h_mid_row + '  *  ' + m_mid_row + '  *  ' + s_mid_row)
        print(h_bot_row + '  *  ' + m_bot_row + '  *  ' + s_bot_row)
        
        if seconds_left == 0:
            print()
            print('DONE!')
            break
        
        print()
        print('Press CTRL+C to quit...')
        
        time.sleep(1)
        seconds_left -= 1
except KeyboardInterrupt:
    sys.exit()
