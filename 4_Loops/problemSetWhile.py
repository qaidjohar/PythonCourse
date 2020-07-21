# Enter a number: 6

# #
# ##
# ###
# ####
# #####
# ######

### Logic 1 ###
# data = int(input('Enter the length of Tower:'))
# x = 1
# while (x <= data):
#     print(x)
#     print('#' * x)
#     x += 1

### Logic 2 ###
data = int(input('Enter the length of Tower:'))
x = 1
while x <= data:
    y = 0
    while y < x:
        print('#', end='')
        y += 1
    print('')
    x += 1
