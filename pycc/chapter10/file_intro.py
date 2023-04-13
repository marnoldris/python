
"""
with open('pi_digits.txt') as file:
    contents = file.read()
print(contents.strip())
"""

with open('pi_digits.txt') as file:
    lines = file.readlines()

for line in range(len(lines)):
    lines[line] = lines[line].strip()
pi_digits = "".join(lines)
print(pi_digits)
##for line in lines:
##    print(line, end='')
