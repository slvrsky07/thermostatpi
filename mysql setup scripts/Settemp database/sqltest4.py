import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="pi",
  passwd="PASSWORD",
  database="status"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT settemp FROM settemp")

myresult = mycursor.fetchone()

for x in myresult:
  print(x)