# f = open('mynewfile.txt', 'w')
# f.write('Hello Taher\nThis is amazing content')
# f.close()

with open('mynewfile.txt', 'w') as f:
    val = input('Enter any text:')
    f.write(val)
