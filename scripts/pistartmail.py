#!/usr/bin/env python
# Import smtplib to provide email functions
import smtplib
from datetime import datetime, time
now = datetime.now()
now_time = now.time()
import time as t
import os
# Import the email modules
from email.mime.text import MIMEText
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)

  
# Define email addresses to use
addr_to   = 'TO EMAIL ADDRESS'
addr_from = 'FROM EMAIL ADDRESS'
  
# Define SMTP email server details
smtp_server = 'MAIL SERVER'
smtp_user   = 'USER NAME'
smtp_pass   = 'PASSWORD'
  
# Construct email
msg = MIMEText('')
msg['To'] = addr_to
msg['From'] = addr_from
msg['Subject'] = 'THERMOSTAT PI JUST RESTARTED'
  
# Send the message via an SMTP server
def send1():
    s = smtplib.SMTP(smtp_server)
    s.login(smtp_user,smtp_pass)
    s.sendmail(addr_from, addr_to, msg.as_string())
    s.quit()
    print ("sent")


GPIO.output(12, True)
GPIO.output(13, True)
GPIO.output(16, True)
GPIO.output(19, True)  
t.sleep(2)
send1()
print ("waiting 240 seconds to send again.. Just incase router is rebooting")
t.sleep(240)
send1()
print("closing window")
t.sleep(2)
exit()
