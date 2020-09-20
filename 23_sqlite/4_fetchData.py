import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def insertData(conn, val):
    sql = "INSERT INTO customers (name, address) VALUES ( ?, ?)"
    cur = conn.cursor()
    cur.execute(sql, val)
    conn.commit()
    return cur.lastrowid


def select_all_tasks(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM customers")

    rows = cur.fetchall()

    for row in rows:
        print(row)


if __name__ == '__main__':
    conn = create_connection("pythonsqlite.db")

    table_query = """ CREATE TABLE IF NOT EXISTS customers (
                            id INT AUTO_INCREMENT PRIMARY KEY, 
                            name text, 
                            address text); """

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, table_query)
        val = ("Mustafa", "Mumbai")
        # rowid = insertData(conn, val)
        # print(rowid)

        select_all_tasks(conn)

    else:
        print("Error! cannot create the database connection.")
