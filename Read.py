#!/usr/bin/env python

import RPi.GPIO as GPIO
import SimpleMFRC522
import time
reader = SimpleMFRC522.SimpleMFRC522()

while True:
        id, text = reader.read()
        if(id!=None):
            print(id)
        time.sleep(5)
"""try:
        id, text = reader.read()
        print(id)
        print(text)
finally:
        GPIO.cleanup()"""
