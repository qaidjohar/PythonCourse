# f = open('myfile.txt', 'r')
# val = f.read()
# print(val, '\n')
# f.seek(0)
# val = f.readline()
# print(val)
# f.close()
# print(f.closed)  # True


# using with keyword

with open('myfile.txt') as f:
    print(f.read())

print(f.closed)
