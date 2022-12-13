names = ['Arielle', 'James', 'Alivia', 'Brittany']

print(f'{names[0]}\n{names[1]}\n{names[2]}\n{names[3]}')


message = 'Hello to you'
# note the terminated quote and line break character \ at char 76
print(f'{message} {names[0]}\n{message} {names[1]}\n{message} {names[2]}\n'\
    f'{message} {names[3]}')    # f' picks up again here, after the indent


print(f'-----------------------------------')

cars = ['Forester',
    'Ascent',
    'Land Cruiser']

print(f'I really like driving our {cars[0]}')
print(f'I love what we can do as a family in our {cars[1]}')
print(f'I would like to own another {cars[2]} some day, maybe an electric one')

print(f'-----------------------------------')

school = ['Boise State']

school.append('Riverstone')    # append() can only add one thing at a time
print(f'{school}')
