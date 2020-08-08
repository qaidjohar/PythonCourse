# def add(num1,num2):
#     print('some addition')
#     raise NameError('Calling this function is a Mistake!!!')
#     print('printed after excepton')

# add(1)

def add_user():
    name = input('Enter Your Name: ')
    age = input('Enter yout Age:')
    if not name.isalpha():
        raise TypeError('Name can only be a char and not number!!')
    if not age.isnumeric():
        raise TypeError('Age can only be a numeric and not char!!')
    age = int(age)
    return dict(name=name, age=age)

print(add_user())