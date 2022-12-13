name = 'ada lovelace'

print(name.title())

print(name.upper())

print(name.lower())


first_name = 'ada'
last_name = 'lovelace'
full_name = f'{first_name} {last_name}'     # this is an f-string

print(full_name)
print(f'Hello, {full_name.title()}!')

message = f'Hello, {full_name.title()}!'
print(message)


print('--------------------------------------------------')

# \t and \n count as whitespace, as well as spaces
name = '  \tArielle\n '
print(f'{name}')

print(f'{name.lstrip()}')   # lstrip() strips white space from the left
print(f'{name.rstrip()}')   # rstrip() strips white space from the right
print(f'{name.strip()}')    # strip() strips white space from both sides
