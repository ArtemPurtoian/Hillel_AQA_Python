import re


camel_case_names = ["FirstItem", "FriendsList", "MyTuple"]
snake_case_names = []
pattern = r"(?<!^)(?=[A-Z])"

for name in camel_case_names:
    snake_case_name = re.sub(pattern, '_', name).lower()
    snake_case_names.append(snake_case_name)

print(snake_case_names)
