# import random as ran

# print(ran.randint(0,100))

# print(ran.choice(['banana','apple','jackfruit','orange']))

# lst = ['banana','apple','jackfruit','orange']
# print(ran.shuffle(lst))
# print(lst)

# import random as ran
# from random import *
from random import randint as randomByQJ, choice as choiceByQJ, shuffle

print(randomByQJ(0,100))

print(choiceByQJ(['banana','apple','jackfruit','orange']))

lst = ['banana','apple','jackfruit','orange']
print(shuffle(lst))
print(lst)
