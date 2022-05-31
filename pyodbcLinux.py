#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 30 10:09:24 2022

@author: user
"""
import pyodbc
import textwrap
import pandas as pd
#con = pyodbc.connect("DSN=my-connector")


# Define the Price Data.
price_data = [
    [ 1.00, 2.00, 3.00, 4.40, 500.00, '2019-01-01'],
    [ 6.00, 7.00, 9.00, 9.40, 1000.00, '2020-01-02'],
    [ 11.00, 12.00, 13.00, 14.40, 1500.00, '2021-01-03']
]


for driver in pyodbc.drivers():
    print(driver)
    
conn_str = (
    "DRIVER={PostgreSQL Unicode};"
    "DATABASE=postgres;"
    "SERVER=localhost;"
    "UID=postgres;"
    "PWD=user;"
    )
    #"Trusted_Connection=yes;"

cnxn = pyodbc.connect(conn_str)
'''
crsr = cnxn.execute("SELECT 123 AS n")
row = crsr.fetchone()
print(row)
crsr.close()
cnxn.close()'''

cursor = cnxn.cursor()
cursor.execute('DELETE FROM td_price_data')

# Loop through to insert each row.
for index, row in enumerate(price_data):
    # define an insert query with place holders for the values.
    insert_query = textwrap.dedent('''
        INSERT INTO td_price_data (close_price, high, low, open_price, volume, day_value) 
        VALUES (?, ?, ?, ?, ?, ?);
    ''')

    # define the values
    values = (row[0], row[1], row[2], row[3], row[4], row[5])

    # insert the data into the database
    cursor.execute(insert_query, values)

# commit the inserts.
cnxn.commit()

# grab all the rows from the table
cursor.execute('SELECT * FROM td_price_data')
#cursor.execute('DELETE FROM td_price_data')
for row in cursor:
    print(row)
    
sql = "Select *"
sql = sql + " From td_price_data"
print(sql)
cursor.execute(sql)

data = pd.read_sql(sql, cnxn)

print('Data:')
print(data)

print('\n\n\Columns:')

columns = [column[0] for column in cursor.description]
print(columns)

results = []
for row in cursor.fetchall():
    results.append(dict(zip(columns, row)))
print("\n\n\nresults: ")
print(results)

# close the cursor and connection
cursor.close()
cnxn.close()
