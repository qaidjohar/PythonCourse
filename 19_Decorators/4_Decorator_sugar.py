# def shout(fn):
#     def wrapper(name):
#         print(f'I am very angry')
#         fn(name)
#     return wrapper


# def reason(name):
#     print(f'You have broken my TV {name}')


# reason = shout(reason)
# reason('Mustafa')


def shout(fn):
    def wrapper(name):
        return fn(name).upper()
    return wrapper


@shout
def greet(name):
    return f"Hi, I'm {name}"


# @shout
# def order(name, dish):
#     return f"Hi! I'm {name} and I would like to order {dish}."


print(greet('Mameet'))
# print(order('Mameet', 'Biryani'))
