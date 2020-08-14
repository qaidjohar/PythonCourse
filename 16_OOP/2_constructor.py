# class Sample:
#     def __init__(self):
#         print('Constructor is printing')

# Sample()
# s1 = Sample()

# class Calculator:
#     def __init__(self,num1,num2):
#         self.n1 = num1
#         self.n2 = num2
#         print('Constructor Called',num1,num2)
#     def add(self):
#         print(self.n1 + self.n2)

# a = Calculator(10,20)
# b = Calculator(20,40)
# a.add()
# b.add()



# class Names:
#     def __init__(self, name):
#         self.name = name
#     def showName(self):
#         print(self.name)

# qj = Names('Qaidjohar')
# mt = Names('Mustafa')
# qj.showName()
# mt.showName()


class Calculator:
    def __init__(self,num1,num2):
        self.n1 = num1
        self.n2 = num2
        print('Constructor Called',num1,num2)

    def add(self):
        return self.n1 + self.n2
    def multiply(self):
        return self.n1 * self.n2
    # divide
    def divide(self):
        return self.n1 / self.n2

    # substract
    def substract(self):
        return self.n1 - self.n2

    # remainder
    def remainder(self):
        return self.n1 % self.n2

    # integer divide
    def integerDivide(self):
        return self.n1 // self.n2

    # getter
    def getter(self):
        return [self.n1, self.n2]

    # setter: change the values for n1 and n2
    def setter(self, num1, num2):
        self.n1 = num1
        self.n2 = num2

a = Calculator(10,20)
b = Calculator(20,40)

print(a.getter())
a.setter(20,30)
print(a.getter())
# print(b.n1)
# a.add()
# b.add()
# a.multiply()


class calci:
    def __init__(self,a,b,c):
        self.num1 =a
        self.num2= b
        self.oprator=c
        if (self.oprator == "add"):
            self.add()
    
    def add(self):
        result= print(self.num1+self.num2)
        print(result)

a = (input("type number1"))
b = (input( "type number2"))
c=(input("oprator"))
c = calci(a,b,c)
