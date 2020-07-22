# print('AlphaNumeric', data.isalnum())
# print('Alpha', data.isalpha())
# print('Numeric', data.isnumeric())

data = input("Enter the length of tower: ")

if data.isnumeric():
    data = int(data)
    x = 1
    while x <= data:
        print(f"{' '*(data-x)}{'#'*x}")
        x += 1
else:
    print('Invalid input. Please enter only numeric values. Ex. 10')

    #
   ###
  #####
 #######
#########
 #######
  #####
   ###
    #
