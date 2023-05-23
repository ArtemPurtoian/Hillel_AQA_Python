import re


with open(r'.\text.txt', 'r') as file:
    data = file.read()
print(data)

data_to_lower = data.lower()
only_letters_data = re.sub(r'[^a-z]', '', data_to_lower)
letter_count = {}

for letter in only_letters_data:
    if letter in letter_count:
        letter_count[letter] += 1
    else:
        letter_count[letter] = 1

print("Letter counts:")
for letter, count in letter_count.items():
    print(f"{letter}: {count}")
