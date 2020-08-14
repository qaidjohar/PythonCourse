class User:
    # Class Attribute
    active_users = 0
    
    #class Methods
    @classmethod
    def display_active(cls):
        return f"Total Active users are {cls.active_users}"

    def __init__(self,first_name,last_name,age):
        # instance Attribute/Variable
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        User.active_users += 1
    
    # Instance method
    def fullName(self):
        return f"{self.first_name} {self.last_name}"
    
    def initials(self):
        return f"{self.first_name[0]}.{self.last_name[0]}."
    
    def likes(self,thing):
        return f"{self.first_name} likes {thing}"
    
    def isSenior(self):
        return (self.age > 65)

print('Active Users',User.active_users)
p = User('Qaidjohar','Jawadwala',70)
q = User('Mustafa','Poona',25)
print('Active Users',User.active_users)
r = User('Qaidjohar','Jawadwala',70)
print('R Active Users',User.active_users)
s = User('Mustafa','Poona',25)
print('Active Users',User.active_users)
print('P Active Users',p.active_users)

print(User.display_active())
print(User.fullName(self))
print(s.display_active())


