# from lcd import drivers
# import time
# display = drivers.Lcd()

# try:
#     print("Writting to display")
#     display.lcd_display_string("Hello, World!!", 1)
#     while True:
#         display.lcd_display_string("** WELCOME **", 2)
#         time.sleep(2)
#         display.lcd_display_string("   WELCOME   ", 2)
#         time.sleep(2)

# finally:
#     print("Cleaning up!")
#     display.lcd_clear()

from lcd import drivers
import time

display = drivers.lcd()

try:
    print("Writing to display")
    display.lcd_display_string("Hello, World!", 1)
    while True:
        display.lcd_display_string("** WELCOME **", 2)
        time.sleep(2)
        display.lcd_display_string("   WELCOME   ", 2)
        time.sleep(2)
finally:
    print("Cleaning up!")
    display.lcd_clear()
