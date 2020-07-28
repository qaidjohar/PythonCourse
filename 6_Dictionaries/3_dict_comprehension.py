# numbers = dict(first=1, second=2, third=3, fourth=4)
# print(numbers)

# squared_numbers = {key: val**2 for key, val in numbers.items()}
# print('squared_numbers', squared_numbers)

# numbers = dict(first=1, second=2, third=3, fourth=4)
# add2numbers = {}
# print(numbers)
# for key, val in numbers.items():
#     print(key, val + 2)
#     add2numbers[key] = val + 2
# print(add2numbers)

# numbers = dict(first=1, second=2, third=3, fourth=4)
# add2numbers = {key+'2': val*2 for key, val in numbers.items()}
# print(add2numbers)


# numbers = [1, 2, 3, 4, 5, 6, 7]
# mynumbers = {num: num**2 for num in numbers}
# print(mynumbers)

# # Keys from 0 to 19 and double values
# mynumbers = {str(num): num*2 for num in range(20)}
# print(mynumbers)

# Value is even or odd
mynumbers = {num: ("even" if num % 2 == 0 else "odd") for num in range(20)}
print(mynumbers)
