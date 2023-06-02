"""
Find all of the numbers from 1-1000 that are divisible by 7
"""
# 1st solution using a generator
divisible_by_7 = (num for num in range(1, 1001) if num % 7 == 0)
for num in divisible_by_7:
    print(num)

# 2nd solution using a list comprehension
divisible_by_7 = [num for num in range(1, 1001) if num % 7 == 0]
print(divisible_by_7)
