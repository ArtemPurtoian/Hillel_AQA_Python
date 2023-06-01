"""
Find all of the numbers from 1-1000 that have a 3 in them
"""
# 1st solution using a generator
numbers_with_3 = (num for num in range(1, 1001) if '3' in str(num))
for num in numbers_with_3:
    print(num)

# 2nd solution using a list comprehension
numbers_with_3 = [num for num in range(1, 1001) if '3' in str(num)]
print(numbers_with_3)
