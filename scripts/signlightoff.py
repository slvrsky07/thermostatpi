#!/usr/bin/env python
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(19,GPIO.OUT)



GPIO.output(19, True)
print("SIGN LIGHT OFF")
exit()

