import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)
prev_input = 0


while True:
	input_value = GPIO.input(17)
        print input_value
        print('The button has been pressed...')
