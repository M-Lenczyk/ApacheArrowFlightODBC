# Apache Arrow Flight ODBC

The goal of this project is to create an Apache Arrow Flight service in combination with an ODBC data source. 
The project also aims to assess the performance diffrence between using a pure ODBC connection and an Apache Arrow Flight augumented one.

Arrow Flight developed by Apache is a client-server RPC framework which simplifies high-performance transfer 
of large datasets through network interfaces. It uses the Apache Arrow format to store and process data in memory 
using a columnar oriented format. This increases the speed of data analysis and processing. 
The transfer in columnar format is optimized with the usage of RPC methods and the IPC format.

<p align="center"><img src="https://user-images.githubusercontent.com/80449303/174089728-1419ea5e-8d18-4d64-9fab-c8bc7d7f7586.png"></p>



DISCLAIMER: This project is not yet finished and some key components are still WIP. 

Finished components include:
* A configured PostgreSQL DBMS
* Linking the ODBC driver with PostgreSQL
* Linking the turboODBC with PostgreSQL
* Base for a FlightClient in Python
* Base for a FlightServer in Python

TODO:
* Inject the TPC-DS or other benchmark dataset into PostgreSQL database
* Complete the FlightClient module (add missing, required commands, dependencies)
* Complete the FlightServer module (add missing, required commands, dependencies)
* Configure the communication between the FlightServer module and the database

## Environment configuration

### 1. Operating system

Described project was created on OS *Debian 11*, with Spyder environment. The Spyder can be installed from the marketplace.

### 2. PostgreSQL
We used PostgreSQL as our preffered Database managment system.
To install PostgreSQL RDBMS as a *root* user run command:

`apt install postgresql `

To check its status run:

`systemctl status postgresql`

In case it is inactive run:

`systemctl start postgresql`

### 3. ODBC

ODBC installation (for PostgreSQL) command is:

`apt install odbc-postgresql`

To check which components have been installed run:

`odbcinst -q -d`

After installation, change to *postgres* user:

`su - postgres`

You can change user credentials by command:

`ALTER USER postgres WITH PASSWORD 'user';`

Now we can proceed to database creation:

`createdb sampledb`


### 4. turbODBC

To install turbODBC ensure you have installed earlier *pyODBC*, *numpy* (required by turbODBC) and *pyarrow* packages.

To install pyODBC you can use:

`pip install pyodbc`

To install *pyarrow* you can use:

`pip install pyarrow`

To install *numpy* you can use:

`pip install numpy`

Afterwards run:

`pip install turbODBC`


### 5. Python

Next step is loading data to database. A sample code *pyarrow1.py* to achieve that is provided.

### 6. Datasets

#### TPC-H

Download the source code for TPC-H tool from https://www.tpc.org/tpc_documents_current_versions/current_specifications5.asp
Copy *Makefile.suite* to Makefile.

`cp Makefile.suite Makefile`

Edit Makefile and update the line regarding the OS:

`nano MakeFile`

Edit and save the line:

`OS=LINUX`

Run Makefile:

`make`

To generate the load data files (50GB) in the example directory you can use





