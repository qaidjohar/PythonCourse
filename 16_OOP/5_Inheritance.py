# Parent Class
class Animal():
    def __init__(self):
        print("Animal created")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")

#Child Class
class Dog(Animal):
    def __init__(self):
        # Animal.__init__(self)
        print("Dog created")
    
    def whoAmI(self):
        print('I am a dog!!')
    
    def Dog(self):
        print('this is dog calling')

#Child Class
class Cat(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Cat created")
    
    def whoAmI(self):
        print('I am a Cat!!')
    
    def whatIDo(self):
        print('I am always hunting rats!!')

class Kitten(Cat):
    def __init__(self):
        print('Kitten Created')
    
    def whoAmI(self):
        Animal.whoAmI(self)


kit = Kitten()
kit.whatIDo()
kit.eat()
kit.whoAmI()



# tony = Dog()
# tony.eat()
# tony.whoAmI()
# tony.Dog()


# kitty = Cat()
# kitty.eat()
# kitty.whatIDo()
