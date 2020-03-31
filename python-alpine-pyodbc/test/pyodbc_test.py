# TEST SCRIPT TO SEE IF PYODBC INSTALLED ON A PYTHON ALPINE BASE CONNECTS TO A LOCAL INSTANCE OF SQL SERVER.

import pyodbc

# SETUP CONNECTION TO THE SQL SERVER DATABASE
def pyodbc_localhost():
    driver = '/usr/lib/libtdsodbc.so'  # NOT THE MOST ELEGANT WAY, BUT WE'RE TELLING PYODBC WHERE TO FIND THE FREETDS DRIVER
    try:
        cnxn = pyodbc.connect('DRIVER='+driver+';SERVER=<serverIP or host.docker.internal>;PORT=1433;DATABASE=<dbname>;UID=<dbuser>;PWD=<dbuserpassword>')
    except Exception as e:
        print(f"Couldn't connect to db on localhost because {e}")
    else:
        cursor = cnxn.cursor()
        return cnxn, cursor


# EXECUTE A SQL QUERY TO SEE IF WE GET A RESULT USING THE CONNECTIONS / CURSOR
def test_localhost(cursor):
    try:
        cursor.execute(""" SELECT * FROM db.schema.table """)  # WHATEVER QUERY YOU WANT TO EXECUTE GOES IN HERE
    except Exception as e:
        print(f"Couldn't get data from table because {e}")
    else:
        for row in cursor.fetchall():
            print(str(row))  # REALLY BASIC TEST JUST TO GET AN OUTPUT AND SEE IF WE CAN RETRIEVE A RESULTSET


cnxn, cursor = pyodbc_localhost()
test_localhost(cursor)
cursor.close()
cnxn.close()
