# lst = [char for char in 'eio' if char in 'xyz']

lst = [True if x%2==0 else False for x in range(0,10,1)]
print(lst)
print('All',all(lst))
print('Any',any(lst))