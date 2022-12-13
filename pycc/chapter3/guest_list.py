guests = ['Perrin', 'Arielle', 'James', 'Alivia']

print(f'{guests[0]} you are always welcome\n'\
    f'{guests[1]} of course\n'\
    f'{guests[2]} you and {guests[3]} are invited to dinner with us!')
print(f'{len(guests)}')


busyguest = 'James'
guests.remove(busyguest)
print(f'{busyguest} can no longer attend')
print(f'{len(guests)}')

guests.append('Dana')
print(f'{len(guests)}')

print(f'\n-----------------------\n')
print(f'{guests[0]} you are always welcome\n'\
    f'{guests[1]} of course\n'\
    f'{guests[3]} we would love to have you\n'\
    f'{guests[2]} you are invited to dinner with us!')

print(f'\n-----------------------\n')
print(f'We\'ve built a bigger table!')

guests.insert(0, 'Amanda')
guests.insert(3, 'Greg')
guests.append('Brad')
print(f'{len(guests)}')

print(f'{guests[1]} you are always welcome\n'\
    f'{guests[2]} of course\n'\
    f'{guests[3]} and {guests[5]} we would love to have you\n'\
    f'{guests[4]} you are invited to dinner with us!\n'\
    f'{guests[0]} you are also invited!')

print(f'\n-----------------------\n')
print(f'Welp, table broke :l')
print(f'{guests.pop()}, I am sorry, but we no longer have room')
print(f'{guests.pop()}, I am sorry, but we no longer have room')
print(f'{guests.pop()}, I am sorry, but we no longer have room')
print(f'{guests.pop()}, I am sorry, but we no longer have room')
print(f'{guests.pop()}, I am sorry, but we no longer have room')

print(f'{guests[1]} and {guests[0]} you are still invited!')

del guests[1]
del guests[0]
print(f'{len(guests)}')

print(f'{guests}')
