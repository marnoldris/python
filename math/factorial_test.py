
numbers = [5, 4, 3, 2, 1]

output = numbers[0]

for i in range(len(numbers) - 1):
    output = output*numbers[i+1]

print(output)

"""
numbers = ['5', '4', '3']
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
print(numbers)
"""
