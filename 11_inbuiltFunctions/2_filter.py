lst = [2,1,3,6,10,23,21,12,14,15,18,17,20]

def isEven(num):
    if(num % 2 == 0):
        return True
    return False

fl = filter(isEven, lst)
print(list(fl))

isEven2 = lambda num: num%2==0

fl2 = filter(lambda num: num%2==1,lst)
print('FL2:',list(fl2))


# Filter all the prime numbers

