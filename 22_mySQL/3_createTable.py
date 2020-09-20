import mysql.connector

# Connection String
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="test"
)
print(mydb)

# Creating a pointer object
mycursor = mydb.cursor()
# Executing the database query
mycursor.execute(
    "CREATE TABLE customers(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

# Displaying list of tables
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)
