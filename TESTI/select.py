#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully")

cursor = conn.execute("SELECT id, name,  age, address, salary from COMPANY")
# for row in cursor:
#    print("ID = ", row[0])
#    print("NAME = ", row[1])
#    print("ADDRESS = ", row[2])
#    print("SALARY = ", row[3], "\n")

# print("Operation done successfully")


lista = []
for row in cursor:
    lista.append(row)
conn.close()

print(lista)
