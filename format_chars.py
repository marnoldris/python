
import os
import pdb

home_dir = os.path.expanduser('~')

try:
    ## Open the source file
    with open(
        #f'{home_dir}/Documents/language_program/hanzi_chars.csv',
        'hanzi_chars.csv',
        encoding='utf-8',
        ) as f:
        contents_list = f.readlines()
    ## Remove new line characters and whitespace from each line
    for line_num in range(len(contents_list)):
        contents_list[line_num] = contents_list[line_num].strip()
except FileNotFoundError as e:
    print('File not found, exiting...')
    exit()

## List to hold our modified data
modified_lines = []

## Split each line on the comma into a list 
## called split_line. Make the modifications 
## and append the new string to the list of 
## modified data.
for line_num in range(len(contents_list)):
    split_line = contents_list[line_num].split(',')
    new_line = f'"{split_line[0]} {split_line[1]}|{split_line[2]}"'
    modified_lines.append(new_line)

try:
    ## Write the modified data to a file.
    with open(
        #f'{home_dir}/Documents/language_program/output.txt',
        'output.txt',
        'w',
        encoding='utf-8',
        ) as f:
        ## write() requires a string, cannot use a list,
        ## so we join the list into a string on the
        ## new line character.
        f.write('\n'.join(modified_lines))
except Exception as e:
    print(e, type(e))

    
