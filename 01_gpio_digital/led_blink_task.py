import RPi.GPIO as GPIO
import time

LED_PIN1 = 22
GPIO.setmode(GPIO.BCM) #GPIO.BCM or GPIO.BOARD
GPIO.setup(LED_PIN1, GPIO.OUT) #GPIO.IN
LED_PIN2 = 27
GPIO.setup(LED_PIN2, GPIO.OUT) #GPIO.IN
LED_PIN3 = 17
GPIO.setup(LED_PIN3, GPIO.OUT) #GPIO.IN

    
GPIO.output(LED_PIN1, GPIO.HIGH) #1
print("led on")
time.sleep(2)
GPIO.output(LED_PIN1, GPIO.LOW) #0 
print("led off")

GPIO.output(LED_PIN2, GPIO.HIGH) #1
print("led on")
time.sleep(2)
GPIO.output(LED_PIN2, GPIO.LOW) #0 
print("led off")

GPIO.output(LED_PIN3, GPIO.HIGH) #1
print("led on")
time.sleep(2)
GPIO.output(LED_PIN3, GPIO.LOW) #0 
print("led off")

GPIO.cleanup() #GPIO 핀상태 초기화