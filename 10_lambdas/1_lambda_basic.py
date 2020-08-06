def double(num):
    return num*2

double2 = lambda num: num*2

# print(double.__name__)
# print(double(3))
# print(double(4))

# print(double2(2))
# print(double2(3))
# print(double2(4))

s = lambda strng: strng.upper()
print(s('hello world'))
# print(s.__name__)

toFar = lambda celsius: (celsius*9/5)+32
# print(toFar(0))
# (0°C × 9/5) + 32 = 32°F

a = lambda: 'Hello World'
# print(a())

add = lambda num1,num2: num1 + num2
# print(add(12,51))

isOdd = lambda num: num%2==1
# print(isOdd(4))

isOddEven = lambda num: 'Even' if num%2 == 0 else 'Odd'
print(isOddEven(4))