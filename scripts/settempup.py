#!/usr/bin/env python3
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
  sql = "UPDATE settemp SET settemp = settemp + 1"

  mycursor.execute(sql)

  mydb.commit()

  print(mycursor.rowcount, "record(s) affected")