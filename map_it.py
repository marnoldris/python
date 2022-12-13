#!/usr/bin/python
"""
Reads an address from command line args or clipboard, then
launches Google Maps in a browser with that address.
"""
import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    # Get the address from the args
    address = ' '.join(sys.argv[1:]) # this is smart
else:
    # Get the address from the clipboard
    address = pyperclip.paste()

webbrowser.open(f'https://www.google.com/maps/place/{address}')
