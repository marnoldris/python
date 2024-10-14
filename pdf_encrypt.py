#!/usr/bin/python

import os
import sys
import PyPDF2

# %% Checking for args
if len(sys.argv) != 3:
    print("Usage: pdf_encrypt <unencrypted pdf> <password>")
    sys.exit()
# %% Finding the home path
home_dir = os.path.expanduser("~")

# %% Set up the output name
# Split the file name on the file extension dot and append
# _enc.pdf in its place
output = f'{sys.argv[1].split(".")[0]}' + "_enc.pdf"

# %% Check if the file exists and asking to overwrite
yes_values = ["", "Y", "y"]
if os.path.exists(output):
    cont = input("Encrypted filename already exists, overwrite? (Y/n): ")
    if cont in yes_values:
        print("Overwriting...")
    else:
        print("Cancelling...")
        sys.exit()

# %% Open the source file and set up the reader
pdfFile = open(sys.argv[1], "rb")
pdfReader = PyPDF2.PdfReader(pdfFile)
pdfWriter = PyPDF2.PdfWriter()

# %% Build the new, encrypted PDF
for page in pdfReader.pages:
    pdfWriter.add_page(page)

# %% Write the encrypted PDF
pdfWriter.encrypt(sys.argv[2])

enc_pdf = open(output, "wb")
pdfWriter.write(enc_pdf)
enc_pdf.close()

# %% Huzzah!
print("Done!")
