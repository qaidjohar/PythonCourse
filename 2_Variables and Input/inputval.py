# Step 1: Accept input from user for How much he has walked in Kms
# Step 2: Convert kms to miles
# Step 3: Print the output to the user.

# miles = kms/1.60934

# print("Enter Kms Walked by you: ")
# kms = input()
# # print(type(kms))
# kms = float(kms)  # Type Casting String to Float


kms = float(input("Enter Kms Walked by you: "))
miles = kms / 1.60934
# To Round the decimal to two places Ex. 3.106863683249034 ==> 3.11
miles = round(miles, 2)
print(f"Yeahh!! You have walked {miles} miles")


x = 10
y = '10'
