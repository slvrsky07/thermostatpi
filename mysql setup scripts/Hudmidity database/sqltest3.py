import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="pi",
  passwd="PASSWORD",
  database="status"
)

mycursor = mydb.cursor()

sql = "UPDATE humidity SET humidity = '28'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")