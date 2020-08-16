from functools import wraps


def log_function_data(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        """I am a Wrapper Function"""
        # print(f"you are calling { fn.__name__ }")
        # print(f"The doc is: { fn.__doc__ }")
        return fn(*args, **kwargs)
    return wrapper


@log_function_data
def add(num1, num2):
    """This is adding two numbers"""
    return num1 + num2


# print(add(10, 20))
print(add.__doc__)
print(add.__name__)


# Exercise
# Calculate sum of arguments in Wrapper
