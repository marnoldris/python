
"""
Write a program that utilizes a 2D list to store information.
The information should be modified via a function that takes
a two member tuple (x, y coordinates) and changes the value
at that location. You will also need a function to print
the 2D list.
"""

def add_data(multid_list, coords, value):
    x_value = coords[0]
    y_value = coords[1]
    multid_list[y_value][x_value] = value
    for i in range(len(multid_list[y_value])):
        for j in range(len(multid_list[i])):
            print(multid_list[i][j],end='')
        print()

array_board = [
    ['-','-','-'],
    ['-','-','-'],
    ['-','-','-'],
    ]

add_data(array_board, (2, 1), 'x')
