#!/usr/bin/python

"""
Simple program to add four spaces and a dash to the beginning 
of each line in the clipboard
"""

import pyperclip

text = pyperclip.paste()

lines = text.split('\n')


question = input('Would you like to remove blank lines? (Y/n): ')

# Remove blank lines if requested
if question == '' or question == 'Y' or question == 'y':
    for line in lines:
        if line == '':
            lines.remove('')


# Add the modifications to each line
for i in range(len(lines)):
    if lines[i] == '':
        continue
    else:
        lines[i] = '    - ' + lines[i]

# Join the lines
text = '\n'.join(lines)

pyperclip.copy(text)

print('Done!')
