
for x in range(1, 21):
    if (x == 4 or x == 13):
        print(f'{x} is unlucky')
    else:
        if (x % 2 == 1):
            print(f'{x} is odd')
        # elif (x % 2 == 0):
        else:
            print(f'{x} is even')
