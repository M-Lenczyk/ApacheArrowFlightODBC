# Apache Arrow Flight ODBC

The goal of this project is to create an Apache Arrow FlightSQL service in combination with an ODBC data source. 
The project also aims to assess the performance diffrence between using a pure ODBC connection and an Apache Arrow FlightSQL augumented one.

Arrow FlightSQL developed by Apache is a client-server RPC framework which simplifies high-performance transfer 
of large datasets through network interfaces. It uses the Apache Arrow format to store and process data in memory 
using a columnar oriented format. This increases the speed of data analysis and processing. 
The transfer in columnar format is optimized with the usage of RPC methods and the IPC format.

<p align="center"><img src="https://user-images.githubusercontent.com/80449303/174089728-1419ea5e-8d18-4d64-9fab-c8bc7d7f7586.png"></p>



DISCLAIMER: This project is not yet finished and some key components are still WIP. 

Finished components include:
* A configured PostgreSQL DBMS
* Linking the ODBC driver with PostgreSQL
* Linking the turboODBC with PostgreSQL

Core components of a FlightClient
* Core components of a FlightServer

TODO:
* Inject the TPC-DS or other benchmark dataset into PostgreSQL
* Complete the FlightClient module (add missing, required commands)
* Complete the FlightServer module (add missing, required commands)

## Data sources

We used PostgreSQL because it offers an ApacheArrow FlightSQL endpoint and is open-sourced.
For the dataset we recommend using either TPC-DS or TPC-H, but any benchmark focused on load assesment should work. 

## Generating datasets

Run `ng generate component component-name`  `ng generate directive|pipe|service|class|guard|interface|enum|module`.

