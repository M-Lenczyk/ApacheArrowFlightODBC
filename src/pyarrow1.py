#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 30 10:41:12 2022

@author: user
"""

#from turbodbc import connect
from turbodbc import connect
import pyarrow as pa
import pyarrow.flight as fl

print("Connecting")

#connection = connect(dsn="my DSN")
#connection.autocommit = True

conn_str = (
    "DRIVER=/usr/lib/x86_64-linux-gnu/odbc/psqlodbcw.so;"
    "DATABASE=postgres;"
    "SERVER=localhost;"
    "UID=postgres;"
    "PWD=user;"
    )
    #"Trusted_Connection=yes;"

connection = connect(connection_string=conn_str)


print("Cursor")
cursor = connection.cursor()
print("Cursor execute")
cursor.execute('SELECT close_price, high FROM td_price_data')
for row in cursor:
    print(row)

print("Fetch")
table = cursor.fetchallarrow()
print("Table")
print(table)
print("\n")
print("Table[0]")
a=table[0].to_pylist()
print(a)
print("Table[1]")
print(table[1].to_pylist())
print("table.to_pandas()")
print(table.to_pandas())