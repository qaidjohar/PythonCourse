# def add(num1, num2, num3 = 0, num4 = 0, num5 = 0, num6=0):
#     return num1 + num2 + num3 + num4 + num5 + num6

# # print(add(10,12,14,16,17,18))
# print(add(10,12,13))

# def add(*args):
#     sum = 0
#     for val in args:
#         sum += val
#     return sum

# print(add(10,33,1,2,3,4,5,6,7,8,9,8,7,6,5,45,3,3,3))

def is_available(*args):
    print(args)
    if 'Qaidjohar' in args or 'Jawadwala' in args:
        print('Hey Qaidjohar... Welcome Back')
    else:
        print('Who are you? I don\'t know you!!')

name = input('Enter Name')
phone = input('Enter Phone')
address = input('Enter Address')
is_available(name,phone,address)