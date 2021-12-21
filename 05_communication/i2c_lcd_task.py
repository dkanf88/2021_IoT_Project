# from lcd import drivers
# import time
# import datetime
# import Adafruit_DHT

# sensor = Adafruit_DHT.DHT11
# pin = 4
# display = drivers.Lcd()
# now = datetime.datetime.now()
# try:
#     print("Writing to display")
#     #display.lcd_display_string("Hello, World!", 1)
#     while True:
#         h, t=Adafruit_DHT.read_retry(sensor, pin)
#         if h is not None and t is not None:
#           display.lcd_display_string(now.strftime("%x%X"), 1)
#           display.lcd_display_string("{0:0.1f}*C, {1:0.1f}".format(t,h), 2)
#         else :
#             print('Read error')
#         time.sleep(1)
#         # display.lcd_display_string((t,h), 2)
        
# finally:
#     print("Cleaning up!")
#     display.lcd_clear()

import Adafruit_DHT
from lcd import drivers
import datetime
import time

display = drivers.Lcd()
sensor = Adafruit_DHT.DHT11
PIN = 4

try:
    while True:
        now = datetime.datetime.now()
        display.lcd_display_string(now.strftime("%x%X"), 1)
        
        humidity, temperature = Adafruit_DHT.read_retry(sensor, PIN)
        if humidity is not None and temperature is not None:
            display.lcd_display_string(f"%.1f*C, %.1f%%" % (temperature,humidity), 2)
        else:
            print('Read error')


finally:
    print("Cleaning up!")
    display.lcd_clear()