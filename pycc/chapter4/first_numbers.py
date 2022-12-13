"""
Working with for loops and the range() function
You can pass the range() function a range to start and end at (-1)
such as range(1,6) would go from 1 to 5
Or you can pass it a single value, in which case it will start counting
at 0 and stop at 1 before the value listed. This gives you the integer
number of values that matches the number you requested (range(5) will 
give you five values, 0, 1, 2, 3, 4)

You can pass a third value to range(), which will give the step size.
For example, range(2,11,2) will give even numbers from 2 to 10 (2, 4,
6, 8, 10)
"""

for value in range(5):
    print(value)

# Squares 1-10
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

# a more consice version
squares.clear()
for value in range(1,11):
    squares.append(value**2)
print(squares)

# a version using List Comprehension
squares = [value**2 for value in range(1,11)]
print(squares)
