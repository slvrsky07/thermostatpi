#!/usr/bin/env python3
import smtplib
import RPi.GPIO as GPIO
import Adafruit_DHT
import os
import time
import datetime
from datetime import datetime

timestamp = datetime.now()
import mysql.connector

addr_to   = 'TO ADDRESS'
addr_from = 'FROM ADDRESS'
smtp_server = 'SERVER ADDRESS'
smtp_user   = 'USERNAME'
smtp_pass   = 'PASSWORD'
msg = 'GARAGE OVERTEMP!'
msg = 'GARAGE TOO COLD!!!'
msg2 = 'GARAGE TEMP SENSOR READ ERROR'
  
# Send the message via an SMTP server
def send1():
  s = smtplib.SMTP(smtp_server)
  s.login(smtp_user,smtp_pass)
  s.sendmail(addr_from, addr_to, msg)
  s.quit()
  time.sleep(10)
  print ("sent")
  
def send2():
  s = smtplib.SMTP(smtp_server)
  s.login(smtp_user,smtp_pass)
  s.sendmail(addr_from, addr_to, msg1)
  s.quit()
  time.sleep(10)
  print ("sent")

def send3():
  s = smtplib.SMTP(smtp_server)
  s.login(smtp_user,smtp_pass)
  s.sendmail(addr_from, addr_to, msg2)
  s.quit()
  time.sleep(10)
  print ("sent")
  

GPIO.setmode(GPIO.BCM) 
GPIO.setup(12, GPIO.OUT) #burner on/off, HIGH is off LOW is on.

dht_sensor = Adafruit_DHT.DHT22
DHT22_pin = 26

humidity, temp = Adafruit_DHT.read_retry(dht_sensor, DHT22_pin)
#temp = temp * 9/5.0 + 32

Condition = True
while (Condition):
    timestamp = datetime.now()
    mydb = mysql.connector.connect(
    host="localhost",
    user="pi",
    passwd="PASSWORD",
    database="status")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT settemp FROM settemp")
    myresult = mycursor.fetchone()
    x=None
    for x in myresult:
      print(float (x))

    humidity, temp = Adafruit_DHT.read_retry(dht_sensor, DHT22_pin)
    if humidity is None or temp is None:
      time.sleep(2)
      humidity, temp = Adafruit_DHT.read_retry(dht_sensor, DHT22_pin)
      if humidity is None or temp is None:
          send3()
          continue


    temp =  temp * 9/5.0 + 32
    #print ("Temp: {0:0.0f}*F ".format(temp))
    print("Temp={0:0.0f}*F  Humidity={1:0.1f}%".format(temp, humidity))
    hum = round(humidity)
    readtemp = round(temp)
    if float(x) >= temp:
        print("burneron",timestamp)
        GPIO.output(12, GPIO.LOW)
        
    if float(x) <= temp:
        print("burneroff",timestamp)
        GPIO.output(12, GPIO.HIGH) 
        
    if temp >= 85:
        print("burneroff OVER TEMP",timestamp)
        send1()
        GPIO.output(12, GPIO.HIGH)
        time.sleep(10)
        exit()
    if temp <= 42:
        print("BOILER FAILURE TOO COLD!",timestamp)
        send2()
        time.sleep(10)
        
    time.sleep(15)
    
    mydb = mysql.connector.connect(
      host="localhost",
      user="pi",
      passwd="PASSWORD",
      database="status")
    mycursor = mydb.cursor()
    sql = "UPDATE humidity SET humidity = %s"
    val = (hum,)
    mycursor.execute(sql,val)
    mydb.commit()
    
    mydb = mysql.connector.connect(
      host="localhost",
      user="pi",
      passwd="PASSWORD",
      database="status")
    mycursor = mydb.cursor()
    sql = "UPDATE readtemp SET readtemp = %s"
    val = (readtemp,)
    mycursor.execute(sql,val)
    mydb.commit()


    
