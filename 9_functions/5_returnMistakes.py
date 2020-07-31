# def

# l = [1, 3, 5, 3, 2, 5, 4, 6, 7, 8]
# val = sum_odd_numbers(l)
# print(val)


# def addnumb():
#     list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14]
#     a = [(list % 2 == 1) for list in list1]
#     return a
# print(addnumb())

# def sum_odd_num(l):
#     i = 0
#     for i in l:
#         if i % 2 == 1:
#             i += l[i]
#         print(i)
#     return i


# l = [1, 2, 3, 4, 5, 5, 6, 4, 3, 7, 8, 9]
# val = sum_odd_num(l)
# print(val)


def sum_odd_numbers(l):
    # print(l)
    i = 0
    for val in l:
        # print(val)
        if val % 2 == 1:
            # print(val)
            i = i + val
    return i


l = [1, 3, 5, 3, 2, 5, 4, 6, 7, 8]
i = sum_odd_numbers(l)
# print(i)


def is_odd_numbers(x):
    if x % 2 == 1:
        return True
    return False

# print(is_odd_numbers(6))


# Practice ProblemSet
def math(num1, num2, operation):
    pass


val = math(1, 4, 'add')
val = math(1, 4, 'sub')
val = math(1, 4, 'mul')
val = math(1, 4, 'div')
