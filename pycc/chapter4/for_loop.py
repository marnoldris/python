people = ['perrin','arielle','matthew'] # better to work with all lower case

for i in people:
    print(i)

"""
Note that this prints the value at the index, instead of 
requiring list[index]. The value of the index is not
explicitly needed or used. It would likely be better
to choose a meaningful singular for the list of plurals
such as `for person in people:`

To get the indices, use range() and len(), like so
`for i in range(len(itemlist)):`
"""

for person in people:
    print(f'{person.title()} you are amazing!')
    print(f'{person.title()} I love you very much\n')
    for person in people:
        print(':)')
print('Yay!')
