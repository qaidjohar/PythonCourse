'''

# Function Definition.......... (first_name, flag) are parameters
def is_instructor(first_name='Qaidjohar', flag=False):
    if flag == True:
        print(f'Hi {first_name}, welcome Back!!')
    else:
        print(f'{first_name} is not an Instructor!!!')


# Function Call ....... ('Qaidjohar', True) are arguments
is_instructor('Mameet')
'''


def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mul(num1, num2):
    return num1 * num2


def div(num1, num2):
    return num1 / num2


def math(num1, num2, fn=add):
    return fn(num1, num2)


print(math(200, 20))
print(math(200, 20, sub))
print(math(200, 20, mul))
print(math(200, 20, div))
