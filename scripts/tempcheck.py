#!/usr/bin/env python3
import smtplib
import Adafruit_DHT
import RPi.GPIO as GPIO
import os
import time
import datetime
from datetime import datetime
timestamp = datetime.now()

addr_to   = 'TO ADDRESS
addr_from = 'FROM ADDRESS'
smtp_server = 'SERVER ADDRESS'
smtp_user   = 'USERNAME'
smtp_pass   = 'PASSWORD'
msg = 'GARAGE OVERTEMP!'
msg1 = 'GARAGE TOO COLD!!!'
msg2 = 'GARAGE TEMP SENSOR READ ERROR'

GPIO.setmode(GPIO.BCM)
dht_sensor = Adafruit_DHT.DHT22
DHT22_pin = 26

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


humidity, temp = Adafruit_DHT.read_retry(dht_sensor, DHT22_pin)
#temp = temp * 9/5.0 + 32

humidity, temp = Adafruit_DHT.read_retry(dht_sensor, DHT22_pin)
if humidity is None or temp is None:
    time.sleep(2)
    humidity, temp = Adafruit_DHT.read_retry(dht_sensor, DHT22_pin)
    if humidity is None or temp is None:
        send3()
        time.sleep(2)

temp =  temp * 9/5.0 + 32
#print ("Temp: {0:0.0f}*F ".format(temp))
print("Temp={0:0.0f}*F  Humidity={1:0.1f}%".format(temp, humidity))
hum = round(humidity)
readtemp = round(temp)
      
if temp >= 85:
    print("burneroff OVER TEMP",timestamp)
    send1()
    time.sleep(10)
        
if temp <= 50:
    print("BOILER FAILURE TOO COLD!",timestamp)
    send2()
    time.sleep(10)
else:
    print("Temp OK")
    
time.sleep(15)
exit()
