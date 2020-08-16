def shout(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs).upper()
    return wrapper


@shout
def greet(name):
    return f"Hi, I'm {name}"


@shout
def order(name, dish):
    return f"Hi! I'm {name} and I would like to order {dish}."


@shout
def user(name, address, phone, gender):
    return f"{name} {address} {phone} {gender}"


print(greet('Mameet'))
print(order(name='Mameet', dish='Biryani'))
print(user('Qaidjohar', 'Camp', '99999', 'Male'))
