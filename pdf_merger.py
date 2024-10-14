#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 16:22:58 2024

@author: matthew
"""

import PyPDF2
import sys


if len(sys.argv) < 3:
    print('Usage:\n pdf_merger.py <output file name> <pdf file names>'
          'Exiting...')
    sys.exit()


def combine_pdfs(output_name, *pdf_files):
    merger = PyPDF2.PdfMerger()

    for pdf in pdf_files:
        merger.append(pdf)

    with open(output_name, 'wb') as output_pdf:
        merger.write(output_pdf)


pdf_input_files = sys.argv[2:]
combine_pdfs(sys.argv[1], *pdf_input_files)
