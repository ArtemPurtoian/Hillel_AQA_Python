import re


my_str = " name=Amanda=sssss&age=32&&salary=1500&currency=euro "

pattern = r"(\w+)=(\w+)"
new_str = re.findall(pattern, my_str)

dictionary = dict(new_str)
print(dictionary)
