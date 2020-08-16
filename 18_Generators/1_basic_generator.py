def count_up_to(max):
    count = 1
    while count <= max:
        # print(count)
        yield count
        count += 1


# c = count_up_to(12)
# print(c)
# print(next(c))
# print(next(c))
# print(next(c))

def counter(max):
    for i in range(max):
        # print(i)
        yield i


c = counter(2)
# print(next(c))
# print(next(c))
# print(next(c))

for i in counter(10):
    print(i)