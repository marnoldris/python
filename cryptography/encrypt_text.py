#!/usr/bin/python

from cryptor import encrypt
import sys

if len(sys.argv) == 1:
    file_name = input('Enter the desired name of the encrypted output file: ')
elif len(sys.argv) == 2:
    file_name = sys.argv[1]
else:
    print('Usage: encrypt_text.py or encrypt_text.py <filename>')
    exit()


text = bytes(input('Enter some text to encrypt: '), 'utf-8')

encrypted_text = encrypt(text)

with open(file_name, 'wb') as f:
    f.write(encrypted_text)
f.close()
