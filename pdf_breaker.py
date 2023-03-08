#!/usr/bin/python

import PyPDF2
import os, sys

home_dir = os.path.expanduser('~')

if len(sys.argv) != 2:
    print('Usage: pdf_breaker <encrypted pdf>')
    sys.exit()

# open the dictionary file
if os.path.exists('dictionary.txt'):
    dict_file = open('dictionary.txt')
else:
    dict_file = open(f'{home_dir}/Documents/dictionary.txt')
dict_words = dict_file.readlines()
dict_file.close()

test_words = []
for word in dict_words:
    test_words.append(word.strip())

# open pdf file
pdfReader = PyPDF2.PdfFileReader(open(sys.argv[1], 'rb'))

if pdfReader.isEncrypted:
    for word in test_words:
        # use lower(), upper(), and title()
        if pdfReader.decrypt(word.lower()):
            print(f'Password is {word.lower()}')
            sys.exit()
        if pdfReader.decrypt(word.upper()):
            print(f'Password is {word.upper()}')
            sys.exit()
        if pdfReader.decrypt(word.title()):
            print(f'Password is {word.title()}')
            sys.exit()

else:
    print(f'{sys.argv[1]} is not encrypted')

