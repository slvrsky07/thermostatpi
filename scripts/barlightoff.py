#!/usr/bin/env python
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.OUT)



GPIO.output(16, True)
print("BAR LIGHT OFF")
exit()

