import pyodbc
import textwrap

# Define the Price Data.
price_data = [
    [ 1.00, 2.00, 3.00, 4.40, 500.00, '2019-01-01'],
    [ 6.00, 7.00, 9.00, 9.40, 1000.00, '2020-01-02'],
    [ 11.00, 12.00, 13.00, 14.40, 1500.00, '2021-01-03']
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
for row in cursor:
    print(row)

# close the cursor and connection
cursor.close()
cnxn.close()