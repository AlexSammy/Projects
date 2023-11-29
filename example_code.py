# This is an example of using mysql in python. This follows a tutorial on https://www.w3schools.com/python/python_mysql_create_db.asp.

# First we import mysql.connector
import mysql.connector

# Now we want to connect to my database using the username and password
mydb = mysql.connector.connect(
  host="localhost",
  user="username",
  password="password",
  database="media"
)

# Lets store the data in a cursor
cursor = mydb.cursor()
createTable(cursor)

def createTable(cursor):
  # Now we can create a table for movies
  cursor.execute("CREATE TABLE movies (name VARCHAR(255), genre VARCHAR(255))")

def getMovies(genre):
  # Gets all movies given the genre provided
  sql = "SELECT name FROM movies WHERE genre = %s"
  cursor.execute(sql, genre)
  result = cursor.fetchall()
  return result

