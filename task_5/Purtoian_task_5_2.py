import pickle


"""
Using the created file in task 1, read the file and perform mathematical 
operations on each element. Output the result of the operation to the 
console. You cannot use imports to import from the first task module.
"""
with open(r'.\test\data\tuples_list_bytes.txt', 'r+b') as file:
    byte_text = file.read()

bytes_to_data = pickle.loads(byte_text)
print(bytes_to_data)

for element in bytes_to_data:
    print(element)
    if element[2] == 1:
        addition = element[0] + element[1]
        print(f'{element[2]} is addition:')
        print(f'{element[0]} + {element[1]} = {addition}')
        print('---------------')
    elif element[2] == 2:
        subtraction = element[0] - element[1]
        print(f'{element[2]} is subtraction:')
        print(f'{element[0]} - {element[1]} = {subtraction}')
        print('---------------')
    else:
        multiplication = element[0] * element[1]
        print(f'{element[2]} is multiplication:')
        print(f'{element[0]} * {element[1]} = {multiplication}')
        print('---------------')
