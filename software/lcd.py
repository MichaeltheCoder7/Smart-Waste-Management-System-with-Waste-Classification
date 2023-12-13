import time
import math
from lcd_api import LcdApi
from i2c_lcd import I2cLcd

# LCD setup
def lcd_setup():
    I2C_ADDR = 0x27
    I2C_NUM_ROWS = 2
    I2C_NUM_COLS = 16
     
    lcd = I2cLcd(1, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)
    return lcd


# scrolling text in second line for LCD
def scroll_text(lcd, category_name, score, text):
    tmp = text                     # Get the display information
    for i in range(0, len(text)):
        lcd.putstr(f"{category_name}:{100 * score: .2f}%")
        lcd.move_to(0,1)           # Position cursor
        lcd.putstr(tmp[:16])       # Display one by one on the second line
        tmp = tmp[1:]
        time.sleep(0.6)            # Delay 600ms
        lcd.clear()                # Clear display


# display text on two lines for LCD
def display_text(lcd, category_name, score, text):
    lcd.putstr(f"{category_name}:{100 * score: .2f}%")
    time.sleep(1.5)
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

# create customized message to user based on category
def custom_feedback(lcd, category_name, score, label_name):
    if label_name == "battery":
        display_text(lcd, category_name, score, "Please dispose  in hazardous wa-ste facility!   Not here!")

    elif label_name == "biological":
        display_text(lcd, category_name, score, "It will decompo-se naturally andenrich the soil!")

    elif label_name == "brown-glass":
        display_text(lcd, category_name, score, "Please empty it before disposal!")

    elif label_name == "cardboard":
        display_text(lcd, category_name, score, "Please dispose  of any food lef-tovers in the  compost bin if  present!")

    elif label_name == "clothes":
        display_text(lcd, category_name, score, "Please consider donating them if they are in    good condition.")

    elif label_name == "green-glass":
        display_text(lcd, category_name, score, "Please empty it before disposal!")

    elif label_name == "metal":
        display_text(lcd, category_name, score, "They can be mel-ted down and re-shaped into new products!")

    elif label_name == "paper":
        display_text(lcd, category_name, score, "It can be reused to make new pa-per products!")

    elif label_name == "plastic":
        display_text(lcd, category_name, score, "Please empty it before disposal!")

    elif label_name == "shoes":
        display_text(lcd, category_name, score, "Please consider donating them if in good condit-ion.")

    elif label_name == "trash":
        display_text(lcd, category_name, score, "Anything that   can not be recy-cled or compost-ed goes here!")
                    
    else:
        display_text(lcd, category_name, score, "Please empty it before disposal!")

    lcd.move_to(0,0)    
