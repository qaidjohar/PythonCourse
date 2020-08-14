class User:
    def __init__(self,first_name,last_name,age):
        # instance Attribute/Variable
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    # Instance method
    def fullName(self):
        return f"{self.first_name} {self.last_name}"
    
    def initials(self):
        return f"{self.first_name[0]}.{self.last_name[0]}."
    
    def likes(self,thing):
        return f"{self.first_name} likes {thing}"
    
    def isSenior(self):
        return (self.age > 65)


q = User('Qaidjohar','Jawadwala',70)
p = User('Mustafa','Poona',25)

print(q.fullName())
print(p.fullName())

print(q.isSenior())
print(p.likes('cakes'))
print(q.likes('Sweets'))
