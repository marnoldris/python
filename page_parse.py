#!/usr/bin/python

import sys

number_strings = sys.argv[1].split(',')
pages = []

for s in number_strings:
    if '-' not in s:
        pages.append(int(s))
    else:
        interval = s.split('-')
        for i in range(2):
            interval.append(int(interval[i]))
        for i in range(2):
            del interval[0]
        start = min(interval)
        end = max(interval) + 1
        for i in range(start, end):
            pages.append(i)

pages = sorted(pages)

for i in range(len(pages)):
    pages[i] = pages[i] - 1
