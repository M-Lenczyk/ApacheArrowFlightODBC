import pyodbc
#cnxn = pyodbc.connect('DRIVER={Devart ODBC Driver for SQL Server};Server=DESKTOP-K8F5Q0A\MSSQLSERVER2019;Database=mydb;Port=1433;User ID=_SYSTEM;Password=sys')
cnxn = pyodbc.connect('Server=localhost\MSSQLSERVER01;Database=master;Trusted_Connection=True;')

cursor = cnxn.cursor()
#cursor.execute("INSERT INTO EMP (EMPNO, ENAME, JOB, MGR) VALUES (535, 'Scott', 'Manager', 545)")
cursor.execute("INSERT INTO osoba (id, imie, nazwisko) VALUES (535, 'Scott', 'Manager')")

cursor = cnxn.cursor()
cursor.execute("SELECT * FROM osoba")
row = cursor.fetchone()
while row:
    print (row)
    row = cursor.fetchone()