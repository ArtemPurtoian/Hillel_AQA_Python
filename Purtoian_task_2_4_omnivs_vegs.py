omnivores = {'John', 'Pedro', 'Salma', 'Michael', 'Sean'}
vegetarians = {'Paul', 'Natalie', 'Ricky', 'Lewis', 'Annie'}

# 1 solution
vegs_herbs_guests = vegetarians.union(omnivores)
print(list(vegs_herbs_guests))

# 2 solution
vegetarians = list(vegetarians)
vegetarians.extend(omnivores)
print(vegetarians)
