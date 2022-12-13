#!/usr/bin/python

import os, sys
import PyPDF2

if len(sys.argv) != 3:
    print('Usage: pdf_encrypt <unencrypted pdf> <password>')
    exit()

home_dir = os.path.expanduser('~')

# Split the file name on the file extension dot and append
# _enc.pdf in its place
output = f'{sys.argv[1].split(".")[0]}' + '_enc.pdf'
if os.path.exists(output):
    cont = input('Encrypted filename already exists, overwrite? (Y/n)')
    if cont == '' or cont == 'y' or cont == 'Y':
        print('Overwriting...')
    else:
        print('Cancelling...')
        exit()

pdfFile = open(sys.argv[1], 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
pdfWriter = PyPDF2.PdfFileWriter()

for page_num in range(pdfReader.numPages):
    pdfWriter.addPage(pdfReader.getPage(page_num))

pdfWriter.encrypt(sys.argv[2])

enc_pdf = open(output, 'wb')
pdfWriter.write(enc_pdf)
enc_pdf.close()
