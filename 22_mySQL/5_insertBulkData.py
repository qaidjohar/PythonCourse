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

# Creating a list with all values in tuple
val = [
    ('Peter', 'Lowstreet 4'),
    ('Amy', 'Apple st 652'),
    ('Hannah', 'Mountain 21'),
    ('Michael', 'Valley 345'),
    ('Sandy', 'Ocean blvd 2'),
    ('Betty', 'Green Grass 1'),
    ('Richard', 'Sky st 331'),
    ('Susan', 'One way 98'),
    ('Vicky', 'Yellow Garden 2'),
    ('Ben', 'Park Lane 38'),
    ('William', 'Central st 954'),
    ('Chuck', 'Main Road 989'),
    ('Viola', 'Sideway 1633')
]

# Executing the database query
mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
