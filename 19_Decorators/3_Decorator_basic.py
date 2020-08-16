def be_polite(fn):
    def wrapper():
        print('What a pleasure to meet you!!!')
        fn()
        print('Hope you have a great day!!!')
    return wrapper


def greet():
    print('I am Qaidjohar')


@be_polite
def regret():
    print('This is my worst day')


# regret = be_polite(regret)

regret()
regret()
regret()


# greet = be_polite(greet)
# greet()
