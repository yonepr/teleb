import sqlite3
import os

try:
    sqlite_connection = sqlite3.connect('sqlite_python.db')
    cursor = sqlite_connection.cursor()
    sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS car (
                                   id INTEGER PRIMARY KEY,
                                   name TEXT NOT NULL,
                                   password TEXT NOT NULL UNIQUE,
                                   number_phone TEXT UNIQUE NOT NULL,
                                   number_car TEXT UNIQUE NOT NULL,
                                   root BOOL NOT NULL DEFAULT False);'''


    sqlite_insert = """INSERT INTO car(name,password, number_phone, number_car, root)
     VALUES('Gleb', 'Admin123', 89999999999, 'ГА899Б152', true)"""


    cursor.execute(sqlite_create_table_query)
    cursor.execute(sqlite_insert)
    sqlite_connection.commit()

except sqlite3.Error:
    print("Error connection database")
finally:
    if sqlite_connection:
        sqlite_connection.close()
        print("Connection close")


