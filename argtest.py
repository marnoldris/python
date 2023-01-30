#!/usr/bin/python

import sys

"""
Simple test program for parsing arguments.
"""

def print_args():
    """ Simple function to print arguments """
    for arg in sys.argv[1:]:
        print(arg)
