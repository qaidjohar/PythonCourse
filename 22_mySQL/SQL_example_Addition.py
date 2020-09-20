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
# mycursor.execute(
#     "CREATE TABLE addition(id INT AUTO_INCREMENT PRIMARY KEY, number1 int, number2 int)")

# Displaying list of tables
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)

# creating a SQL statement
sql = "INSERT INTO addition (number1, number2) VALUES (%s, %s)"
val = [(16, 11), (13, 6), (45, 41)]

# Executing the database query
mycursor.executemany(sql, val)
mydb.commit()

print(mycursor.rowcount, "record inserted.")


# creating a SQL statement
mycursor.execute("SELECT * FROM addition")

# Executing the database query
myresult = mycursor.fetchall()

# Printing the data
for x in myresult:
    # print(x)
    print(f'Addition of:{x[1]} and {x[2]} is {x[1]+x[2]}')
    sql = f"UPDATE addition SET Total = {x[1]+x[2]} WHERE id = {x[0]}"
    mycursor.execute(sql)
    mydb.commit()

# mydb.commit()
