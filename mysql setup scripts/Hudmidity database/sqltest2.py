#!/usr/bin/env python3
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="pi",
  passwd="PASSWORD",
  database="status"
)

mycursor = mydb.cursor()

sql = "INSERT INTO humidity (humidity) VALUES (45)"
mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
