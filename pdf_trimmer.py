#!/usr/bin/python

import os, sys, PyPDF2

# Check to make sure the user is running the program correctly
if len(sys.argv) != 3:
    print('Usage: pdf_trimmer <input pdf> <pages n,m,o-q,etc>\n\n'
          'Page numbers should be separated by a comma (no space)'
          ', can be duplicated, and will be kept in the order '
          'given.\n\n'
          'Ex.: $ pdf_trimmer long.pdf 1,3,3,5-8,2'
    )
    exit()

def parse_arg_nums(a):
    number_strings = sys.argv[a].split(',')
    nums = []

    for s in number_strings:
        if '-' not in s:
            nums.append(int(s))
        else:
            interval = s.split('-')
            # Change the strings into integers
            try:
                for i in range(2):
                    interval.append(int(interval[i]))            
            except ValueError:
                print('Negative indexing not supported, exiting...')
                exit()
            for i in range(2):
                del interval[0]
            start = min(interval)
            end = max(interval) + 1
            for i in range(start, end):
                nums.append(i)
    return nums

# Get the page number(s) to include
page_nums = parse_arg_nums(2)

# Subtract 1 to turn the page numbers into indices
for i in range(len(page_nums)):
    page_nums[i] = page_nums[i] - 1

end_page = max(page_nums)

# Split the file name on the file extension dot and append
# the trimmed page numbers, ending with the .pdf extension
output_name = f'{sys.argv[1].split(".")[0]}'
if len(page_nums) == 1:
    output_name = output_name + f'_page_{page_nums[0] + 1}.pdf'
elif len(page_nums) > 10:
    output_name = output_name + f'_trimmed.pdf'
else:
    output_name = output_name + '_pages_'
    for i in range(len(page_nums)):
        if i + 1 < len(page_nums):
            output_name = output_name + f'{page_nums[i] + 1}_'
        else:
            output_name = output_name + f'{page_nums[i] + 1}.pdf'

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
if (end_page + 1) > len(pdf_reader.pages):
    print('Requested page(s) are out of range, exiting...')
    exit()
for num in page_nums:
    if num < 0:
        print('Requested page(s) are out of range, exiting...')
        exit()

# Create the writer
pdf_writer = PyPDF2.PdfFileWriter()

# Copy the desired pages
for num in page_nums:
    page_obj = pdf_reader.pages[num]
    pdf_writer.add_page(page_obj)

# Open a blank pdf with the given file name and write the pages.
output_pdf = open(output_name, 'wb')
pdf_writer.write(output_pdf)
output_pdf.close()
print('Done!')
