# Custom For Loop

# for num in [1,2,3]
# for char in "hi there"


def my_for(iterable, func):
    iterator = iter(iterable)
    while True:
        try:
            val = next(iterator)
        except StopIteration:
            print('Ending For Loop')
            break
        else:
            func(val)


def square(x):
    print(x*x)


my_for("qaidjohar", print)
my_for([1, 2, 3, 4, 5], square)
