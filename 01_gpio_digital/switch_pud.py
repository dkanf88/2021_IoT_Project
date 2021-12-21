import RPi.GPIO as GPIO
import time

SWITCH_PIN = 23

GPIO.setmode(GPIO.BCM)
#내부풀업저항 사용하기
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        val = GPIO.input(SWITCH_PIN)
        print(val)
        time.sleep(0.1)



finally:
    GPIO.cleanup()
    print('cleanup and exit')
