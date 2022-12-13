places = ['British Columbia',
    'Lochsa River',
    'New Zealand',
    'Australia',
    'Saskatchewan']

print(f'Original:\n{places}\n')
print(f'temp sorted:\n{sorted(places)}\n')  # temporarily sorts the list
                            # note this is a function, not a method
print(f'temp reverse sorted:\n{sorted(places,reverse=True)}\n')
                            # temp sorts in reverse order
print(f'Original:\n{places}\n')

places.reverse()    # permanently reverses the list
print(f'Reversed:\n{places}\n')

places.reverse()
print(f'Un-reversed:\n{places}\n')

places.sort()   # permanently sorts the list alphabetically
                # note that this is a method
print(f'Permanently sorted:\n{places}\n')

places.sort(reverse=True)
print(f'Permamently reverse sorted:\n{places}\n')

print(f'------------------------')
