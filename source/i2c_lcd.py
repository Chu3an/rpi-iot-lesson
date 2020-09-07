import os
import sys
import time

import smbus2
from RPLCD.i2c import CharLCD

# system module setting
sys.modules['smbus'] = smbus2

if __name__ == "__main__":
    # remember to change 'address' to your address
    lcd = CharLCD('PCF8574', address=0x27, port=1, backlight_enabled=True)
    try:
        print('Press Ctrl+C to stop program.')
        lcd.clear()
        while True:
            lcd.cursor_pos = (0, 0)
            lcd.write_string(time.strftime(" %Y/%m/%d %a"))
            lcd.cursor_pos = (1, 0)
            lcd.write_string(time.strftime("    %H:%M:%S"))
            time.sleep(0.5)
    except KeyboardInterrupt:
        print('Program closed.')
    finally:
        lcd.clear()
