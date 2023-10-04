#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 10:04:12 2023

@author: matthew
"""

import pyperclip

question = input(
    "Enter the string to replace spaces with underscores "
    "(press enter to use clipboard contents): "
)

if len(question) == 0:
    spaced_string = pyperclip.paste()
else:
    spaced_string = question

print(f"String to replace spaces with underscores: {spaced_string}")

split_string = spaced_string.split(" ")

underscore_string = "_".join(split_string)

pyperclip.copy(underscore_string)

print(f"Done! New string: \n\n{underscore_string}")
