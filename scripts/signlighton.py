#!/usr/bin/env python
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(19,GPIO.OUT)



GPIO.output(19, False)
print("SIGN LIGHT ON")
exit()

