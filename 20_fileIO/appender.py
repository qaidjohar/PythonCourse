# with open('mynewfile.txt', 'a') as f:
#     val = input('Enter any text:')
#     f.write(val)

with open('mynewfile.txt', 'r+') as f:
    val = input('Enter any text:')
    f.write(val)
    f.seek(10)
    val = input('Enter any text:')
    f.write(val)
    f.truncate()
