import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN)

while True:
    input_value = gpio.input(17)
    if input_value == False:
        print input_value
        print('The button has been pressed...')
        while input_value == False:
            input_value = gpio.input(17)
