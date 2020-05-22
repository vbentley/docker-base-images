# docker-base-images
Repo with docker base images that can be used as a starting point for work. Multiple versions using different drivers and over time.

## Python-alpine-pyodbc-freetds
A docker image built from a Python 3.8 Alpine base along with pyodbc and its dependencies to connect to an SQL Server Instance using freetds drivers

## Python-alpine-pyodbc-mssql
A docker image built from a Python 3.8 Alpine base along with pyodbc and its dependencies to connect to an SQL Server Instance using Microsoft's ODBC Driver for SQL Server on Linux


### Notes
* Both images have a footprint of about 280MB. Might be able to optimize it further for a smaller footprint
* Microsoft officially started supporing drivers for Alpine based images around April 2020. [https://docs.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-ver15#alpine17](Ref Microsoft). The mssql folder has the Dockerfile needed to build an image for this.
* If you're not familiar with Docker, here's what you'll need to do to use the test file
  * Make sure your connection string is accurate
  * Copy the file into a container based off the image
  * From within the container, run the file 
  * Alternately you could use a docker-compose file to automate the steps above
 
 
