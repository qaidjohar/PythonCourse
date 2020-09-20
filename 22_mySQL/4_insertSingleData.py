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
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Taher", "kondhwa")

# Executing the database query
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
