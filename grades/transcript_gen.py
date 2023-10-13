#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 11:00:54 2023

@author: matthew
"""

import sys
import os
import csv
import re
import traceback

VERSION = 1.2

#%% TODO
"""
Parse args to ensure proper number, print message and quit if not.
sys.argv[1] should be Report Name
sys.argv[2] is input file
sys.argv[3] is output file

Trim headers
Parse line 3 for programme, academic year, academic term

concat student email, programme, academic year, academic term, report name, subject group, class name, class grade, term grade, local grade, credit, level

build output
write output to file
"""        

#%% Functions
#%%% Email generator
def email_gen(name) -> str:
    """ Generate an email address from a given name string. """
    
    # Strip the nickname in parentheses
    pattern = re.compile(r'\(.+\)\s')
    """
    The \( and \) match opening and closing parentheses.
    .* matches any number of any characters.
    The \s matches a space
    """
    name_subbed = pattern.sub('', name)
    #name_subbed = re.sub(pattern, '', name)
    
    # RE for the I II III IV V VI VII etc cases?
    # Split the name so it can be cleaned up and reassembled
    name_parts = name_subbed.split(' ')
    
    for i in range(len(name_parts)):
        if name_parts[i] == '|':
            del name_parts[i:]
            break
    
    name_parts_copy = name_parts[:]
    
    # Special case for Fiona Van De Graff
    if len(name_parts) == 4:
        first_name = name_parts[0]
        last_name = ''.join(name_parts[1:])
    else:
        first_name = ''.join(name_parts[:-1])
        last_name = name_parts[-1]
        
    email = first_name.lower() + '.' + last_name.lower() + '@riverstoneschool.org'
    
    return email

#%%% Parse parentheses
def parse_parens(s) -> str:
    """ Parse out a string from between parentheses, exclusive """
    pattern = re.compile(r'\((.+)\)')
    """
    The \( and \) match opening and closing parentheses.
    The ( ) group the result, removing the parentheses themselves (the stuff
    between the ( ) is what we want, not the matched characters around it).
    .* matches any number of any characters
    """
    matches = pattern.findall(s)
    return matches[0]

#%%% Parse classes
def parse_class_name(s) -> str:
    
    class_finder = re.compile(r'\w+\s\w+\s([A-Za-z\s]+)(X|Y|\d)')
    mo = class_finder.search(s)    
    try:
        class_name = mo.group()
        class_subname = mo.group(1)
        if 'HUM' in class_name:
            hum = re.compile(r'HUM')
            class_name = hum.sub('Integrated Humanities', mo.group())
        elif 'PE' in class_name:
            pe = re.compile(r'PE')
            class_name = pe.sub('Physical Education', mo.group())
        elif 'DT' in class_name:
            dt = re.compile(r'DT')
            class_name = dt.sub('Design Technology', mo.group())
        
        # Check for the case of no space between the class name and number
        no_space = re.compile(r'n(\d)')
        no_space_mo = no_space.search(class_name)
        if no_space_mo:
            class_name = no_space.sub(f'n {no_space_mo.group(1)}', class_name)

            
    except AttributeError:
        traceback.print_exc()
        print('\n\nMatch not found, please report this issue.\n'
              'Exiting...')
        sys.exit()
    return class_name

#%%% Calculate local grade
def calc_local_grade(l) -> str:
    if 'N/A' in l[13]:
        return 'N/A'
    if 'INC' in l[13]:
        return 'Incomplete'
    try:
        a = int(l[12])
    except ValueError:
        traceback.print_exc()
        print('\n\nInvalid local grade, please report this error.\n'
              'Exiting...')
        sys.exit()
    if 'PE' in l[0] or 'Physical' in l[0]:
        if a >= 3:
            return 'PASS'
        else:
            return 'FAIL'
    if a <= 5:
        local_grade = 'F'
    elif a <= 9:
        local_grade = 'D'
    elif a == 10:
        local_grade = 'C-'
    elif a <= 12:
        local_grade = 'C'
    elif a <= 14:
        local_grade = 'C+'
    elif a <= 16:
        local_grade = 'B-'
    elif a <= 18:
        local_grade = 'B'
    elif a <= 20:
        local_grade = 'B+'
    elif a <= 23:
        local_grade = 'A-'
    elif a <= 30:
        local_grade = 'A'
    elif a > 30:
        local_grade = 'A+'
    return local_grade

#%%% Calculate grade level
def calc_grade_level(l) -> str:
    # *5 is 10th grade, add 5 to * level
    # if 11th & 12th, its just 11 and 12
    #programme_filter = re.compile(r'w\+\s(\w+)')
    #mo = programme_filter.search(l[0])
    if 'DP' in l[0]:
        return 'Grade ' + l[5]
    elif 'MYP' in l[0]:
        num_filter = re.compile('\d')
        mo = num_filter.search(l[5])
        grade = int(mo.group()) + 5
        grade_level = str(grade)
        return 'Grade ' + grade_level
    

#%%% Read in the csv
def read_csv(in_file) -> list[list[str]]:
    rows = []
    
    try:
        with open(in_file) as csv_file:
            reader = csv.reader(csv_file, delimiter=',', quotechar='"')
            for row in reader:
                rows.append(row)
    except FileNotFoundError:
        traceback.print_exc()
        print('\n\nFile not found!')
        sys.exit()
    
    return rows
#%% Handle args

if len(sys.argv) >= 2:
    if sys.argv[1] == '--version' or sys.argv[1] == '-v':
        print(f'Version: {VERSION}')
        sys.exit()

if len(sys.argv) > 1 and len(sys.argv) < 4:
    print('Invalid arguments. Usage:\n'
          '$ transcript_gen.py\n'
          'or\n'
          '$ transcript_gen.py report_name input_file.csv output_file.csv\n'
          'Contact Matthew with questions.\n'
          'Exiting...'
    )
    sys.exit()
if len(sys.argv) == 4:
    report_name = sys.argv[1]
    input_file = sys.argv[2]
    output_file = sys.argv[3]
else:
    print('Please enter a name for your report:')
    report_name = input('> ').strip()
    
    print('Please enter the input file name:')
    input_file = input('> ').strip()
    
    print('Please enter the output file name:')
    output_file = input('> ').strip()

#%% Read in the csv and make a trimmed version

rows = read_csv(input_file)
rows_trimmed = []
for i in range(len(rows)):
    #current_row = rows[i]
    if rows[i][0] == 'Term Grades':
        continue
    if rows[i][0].startswith('Riverstone International'):
        continue
    if rows[i][0].startswith('Class Name'):
        continue
    if i == 2:
        # Parse data from row 3 then trim it
        if 'IB Middle' in rows[i][0]:
            programme = 'IB MYP'
        else:
            programme = 'IB DP'
        if 'First Semester' in rows[i][0]:
            academic_term = 'First Semester'
        else:
            academic_term = 'Second Semester'
        year = parse_parens(rows[i][0])
        continue
    
    rows_trimmed.append(rows[i])

#%% Build the output file
output = [
    [
    'Student email', 'Programme', 'Academic Year', 'Academic Term',
    'Report Name', 'Subject Group', 'Class Name', 'Class Grade',
    'Term Grade', 'Local Grade', 'Credit', 'Level'
    ]
]
emails = []
for row in rows_trimmed:
    if row[0] and not row[3]:   # Row contains only a name
        email = email_gen(row[0])
        emails.append(email)
    elif not row[0]:            # Row is empty
        continue
    else:
        output.append([
            email, programme, year, academic_term, report_name,
            row[3], parse_class_name(row[0]),
            calc_grade_level(row), row[13],
            calc_local_grade(row), '', ''
        ])
        

#%% Write output
with open(output_file, 'w') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerows(output)
