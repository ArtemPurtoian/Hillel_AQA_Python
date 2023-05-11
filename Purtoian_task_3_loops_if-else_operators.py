# 1
print("# 1")

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd = []
even = []

for index, value in enumerate(numbers):
    if index % 2 != 0:
        odd.append((index, value))
    else:
        even.append((index, value))

print(f'This is the list of odd indexes and values  - {odd}.')
print(f'This is the list of even indexes and values - {even}.')
print("--------------------")

# 2
print("# 2")

number = 2

result_1 = number * number
print(f"Result 1 = {result_1};")

result_2 = number + number
print(f"Result 2 = {result_2};")

result_3 = number / number
print(f"Result 3 = {result_3};")

result_4 = number // number
print(f"Result 4 = {result_4}.")
print("--------------------")

# 3
print("# 3")

friends = ["John", "Marta", "James"]
enemies = ["John", "Jonathan", "Artur"]

for friend in friends:
    if friend == "James":
        continue
    elif friend not in enemies:
        print(f"{friend}, we are the best friends!")
    else:
        print(f"{friend}, we are not friends anymore!")
