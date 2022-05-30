import pyodbc
# Some other example server values are
#server = 'localhost\sqlexpress' # for a named instance
#server = 'myserver,port' # to specify an alternate port
server = '192.168.1.5,1433' # to specify an alternate port
server = 'DESKTOP-K8F5Q0A\MSSQLSERVER2019,1433' # to specify an alternate port

#server = 'tcp:myserver.database.windows.net'
database = 'mydb'
#username = 'myusername'
username = 'student'
#password = 'mypassword'
password = 'student'
#cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cnxn = pyodbc.connect('DRIVER={Devart ODBC Driver for SQL Server};SERVER='+server+';DATABASE='+database+';''UID='+username+';PWD='+ password)


#DRIVER=Devart ODBC Driver for SQL Server;Description=ODBC Driver for SQL Server;Data Source=192.168.56.1;Initial Catalog=testdb;User ID=sa;Password=sa

cursor = cnxn.cursor()

#Sample select query
cursor.execute("SELECT @@version;")
row = cursor.fetchone()
while row:
    print(row[0])
    row = cursor.fetchone()



