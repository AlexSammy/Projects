# This is an example of using mysql in python. This follows a tutorial on https://www.w3schools.com/python/python_mysql_create_db.asp.

# First we import mysql.connector
import mysql.connector

# Now we want to connect to my database using the username and password
mydb = mysql.connector.connect(
  host="localhost",
  user="username",
  password="password"
)

# Lets store the data in a cursor
cursor = mydb.cursor()

# Now we can create a database for movies
cursor.execute("CREATE DATABASE movies")

# todo(alexsammy): add queries for movies database
