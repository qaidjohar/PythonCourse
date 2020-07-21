# Asking for password 3 times if entered wrong
# # i = 0
# while i < 3:
#     password = input('Enter a Password: ')
#     if password == 'security':
#         print('Password is correct.')
#         break
#     else:
#         print('Please try again!!')

#     # i = i+1
#     i += 1


# break
# continue


# Keep asking for password until password entered is correct

#### Code Logic 1 ######
# while True:
#     password = input('Enter a Password: ')
#     if password == 'security':
#         print('Password is correct.')
#         break
#     else:
#         print('Please try again!!')

#### Code Logic 2 ######
password = input('Enter a Password:')
while password != 'alpha@123#QJ':
    print('Invalid password!! Please try again!!')
    password = input('Enter a Password:')

print('Password is correct')
