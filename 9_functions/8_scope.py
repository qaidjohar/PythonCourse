# val = 'Qaidjohar'
# def name():
#     print(val)
# name()

x = 5

def alter():
    global x
    x = x + 10
    print(x)

print('Global x is',x)
alter()
print('Global x is',x)