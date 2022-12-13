#!/usr/bin/python

import os, sys, PyPDF2

# Check to make sure the user is running the program correctly
if len(sys.argv) < 3:
    print('Usage: pdf_trimmer <input pdf> <pages n-m>')
    exit()

# we could split on commas, then for each element in the list,
# split on - if there is one, appending range(first,last) to
# the list. Then our page function would just need to loop through
# every element in the list, using its value as the page to add
# Get the page number(s) to include
pages = sys.argv[2].split("-")
start_page = int(min(pages)) - 1
end_page = int(max(pages))

# Split the file name on the file extension dot and append
# the trimmed page numbers, ending with the .pdf extension
if len(pages) == 1:
    output_name = f'{sys.argv[1].split(".")[0]}' + f'_page_{pages[0]}.pdf'
else:
    output_name = f'{sys.argv[1].split(".")[0]}' + f'_pages_{pages[0]}-{end_page}.pdf'

# Check to see if the file exists, confirm overwrite if it does
if os.path.exists(output_name):
    cont = input('Trimmed filename already exists, overwrite? (Y/n)')
    if cont == '' or cont == 'y' or cont == 'Y':
        print('Overwriting...')
    else:
        print('Cancelling...')
        exit()

# Open the original pdf and create the reader
orig_pdf = open(sys.argv[1], 'rb')
pdf_reader = PyPDF2.PdfFileReader(orig_pdf)

# Make sure the requested pages exist in the original PDF
if end_page > pdf_reader.numPages:
    print('Requested page(s) are out of range, exiting...')
    exit()

# Create the writer
pdf_writer = PyPDF2.PdfFileWriter()

# Copy the desired pages
if len(pages) == 1:
    # just copy one page
    page_obj = pdf_reader.getPage(start_page)
    pdf_writer.addPage(page_obj)
else:
    # copy pages from start_page to end_page
    for i in range(start_page, end_page):
        page_obj = pdf_reader.getPage(i)
        pdf_writer.addPage(page_obj)

# Open a blank pdf with the given file name and write the pages.
output_pdf = open(output_name, 'wb')
pdf_writer.write(output_pdf)
output_pdf.close()
print('Done!')
