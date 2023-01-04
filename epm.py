import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module


GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
#GPIO.setup(37, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)
#Set Button and LED pins
Button = 40
EPM = 37
#Setup Button and LED
GPIO.setup(Button,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(EPM,GPIO.OUT)
#flag = 0

while True:
    button_state = GPIO.input(Button)
    print(button_state)
    if button_state == 0:
        GPIO.output(EPM,GPIO.HIGH)
    else:
        GPIO.output(EPM,GPIO.LOW)
    sleep(1)
"""
while True: # Run forever
 GPIO.output(37, GPIO.HIGH) # Turn on
 sleep(5) # Sleep for 1 second
 GPIO.output(37, GPIO.LOW) # Turn off
 sleep(5) # Sleep for 1 second
 """