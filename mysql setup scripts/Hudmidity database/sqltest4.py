import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="pi",
  passwd="PASSWORD",
  database="status"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT humidity FROM humidity")

myresult = mycursor.fetchone()

for x in myresult:
  print(x)