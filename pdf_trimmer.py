#!/usr/bin/python

import os
import sys
import re
import PyPDF2

# Check to make sure the user is running the program correctly
if len(sys.argv) != 3:
    print(
        "Usage: pdf_trimmer <input pdf> <pages n,m,o-q,etc>\n\n"
        "Page numbers should be separated by a comma (no space)"
        ", can be duplicated, and will be kept in the order "
        "given.\n\n"
        "Ex.: $ pdf_trimmer long.pdf 1,3,3,5-8,2\n\n"
        "To copy all pages, use all instead of page numbers."
    )
    sys.exit()
test_name = sys.argv[1]

def parse_arg_nums(a):
    number_strings = sys.argv[a].split(",")
    nums = []

    for s in number_strings:
        if "-" not in s:
            nums.append(int(s))
        else:
            interval = s.split("-")
            # Change the strings into integers
            try:
                for i in range(2):
                    interval.append(int(interval[i]))
            except ValueError:
                print("Negative indexing not supported, exiting...")
                sys.exit()
            for i in range(2):
                del interval[0]
            start = min(interval)
            end = max(interval) + 1
            for i in range(start, end):
                nums.append(i)
    return nums

def name_output() -> str:
    filename_filter = re.compile(r'([^/]+)(\.pdf)')
    mo = filename_filter.search(sys.argv[1])
    if mo:
        original_name = mo.group(1)
    else:
        print('File name not found. Exiting...')
        sys.exit()
    if len(page_nums) == 1:
        output_name = '_'.join([
            original_name,
            'page',
            str(page_nums[0] + 1),
            ])
        output_name = ''.join([output_name, '.pdf'])
    elif len(page_nums) > 10:
        output_name = '_'.join([original_name, 'trimmed.pdf'])
    else:
        outputs = [original_name, 'pages',]
        for i in range(len(page_nums)):
            outputs.append(str(page_nums[i] + 1))
        output_name = '_'.join(outputs)
        output_name = ''.join([output_name, '.pdf'])
    
    return output_name


# Open the original pdf and create the reader
try:
    pdf_reader = PyPDF2.PdfReader(sys.argv[1], "rb")
except FileNotFoundError:
    print('File not found! Exiting...')
    sys.exit()

# Check for encryption, ask for password if so
if pdf_reader.is_encrypted:
    password = input("Encryption detected, please enter the password: ")
    pdf_reader.decrypt(password)


# Get the page number(s) to include
if sys.argv[2] == "all":
    page_nums = [i for i in range(len(pdf_reader.pages))]
else:
    page_nums = parse_arg_nums(2)
    # Subtract 1 to turn the page numbers into indices
    for i in range(len(page_nums)):
        page_nums[i] = page_nums[i] - 1

end_page = max(page_nums)

# Synthesize the output file name
output_name = name_output()

# Check to see if the file exists, confirm overwrite if it does
if os.path.exists(output_name):
    cont = input("Trimmed filename already exists, overwrite? (Y/n)")
    if cont == "" or cont == "y" or cont == "Y":
        print("Overwriting...")
    else:
        print("Cancelling...")
        sys.exit()

# Make sure the requested pages exist in the original PDF
if (end_page + 1) > len(pdf_reader.pages):
    print("Requested page(s) are out of range, exiting... (upper bound)")
    sys.exit()
for num in page_nums:
    if num < 0:
        print("Requested page(s) are out of range, exiting... (lower bound)")
        sys.exit()

# Create the writer
pdf_writer = PyPDF2.PdfWriter()

# Copy the desired pages
for num in page_nums:
    page_obj = pdf_reader.pages[num]
    pdf_writer.add_page(page_obj)

# Open a blank pdf with the given file name and write the pages.
output_pdf = open(output_name, "wb")
pdf_writer.write(output_pdf)
output_pdf.close()
print("Done!")
