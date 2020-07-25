# d = {'name': 'Qaidjohar', 'id': '221', 'age': 27, 101: 'Something'}

# # print(d['name'], d['id'])
# print(d)
# print(d.items())
# print('\n')

# for key, value in d.items():
#     print(f'Key:{key} Value:{value}')


l = [33, 22, 11, 44, 33, 22, 11]

# if 33 in l:
#     print('33 iS available')

# for val in l:
#     print(f'val: {val}')

some_dict = dict(id=22,
                 name='Qaidjohar',
                 training='Python',
                 company='QJ Academy'
                 )

# print(some_dict)

# # for key, val in some_dict.items():
# #     print(key, val)

# print(some_dict.keys())

# for k in some_dict.keys():
#     print(k)
# print('\n Values')
# for v in some_dict.values():
#     print(v)


# print(some_dict)
# print('training' in some_dict.keys())
# if 'address' in some_dict.keys():
#     print('Training is available')
# else:
#     print('Training is not available')

# print('Qaidjohar' in some_dict.values())


# print(some_dict.values())


network = {}
network['comp1'] = '192.168.43.12'
network['comp2'] = '192.168.43.13'
network['comp3'] = '192.168.43.14'
network['comp4'] = '192.168.43.15'

print(network)

print(network['comp3'])

for name in network.keys():
    print(name)

for ip in network.values():
    print(ip)

for name, ip in network.items():
    print(name, ip)

print('\n')
if 'comp4' in network.keys():
    print(network['comp4'])
