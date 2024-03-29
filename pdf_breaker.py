#!/usr/bin/python

import PyPDF2
import os, sys
from time import sleep

home_dir = os.path.expanduser('~')

if len(sys.argv) < 2:
    print('Usage: pdf_breaker <optional -v> <encrypted pdf>')
    sys.exit()

if '-v' in sys.argv:
    verbose_flag = True
else:
    verbose_flag = False

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
for arg in sys.argv:
    if arg[0] == '-':
        continue
    else:
        pdf_file_name = arg
#pdfReader = PyPDF2.PdfReader(open(sys.argv[1], 'rb'))
pdfReader = PyPDF2.PdfReader(pdf_file_name, 'rb')

# Print a message warning that verbose has been selected, then count down
# to start.
if verbose_flag:
    print('Verbose flag detected, test words will be printed as they\'re '
          'used.'
    )
    sleep(0.3)
    print('Starting in 3...')
    sleep(1)
    print('            2...')
    sleep(1)
    print('            1...')
    sleep(1)

# Function to test the words with and without appended numbers
def try_word(word):
    if pdfReader.decrypt(word):
        print(f'Password is {word}')
        sys.exit
    for i in range(10):
        wordn = word + str(i)
        if pdfReader.decrypt(wordn):
            print(f'Password is {wordn}')
            sys.exit()
    for i in range(10):
        for j in range(10):
            wordnn = word + str(i) + str(j)
            if pdfReader.decrypt(wordnn):
                print(f'Password is {wordnn}')
                sys.exit()
    for i in range(10):
        for j in range(10):
            for k in range(10):
                wordnnn = word + str(i) + str(j) + str(k)
                if pdfReader.decrypt(wordnnn):
                    print(f'Password is {wordnnn}')
                    sys.exit()
        

# Start crackin'!
if pdfReader.isEncrypted:
    for word in test_words:
        # use lower(), upper(), and title()
        if verbose_flag:
            print(f'{word.lower()}   |   {word.upper()}   |   {word.title()}'
            )
        try_word(word.lower())
        try_word(word.upper())
        try_word(word.title())
        """
        if pdfReader.decrypt(word.lower()):
            print(f'Password is {word.lower()}')
            sys.exit()
        # print(word.upper()) if verbose_flag else None
        if pdfReader.decrypt(word.upper()):
            print(f'Password is {word.upper()}')
            sys.exit()
        if pdfReader.decrypt(word.title()):
            print(f'Password is {word.title()}')
            sys.exit()
        """

else:
    print(f'{sys.argv[1]} is not encrypted')

