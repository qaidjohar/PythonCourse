s = set({11, 22, 33, 44, 55, 66, 77, 66, 55, 44, 33, 22, 11})

# print(s)

# for val in s:
#     print('Set Values: ', val)

# Add method in Set
s.add(5)
# print(s)

# Remove method in Set
s.remove(5)

# clear
s.clear()


python_class = {'Taher', 'Fatima', 'Mustafa', 'Mameet'}
web_class = {'Zainab', 'Qaidjohar', 'Taher', 'Mustafa'}


# Union
students = python_class | web_class

# Intersection
students = python_class & web_class


# set comprehension

sc = {val**2 for val in range(10)}
print(sc)
