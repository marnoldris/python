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

#%% Static variables
VERSION = 1.2
SUBJECT_INDEX = 3       # 3
CLASS_NAME_INDEX = 0    # 0
FINAL_GRADE_INDEX = 13  # 13
SUM_INDEX = 12          # 12
GRADE_LEVEL_INDEX = 5   # 5     

#%% Functions
#%%% Email generator
def email_gen(name) -> str:
    """ Generate an email address from a given name string. """
    
    # Strip the nickname in parentheses
    pattern = re.compile(r'\(.+\)\s')
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
    if 'N/A' in l[FINAL_GRADE_INDEX]:
        return 'N/A'
    if 'INC' in l[FINAL_GRADE_INDEX]:
        return 'Incomplete'
    try:
        a = int(l[SUM_INDEX])
    except ValueError:
        traceback.print_exc()
        print('\n\nInvalid local grade, please report this error.\n'
              'Exiting...')
        sys.exit()
    if 'PE' in l[CLASS_NAME_INDEX] or 'Physical' in l[CLASS_NAME_INDEX]:
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
    if 'DP' in l[CLASS_NAME_INDEX]:
        return 'Grade ' + l[GRADE_LEVEL_INDEX]
    elif 'MYP' in l[CLASS_NAME_INDEX]:
        num_filter = re.compile(r'\d')
        mo = num_filter.search(l[GRADE_LEVEL_INDEX])
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
        print('\n\nFile not found! Exiting...')
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

#%% Assign indices
for i in range(len(rows)):
    for j in range(len(rows[i])):
        current = rows[i][j]
        if current.lower() == 'subject':
            if j != SUBJECT_INDEX:
                print(f'Subject index changed to {j}')
                SUBJECT_INDEX = j
        elif current.lower() == 'class name':
            if j != CLASS_NAME_INDEX:
                print(f'Class name index changed to {j}')
                CLASS_NAME_INDEX = j
        elif current.lower() == 'final grade':
            if j != FINAL_GRADE_INDEX:
                print(f'Final grade index changed to {j}')
                FINAL_GRADE_INDEX = j
        elif current.lower() == 'sum':
            if j != SUM_INDEX:
                print(f'Sum index changed to {j}')
                SUM_INDEX = j
        elif current.lower() == 'grade level':
            if j != GRADE_LEVEL_INDEX:
                print(f'Grade level index changed to {j}')
                GRADE_LEVEL_INDEX = j
            
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
            row[SUBJECT_INDEX], parse_class_name(row[CLASS_NAME_INDEX]),
            calc_grade_level(row), row[FINAL_GRADE_INDEX],
            calc_local_grade(row), '', ''
        ])
        

#%% Write output
with open(output_file, 'w') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerows(output)
