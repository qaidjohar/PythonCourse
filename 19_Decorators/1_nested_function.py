from random import choice


def greet(person):
    def get_mood():
        msg = choice(('Welcome Dear ', 'Hello There ',
                      'Please Leave ', 'Go Away '))
        return msg

    result = get_mood() + person
    return result


# print(greet('Taher'))

def calc(num1, num2, expr):
    def add():
        return num1 + num2

    def mul():
        return num1 * num2

    if expr == 'add':
        result = add()
    else:
        result = mul()
    return result


print(calc(10, 20, 'mul'))
