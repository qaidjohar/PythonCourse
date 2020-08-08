import sys

def add_user():
    while True:
        try:
            name = input('Enter Your Name: ')
            if not name.isalpha():
                raise TypeError('Only string is expected as name')
        except Exception as err:
            print('Error:',err)
        else:
            print('Name is ',name)
            break
        finally:
            print('This will be printed')
    
    age=12
    return dict(name=name, age=age)

print(add_user())