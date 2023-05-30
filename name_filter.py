#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 25 08:58:52 2023

Program that takes a plain text file and filters out names, replacing them
with <name>

@author: matthew
"""

import sys
import string

punctuation = list(string.punctuation)

# %% Open the file
try:
    with open(sys.argv[1]) as f:
        name_list = [line.rstrip().title() for line in f.readlines()]
    with open(sys.argv[2]) as f:
        contents_list = f.readlines()
except (FileNotFoundError, IndexError) as e:
    if isinstance(e, FileNotFoundError):
        print("File not found, double check the name and try again.")
    elif isinstance(e, IndexError):
        print("Please include a file name.")
    sys.exit()

# %% Compare each word to the name list and change to <name> if matched.

anonymized_list = []

for line in contents_list:
    new_line = []
    for word in line.split(" "):
        word_stripped = word.strip()
        if (len(word_stripped) > 1 and word_stripped[-1] in punctuation):
            word_trimmed = word_stripped[:-1]
            if word_trimmed in name_list:
                new_line.append(f"<name>{word_stripped[-1]}")
            else:
                new_line.append(word)
        elif word_stripped in name_list:
            new_line.append("<name>")
        else:
            new_line.append(word)
    anonymized_list.append(" ".join(new_line))


# %% Write the output file

with open("anonymized.txt", "w") as f:
    f.write(''.join(anonymized_list))
