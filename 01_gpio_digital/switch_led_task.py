import RPi.GPIO as GPIO

LED_PIN1 = 19
SWITCH_PIN1 = 17
LED_PIN2 = 13 
SWITCH_PIN2 = 27
LED_PIN3 = 6
SWITCH_PIN3 = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN1, GPIO.OUT)
GPIO.setup(LED_PIN2, GPIO.OUT)
GPIO.setup(LED_PIN3, GPIO.OUT)
GPIO.setup(SWITCH_PIN1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SWITCH_PIN2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SWITCH_PIN3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


try:
    while True:
        val = GPIO.input(SWITCH_PIN1) 
        print(val)
        GPIO.output(LED_PIN1, val) 
        val2 = GPIO.input(SWITCH_PIN2) 
        print(val2)
        GPIO.output(LED_PIN2, val2)
        val3 = GPIO.input(SWITCH_PIN3) 
        print(val3)
        GPIO.output(LED_PIN3, val3)


finally:
    GPIO.cleanup()
    print('cleanup and exit')