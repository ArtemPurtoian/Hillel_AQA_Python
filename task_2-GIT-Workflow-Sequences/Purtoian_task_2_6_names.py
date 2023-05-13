non_unique_names = ['Anna', 'Bob', 'Chris', 'Anna', 'John', 'David', 'Chris']
names_dict = dict.fromkeys(non_unique_names)
non_dup_names = list(names_dict.keys())
print(non_dup_names)
