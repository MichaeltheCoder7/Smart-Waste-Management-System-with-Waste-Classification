import time
import math
import RPi.GPIO as GPIO

import inference
import lcd

def sensor_setup():
    # Infrared motion sensor setup
    ledPin = 12 # define ledPin
    sensorPin = 11 # define sensorPin
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD) # use PHYSICAL GPIO Numbering
    GPIO.setup(ledPin, GPIO.OUT) # set ledPin to OUTPUT mode
    GPIO.setup(sensorPin, GPIO.IN) # set sensorPin to INPUT mode

    return ledPin, sensorPin

ledPin, sensorPin = sensor_setup()
# Set up lcd screen
lcd_screen = lcd.lcd_setup()

def destroy():
    GPIO.cleanup() # Release GPIO resource


# loop for infrared sensor
def sensor_loop(lcd_screen, ledPin, sensorPin):
    while True:
        if GPIO.input(sensorPin)==GPIO.HIGH:
            GPIO.output(ledPin,GPIO.HIGH) # turn on led
            time.sleep(0.8)
            inference.inference_loop(lcd_screen) # activate inference loop when the sensor sense infrared motion
        else:
            GPIO.output(ledPin,GPIO.LOW) # turn off led
        time.sleep(1) # sleep to save power


# Use interrupt for the sensor
def motion_detected(channel):
    GPIO.output(ledPin, GPIO.HIGH) # turn on led
    time.sleep(0.8)
    inference.inference_loop(lcd_screen) # activate inference loop when the sensor sense infrared motion 
    GPIO.output(ledPin,GPIO.LOW)

GPIO.add_event_detect(sensorPin, GPIO.RISING, callback=motion_detected)


# Main program that runs on raspberry pi
if __name__ == '__main__': 
    print ('Starting...')
    # Set up the infrared motion sensor
    #ledPin, sensorPin = sensor_setup()
    # Set up lcd screen
    #lcd_screen = lcd.lcd_setup()
    try:
        while True:
            time.sleep(1)
        #sensor_loop(lcd_screen, ledPin, sensorPin)
    except KeyboardInterrupt: # Press ctrl-c to end the program.
        destroy()
