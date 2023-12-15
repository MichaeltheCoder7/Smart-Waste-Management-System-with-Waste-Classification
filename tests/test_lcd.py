from lcd_api import LcdApi
from i2c_lcd import I2cLcd
import time
import math

# LCD setup
I2C_ADDR = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16
 
lcd = I2cLcd(1, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

text = 'Please dispose in hazardous waste facility! Not here!'

def long_text(lcd, text):
    tmp = text                     # Get the display information
    for i in range(0, len(text)-15):
        lcd.putstr("Recycle")
        lcd.move_to(0,1)           # Position cursor
        lcd.putstr(tmp[:16])       # Display one by one on the second line
        tmp = tmp[1:]
        time.sleep(0.6)            # Delay 600ms
        lcd.clear()                # Clear display

# display text on two lines
def display_text(lcd, category_name, score, text):
    lcd.putstr(f"{category_name}:{100 * score: .2f}%")
    time.sleep(1.2)
    tmp = text
    # show 32 characters at a time
    for i in range(0, math.ceil(len(text) / 32)):
        lcd.move_to(0, 0)
        if len(tmp) >= 32:
            lcd.putstr(tmp[:32])
        else:
            lcd.putstr(tmp)
        tmp = tmp[32:]
        time.sleep(2.5)
        lcd.clear()
        
if __name__ == '__main__':
    long_text(lcd, text)
    #display_text(lcd, "Recycle", 0.98, text)

