# Apache Arrow Flight ODBC

## Introduction

The goal of this project is to create an Apache Arrow Flight service in combination with an ODBC data source. 
The project also aims to assess the performance diffrence between using a pure ODBC connection and an ODBC connection with Apache Arrow Flight augumentation. 

We will be using PostgreSQL DBMS with a dedicated ODBC driver, enriched by the turbODBC library to get our results in the Arrow Format. The datasets on which we will perform our queries should be provided by a dedicated benchmark, for example: TPC-DS.



Proposed solution architecture:

<p align="center"><img src="https://user-images.githubusercontent.com/80449303/174089728-1419ea5e-8d18-4d64-9fab-c8bc7d7f7586.png"></p>

This document provides means for installation and configuration of the test environment and a short introduction to used technologies, modules and how they work.

DISCLAIMER: 
This project is not yet finished and some key components are still WIP.

It is highly recommended to get familiar with the references listed at end of this document.

Especially:

* the one regarding a similiar project made with the RUST language: https://github.com/timvw/arrow-flightsql-odbc
* ArrowFlight: Server, Client module implemantation: https://mirai-solutions.ch/news/2020/06/11/apache-arrow-flight-tutorial/


Finished components (with installation instructions below) include:
* A configured PostgreSQL DBMS
* Linking the ODBC driver with PostgreSQL
* Linking the turboODBC with PostgreSQL and returning the data in arrow format (*pyarrow1.py*)
* Base for a FlightClient in Python (*FlightClient.py*)
* Base for a FlightServer in Python (*FlightServer.py*)
* Full protobuf definitions

TODO:
* Inject the TPC-DS or other benchmark dataset into PostgreSQL database
* Complete the FlightClient module (add missing, required commands, dependencies)
* Complete the FlightServer module (add missing, required commands, dependencies)
* Configure the communication between the FlightServer module and the database

## Used technologies

### 1. Apache Arrow Flight

Arrow Flight developed by Apache is a client-server RPC framework which sim-
plifies high-performance transfer of large datasets through network interfaces.
It uses the Apache Arrow format to store and process data in memory using a
columnar oriented format. This increases the speed of data analysis and pro-
cessing. The transfer in columnar format is optimized with the usage of RPC
methods and the IPC format.

### 2. ODBC

ODBC (Open Data Base Connectivity) - API specification that allows the application to access multiple
Database Management Systems (DBMS) with the same source code. The appli-
cation calls functions in the ODBC interface that are implemented in modules
called drivers, that support a specific database. Driver Manager handles the
communication between the application and individual drivers. 

Architectural assumptions of ODBC to implement access standardization:

* Applications must access multiple DBMSs using the same source code
without recompiling and linking.

* Applications must be able to access multiple DBMSs simultaneously.

* NOTE: The ODBC API is used between the application and the manager,
and between the manager and individual drivers.

What the ODBC interface needs

* Applications - for calling ODBC functions, sending SQL statements and
displaying / retrieving results.

* Driver Manager - handles drivers for the application and performs called
ODBC functions, or redirects these calls to individual drivers.

* Drivers - they handle ODBC function calls, execute SQL queries on the
selected data source and modify the application’s query if necessary to be
supported by the selected DBMS.

* Data source - a single data source includes: data that the user wants to
handle, as well as the operating system and DBMS used.

### 3. TPC-DS

TPC-DS is a decision support benchmark that models several aspects of a de-
cision support system, for example queries and data maintenance. The bench-
mark provides a evaluation of performance as a general purpose decision support
system. A benchmark result measures query response time:

* in single user mode,
* query throughput in multi user,
* mode and data maintenance performance.

for a given:

* hardware,
* operating system,
* data processing system configuration under a controlled,
* complex,
* multi-user decision support workload.

### 4. TPC-H

An alternative to TPC-DS is the TPC-H. TPC-H is a decision support benchmark. 
TPC-H Benchmark accommo-dates trends and maintain the relevance of the 
Price/Performance metric. It consists of a suite of business oriented ad-hoc
queries and concurrent data modifications. This benchmark illustrates decision 
support systems that examine large volumes of data. TPC-H executes queries with a high degree of complexity.
Moreover, Benchmark gives answers to critical business questions.


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

`pip install turbodbc`


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

To generate the load data files (50GB) in the example directory you can use:

`dsdgen scale 50 dir /tmp`

DISCLAIMER: To make the experiment plausible it is recommended to provide two datasets.
* One in which the dataset is will be almost completely cached
* One in which the dataset definitely will not be cached

To ensure the above the datasets should be tier or two smaller/bigger in size than the OS operating memory.
For example: for 8GB operating memory a dataset D1 with 100MB and dataset D2 with 100GB should be created.

#### TPC-H

Download the source code for TPC-H tool from https://www.tpc.org/tpc_documents_current_versions/current_specifications5.asp

Make directory *tpch-tool*

`mkdir /opt/db/tpch-tool`

Save the TPC-H Tool zip to the above directory and extract it with the name *tpc-h-tool_number_version.zip*

Unzip the folder:

`unzip tpc-h-tool_number_version.zip`

Go to dbgen folder:

`cd tpc-h-tool_number_version/dbgen`

Copy makefile.suite to Makefile: Go to dbgen folder:

`cp makefile.suite Makefile`

Edit Makefile:

`nano Makefile`

Update the lines below:

`CC=gcc
DATABASE=ORACLE
MACHINE=LINUX
WORKLOAD=TPCH
`
Run Makefile:

`make`

To generate queries and see sizes queries run the following commands:

`./dbgen -s 1`

`ls -l *.tbl`

```for i in `ls *.tbl`; do sed 's/|$//' $i > ${i/tbl/csv};```

`echo $i; done;`

```cd /opt/db/ws/tpch/sql```

```cp /opt/db/tpch-tool/tpch_number_version/dbgen/dists.dss```

```for q in `seq 1 22`;do DSS_QUERY=/opt/db/tpch-tool/tpch_number_version/dbgen/queries qgen $q > $q.sql;```

## References

https://arrow.apache.org/overview/#

https://arrow.apache.org/blog/2019/10/13/introducing-arrow-flight/












