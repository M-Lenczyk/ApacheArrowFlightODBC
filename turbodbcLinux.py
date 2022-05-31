 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 31 05:22:16 2022

@author: user
"""

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
'''
[PostgreSQL ANSI]
Description=PostgreSQL ODBC driver (ANSI version)
Driver=psqlodbca.so
Setup=libodbcpsqlS.so
Debug=0
CommLog=1
UsageCount=1

'''
conn_str = (
    "DRIVER={PostgreSQL ANSI};"
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
#table = cursor.fetchallarrow()
#print(table)

#print(table[0].to_pylist())
#print(table[1].to_pylist())
#print(table.to_pandas())
