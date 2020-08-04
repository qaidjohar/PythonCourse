def sum_values(*args):
    print(args)
    sum = 0
    for val in args:
        sum += val
    return sum

values = [33,22,11,44,3,4,5,6,7]
# print(sum_values(*values))
# print(sum_values(*[1,2,3,4,5]))






def favcolors(**kwargs):
    print('kwargs:',kwargs)

val = dict(qj='green',mameet='black',mustafa='blue',fatima='orange',taher='yellow')
# print(val)
favcolors(**val)
favcolors(qj='green',mameet='black',mustafa='blue',fatima='orange',taher='yellow')
favcolors(**dict(qj='green',mameet='black',mustafa='blue',fatima='orange',taher='yellow'))
