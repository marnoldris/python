#!/usr/bin/python

import pyautogui
from time import sleep

# Insert a little buffer so keys can be physically un-pressed
sleep(0.2)

# Make sure the hotkeys used to trigger the script are not pressed
pyautogui.keyUp('winleft')
pyautogui.keyUp('shiftleft')
pyautogui.keyUp('ctrlleft')
pyautogui.keyUp('f')

# Click the dropdown
pyautogui.click(468,121, duration=0.1)


# Click to select the text
pyautogui.click(468,285, duration=0.1)

# Send ctrl+[
sleep(0.1)
pyautogui.hotkey('ctrl','[')
