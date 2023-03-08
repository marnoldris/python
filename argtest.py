#!/usr/bin/python

import sys

"""
Simple test program for parsing arguments.
"""

def print_args():
    """ Simple function to print arguments """
    counter = 0
    for arg in sys.argv[1:]:
        counter += 1
        print(arg)
        print(counter)

print_args()
