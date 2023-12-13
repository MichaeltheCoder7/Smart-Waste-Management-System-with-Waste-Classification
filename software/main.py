import sensor
import lcd

# Main program that runs on raspberry pi
if __name__ == '__main__': 
    print ('Starting...')
    # Set up the infrared motion sensor
    ledPin, sensorPin = sensor.sensor_setup()
    # Set up lcd screen
    lcd_screen = lcd.lcd_setup()
    try:
        sensor.sensor_loop(lcd_screen, ledPin, sensorPin)
    except KeyboardInterrupt: # Press ctrl-c to end the program.
        sensor.destroy()
