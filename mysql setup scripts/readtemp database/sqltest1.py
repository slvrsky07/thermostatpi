import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="pi",
  passwd="PASSWORD",
  database="status"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE readtemp (readtemp VARCHAR(255))")