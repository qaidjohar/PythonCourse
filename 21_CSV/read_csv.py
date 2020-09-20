# Bad way of reading a csv

# master = list()
# with open('username.csv') as f:
#     data = f.read()

# data = data.split('\n')
# for val in data:
#     temp = val.split(',')
#     # print(temp)
#     master.append(temp)

# # print(master)
# print(master[2])


# from csv import reader

# with open('username.csv') as file:
#     csv_reader = reader(file)
#     next(csv_reader)
#     for user in csv_reader:
#         print(user[0], user[-1])

from csv import DictReader

with open('username.csv') as file:
    csv_reader = DictReader(file)
    for row in csv_reader:
        print(row['First name'])
