
# nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(nested_list)

# for listval in nested_list:
#     # print(listval)
#     for val in listval:
#         print(val)

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

l = [[val for val in listval] for listval in nested_list]
print(l)
