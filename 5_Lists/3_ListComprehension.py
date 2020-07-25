# name = 'qaidjohar'
# print('Input is', name)
# l = []
# for n in name:
#     n = n.upper()
#     l.append(n)

# print(l)


# l = [n.upper() for n in name]
# print('List Comprehension output', l)


# number = 10

# # num_list = [num ** 2 for num in range(number)]
# # print(num_list)

# i = 10
# numb = [number/2 for number in range(20)]
# print(numb)

# HomeWork ProblemSet
# (0°C × 9/5) + 32 = 32°F

celsius = [5, 22, 43, 64, 54, 12, 69, 78, 92]
# fahrenheit = [????]

fahrenheit = [(c*9/5+32) for c in celsius]
print(fahrenheit)
