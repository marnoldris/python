#!/usr/bin/python

import os

board = {'1': ' ', '2': ' ', '3': ' ',
         '4': ' ', '5': ' ', '6': ' ',
         '7': ' ', '8': ' ', '9': ' ',
        }

UL = chr(9484)
UR = chr(9488)
BL = chr(9492)
BR = chr(9496)
H = chr(9472)
V = chr(9474)
C = chr(9532)
CL = chr(9500)
CR = chr(9508)

"""
def print_board(board):
    print()
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
"""
"""
def print_board(board):
    print()
    print(board['top-L'] + V + board['top-M'] + V + board['top-R'])
    print(H + C + H + C + H)
    print(board['mid-L'] + V + board['mid-M'] + V + board['mid-R'])
    print(H + C + H + C + H)
    print(board['low-L'] + V + board['low-M'] + V + board['low-R'])
"""
def print_board(board):
    print()
    print(UL + H*5 + UR)
    print(V + board['1'] + V + board['2'] + V + board['3'] + V +
          '     1 2 3')
    print(CL + H + C + H + C + H + CR)
    print(V + board['4'] + V + board['5'] + V + board['6'] + V +
          '     4 5 6')
    print(CL + H + C + H + C + H + CR)
    print(V + board['7'] + V + board['8'] + V + board['9'] + V +
          '     7 8 9')
    print(BL + H*5 + BR)

def check_win():
    return ((board['1'] == board['2'] == board['3'] != ' ') or
            (board['4'] == board['5'] == board['6'] != ' ') or
            (board['7'] == board['8'] == board['9'] != ' ') or
            (board['1'] == board['4'] == board['7'] != ' ') or
            (board['2'] == board['5'] == board['8'] != ' ') or
            (board['3'] == board['6'] == board['9'] != ' ') or
            (board['3'] == board['5'] == board['7'] != ' ') or
            (board['1'] == board['5'] == board['9'] != ' ')
            )

print('\n\n\n')

counter = 0
win = False
x_win = False
o_win = False
turn = 'X'

while counter < 9 and win == False:
    os.system('cls' if os.name == 'nt' else 'clear')
    print_board(board)
    print('Turn for ' + turn + '. Move on which space? (1-9)')
    move = input('> ')
    move_int = int(move)
    while move_int < 1 or move_int > 9 or board[move] != ' ':
        print('Invalid entry, try again (1-9)')
        move = input('> ')
        move_int = int(move)
    board[move] = turn
    win = check_win()
    counter += 1
    if turn == 'X':
        if win:
            x_win = True
            continue
        turn = 'O'
    else:
        if win:
            o_win = True
            continue
        turn = 'X'
print('\nGame over!')
if x_win:
    print('X wins! :D')
elif o_win:
    print('O wins! :D')
else:
    print('Draw :(')
print_board(board)
