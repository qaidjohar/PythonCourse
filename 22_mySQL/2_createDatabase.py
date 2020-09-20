import mysql.connector

# Connection String
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)
print(mydb)

# Creating a pointer object
mycursor = mydb.cursor()
# Executing the database query
mycursor.execute("CREATE DATABASE test")

# Show all Databases
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)
