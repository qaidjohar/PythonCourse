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
    val = 54321
    def __init__(self,num1,num2):
        self.n1 = num1
        self.n2 = num2
        print('Constructor Called',num1,num2)
    def add(self):
        print(self.n1 + self.n2)
    def multiply(self):
        print(self.n1 * self.n2)
    # divide
    # substract
    # remainder
    # integer divide
    # getter
    # setter: change the values for n1 and n2

a = Calculator(10,20)
b = Calculator(20,40)
a.set(50,60)
print(a.n1,a.n2)
print(a.val)
# print(b.n1)
# a.add()
# b.add()
# a.multiply()