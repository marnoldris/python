user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }

for key, value in user_0.items():    # could use k, v instead of key, value
    print(f'\nKey: {key}')
    print(f'Value: {value}')

for key in user_0.keys():    # this is the default behavior, without .keys() 
    print(f'\nKey: {key}')

print(f'\n\n')

for key in user_0:
    print(f'{user_0[key]}')
