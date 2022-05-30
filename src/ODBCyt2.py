import pyodbc
import textwrap

# Define the Price Data.
price_data = [
    [ 5.00, 3.00, 1.00, 2.40, 100.00, '2019-01-01'],
    [ 6.00, 3.00, 5.00, 9.40, 300.00, '2020-01-02'],
    [ 7.00, 2.00, 1.00, 2.40, 200.00, '2021-01-03']
]


for driver in pyodbc.drivers():
    print(driver)

# define the server and the database
server = 'DESKTOP-K8F5Q0A\MSSQLSERVER2019'
database = 'stock_database'

# Define the connection string
cnxn = pyodbc.connect(
    'DRIVER={ODBC Driver 18 for SQL Server}; \
    SERVER='+ server +'; \
    DATABASE='+ database +';\
    Trusted_Connection=yes;'
)

# Create the Cursor.
cursor = cnxn.cursor()

#cursor.execute("INSERT INTO td_price_data (close_price, high, low, open_price, volume, day_value) VALUES (7.00, 2.00, 1.00, 2.40, 200.00, '2021-01-03')")
#cursor.execute('DELETE FROM td_price_data WHERE close_price=11')
cursor.execute('DELETE FROM td_price_data')
# commit the inserts.
cnxn.commit()

# grab all the rows from the table
cursor.execute('SELECT * FROM td_price_data')
for row in cursor:
    print(row)



# close the cursor and connection
cursor.close()
cnxn.close()