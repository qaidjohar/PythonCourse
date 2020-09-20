import mysql.connector

# Connection String
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="test"
)
# print(mydb)

# Creating a pointer object
mycursor = mydb.cursor()

# creating a SQL statement
mycursor.execute("SELECT * FROM customers where name='Qaidjohar'")

# Executing the database query
myresult = mycursor.fetchall()

# Printing the data
for x in myresult:
    # print(x)
    print(f'Sr.No:{x[0]}  Name:{x[1]}  Address:{x[2]}')
