"""
Practice working with lists of numbers and
number operations
"""

# 4-3 Counting to 20
for number in range(1,21):
    print(number)

# 4-4 One Million
million_nums = list(range(1,1_000_001))
print(million_nums)

# 4-5 Summing a Million
print(f'{min(million_nums)}\n'
      f'{max(million_nums)}\n'
      f'{sum(million_nums)}')

# 4-6 Odd Numbers
odd_nums = list(range(1,20,2))
for number in odd_nums:
    print(number)

# 4-7 Threes
threes = list(range(3,31,3))
for number in threes:
    print(number)

# 4-8 Cubes
cubes = [value**3 for value in range(1,11)]
for number in cubes:
    print(number)

# 4-10
print(f'The first three numbers in the list of cubes are: {cubes[:3]}')
print(f'Three numbers from the middle of the list of cubes are: '
      f'{cubes[4:7]}')
print(f'The last three numbers in the list of cubes are: {cubes[-3:]}')
