# docker-base-images
Repo with docker base images that can be used as a starting point for work.

## Python-alpine-pyodbc
A docker image built from a Python 3.7 Alpine base along with pyodbc and its dependencies to connect to an SQL Server Instance. 

### Notes
* The image has a footprint of about 275MB. We should be able to optimize it further for a smaller footprint
* If you're not familiar with Docker, here's what you'll need to do to use the test file
  * Make sure your connection string is accurate
  * Copy the file into a container based off the image
  * From within the container, run the file 
  * Alternately you could use a docker-compose file to automate the steps above
 
 
