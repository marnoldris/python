#!/usr/bin/python

board = [
    ['a1','a2','a3'],
    ['b1','b2','b3'],
    ['c1','c2','c3'],
    ]

def print_board():
    row_number = 0
    column_number = 0
    for row in board:
        for j in row:
            if j == 'X':
                print('X', end='')
            elif j == 'O':
                print('O', end='')
            else:
                print(' ', end='')
            if column_number < 2:
                print('|', end='')
                column_number += 1
            elif row_number < 2:
                # When we get here, we know we're at the end of the
                # row so we need to reset columns to zero and add
                # one to row_number.
                print('\n-+-+-')
                column_number = 0
                row_number += 1
    print(end='\n\n')

def print_instruction_board():
    for i in board:
        print(i)

def replace_value(old, new):
    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] == old:
                board[row][column] = new
                break    # break us out of the for loop once we find the target
                
print_instruction_board()

turn = 'X'
for i in range(9):
    move = input(f'Turn {turn}: ')
    replace_value(move, turn)
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    print_board()
