#from turbodbc import connect
from turbodbc import connect
import pyarrow as pa
import pyarrow.flight as fl

print("Connecting")
connection = connect(driver='{ODBC Driver 18 for SQL Server}',
                    server='DESKTOP-K8F5Q0A\MSSQLSERVER2019',
                    #port=1433,
                    database='stock_database',
                    trusted_connection = 'yes')
print("Cursor")
cursor = connection.cursor()
print("Cursor execute")
cursor.execute('SELECT close_price, high FROM td_price_data')
for row in cursor:
    print(row)

table = cursor.fetchallarrow()
print(table)

print(table[0].to_pylist())
print(table[1].to_pylist())
print(table.to_pandas())