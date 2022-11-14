#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully")

# conn.execute('''CREATE TABLE COMPANY
#          (ID INT PRIMARY KEY     NOT NULL,
#          NAME           TEXT    NOT NULL,
#          AGE            INT     NOT NULL,
#          ADDRESS        CHAR(50),
#          SALARY         REAL);''')
# print("Table created successfully")

# conn.close()


kursori = conn.cursor()

# create a table
# kursori.execute("create table lang(name, first_appeared)")

# # insert values into a table
# kursori.execute("insert into lang values (?, ?)", ("C", 1972))

# execute a query and iterate over the result
for row in kursori.execute("select * from COMPANY"):
    print(row)

conn.close()
print("Database connection closed")

from sqlite3.dbapi2 import *