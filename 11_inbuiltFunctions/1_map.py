l = [1,2,3,4,5]
doubleList = []
def double(num):
    return num * 2

for val in l:
    temp = double(val)
    doubleList.append(temp)
# print(doubleList)

l2 = [10,20,30,40,50]
def triple(num):
    return num * 3

tripleList = map(triple, l2)
# print(list(tripleList))

l3 = [10,20,30,40,50]
tlist = map(lambda num: num * 4, l3)
print(list(tlist))

# doubleList = map(double, l)
# print(list(doubleList))


