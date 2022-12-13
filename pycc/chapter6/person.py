"""
Simple program using a dictionary to represent a person with varoius
attributes. The user inputs the data, and the program prints it back
out in three different ways.
"""

person = {}

first_name = input('Please enter their first name:\n')
person['first_name'] = first_name.lower()
person['last_name'] = input('Please enter their last name:\n').lower()
person['age'] = input('Please enter their age:\n').lower()
person['city'] = input('Please enter the city in which they reside:\n').lower()

print('\n\n')

# using direct key addressing to get attributes
for attribute in person:
    print(person[attribute].title())

print('\n\n')

# using .get() to retrieve attributes
for attribute in person:
    print(person.get(attribute).title())

print('\n\n')

print(person)
