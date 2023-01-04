#!/usr/bin/python

from cryptor import decrypt
import sys

if len(sys.argv) == 1:
    file_name = input('Enter the full file name to decrypt: ')
elif len(sys.argv) == 2:
    file_name = sys.argv[1]
else:
    print('Usage: decrypt_text.py or decrypt_text.py <filename>')
    exit()

with open(file_name, 'rb') as f:
    encrypted = f.read()

print('Decrypting text...')

output = decrypt(encrypted)
output = output.decode('utf-8')

print(output)

with open('decrypted.txt', 'w') as f:
    f.write(output)
    f.write('\n')

print('Done!')
