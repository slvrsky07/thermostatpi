import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="pi",
  passwd="PASSWORD",
  database="status"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT readtemp FROM readtemp")

myresult = mycursor.fetchone()

for x in myresult:
  print(x)