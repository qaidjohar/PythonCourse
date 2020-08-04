# def favcolors(mameet,qj,mustafa):
#     print(mameet, qj,mustafa)


# favcolors(qj='green',mameet='black',mustafa='blue')
# # ,,

def favcolors(**kwargs):
    print(kwargs)
    for key,val in kwargs.items():
        print('Favourite color of',key,'is',val)
# favcolors(qj='green',mameet='black',mustafa='blue',fatima='orange',taher='yellow')


# Both * and ** 
# ordering
def favcolors2(num1,*args,qj,**kwargs):
    print('num1:',num1)
    print('args:',args)
    print('def arguments:',qj)
    print('kwargs:',kwargs)
    # for key,val in kwargs.items():
    #     print('Favourite color of',key,'is',val)

favcolors2(10,20,'aaaa',qj='green',mameet='black',mustafa='blue',fatima='orange',taher='yellow')