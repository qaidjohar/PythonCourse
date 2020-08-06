from functools import reduce

def add(num1,num2):
    print('Insider',num1,num2)
    return num1+num2

lst = [2,3,1,6,9,8,7]

sum1 = reduce(add, lst)
print(sum1)


sum2 = reduce(lambda num1,num2: num1+num2, lst)
print(sum2)

# Multiplication and Division