
import random

rand_nums = [random.randint(1, 50) for i in range(10)]
# or
#rand_nums = []
#for i in range(10):
#    rand_nums.append(random.randint(1, 50))

num_string = ''

# this works
num_string = ', '.join(str(num) for num in rand_nums)

print(num_string)
