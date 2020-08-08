import sys

def add_user():
    try:
        name = input('Enter Your Name: ')
        age = input('Enter yout Age:')
        age = int(age)
        age = name/age
    except ValueError as err:
        print('Value Error Occured::', err)
        sys.exit(1)
    except NameError as err:
        print('Name Error Occured::', err)
        sys.exit(1)
    except Exception as err:
        print('Exception Occured::', err)
        print('Mail this error')
    return dict(name=name, age=age)

print(add_user())