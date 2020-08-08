import sys

def add_user():
    while True:
        try:
            name = input('Enter Your Name: ')
            if not name.isalpha():
                raise TypeError('Only string is expected as name')
        except Exception as err:
            print('Error:',err)
            continue
        break
    print('Name is ',name)

    while True:
        try:
            age = input('Enter Your Age: ')
            if not age.isnumeric():
                raise TypeError('Only number is expected as name')
        except Exception as err:
            print('Error:',err)
            continue
        break
    print('Age is ',age)
    # try:
    #     age = input('Enter yout Age:')
    # except Exception:
    #     print('Error in name')
    #     sys.exit(1)
    return dict(name=name, age=age)

print(add_user())