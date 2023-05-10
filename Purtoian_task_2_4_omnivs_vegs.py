omnivores = {'John', 'Pedro', 'Salma', 'Michael', 'Sean'}
vegetarians = {'Paul', 'Natalie', 'Ricky', 'Lewis', 'Annie'}

vegs_herbs_guests = vegetarians.union(omnivores)
print(list(vegs_herbs_guests))
