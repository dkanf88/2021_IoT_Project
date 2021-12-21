import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#GPIO 7개 핀 설정(A~G)
#               A   B   C   D   E   F   G              
SEGMENT_PINS = [25, 24, 14, 18, 23, 16, 20]

for segment in SEGMENT_PINS:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, GPIO.LOW)

#LED, 피에조부저 및 음계 PIN number
LED_PIN1 = 19
SWITCH_PIN1 = [4, 27, 5, 12]
LED_PIN2 = 26
SWITCH_PIN2 = [17, 22, 6]
buzzer = 21
do = 4
re=17
mi = 27
fa = 22
sol = 5
ra = 6
si = 12
scale=[261, 294, 329, 349, 392, 440, 493]

GPIO.setmode(GPIO.BCM)
GPIO.setup(do,GPIO.IN)
GPIO.setup(re,GPIO.IN)
GPIO.setup(mi,GPIO.IN)
GPIO.setup(fa,GPIO.IN)
GPIO.setup(sol,GPIO.IN)
GPIO.setup(ra,GPIO.IN)
GPIO.setup(si,GPIO.IN)
GPIO.setup(buzzer, GPIO.OUT)

GPIO.setup(LED_PIN1, GPIO.OUT)
GPIO.setup(LED_PIN2, GPIO.OUT)

p=GPIO.PWM(buzzer, 600)
p.start(0)

# Common Cathode : ON -> HIGH, OFF -> LOW
data= {'7':[1,1,1,0,0,0,0]} #7
     


try:
    while True:
        for i in range(3): #0~2
            GPIO.output(SEGMENT_PINS[i],data['7'][i]) #7출력

        if GPIO.input(do)==GPIO.HIGH:
            p.ChangeFrequency(scale[0])
            p.ChangeDutyCycle(10)
            GPIO.output(LED_PIN1, 1)
            
        elif GPIO.input(re)==GPIO.HIGH:
            p.ChangeFrequency(scale[1])
            p.ChangeDutyCycle(10)
            GPIO.output(LED_PIN2, 1)
           
        elif GPIO.input(mi)==GPIO.HIGH:
            p.ChangeFrequency(scale[2])
            p.ChangeDutyCycle(10)
            GPIO.output(LED_PIN1, 1)

        elif GPIO.input(fa)==GPIO.HIGH:
            p.ChangeFrequency(scale[3])
            p.ChangeDutyCycle(10)
            GPIO.output(LED_PIN2, 1)

        elif GPIO.input(sol)==GPIO.HIGH:
            p.ChangeFrequency(scale[4])
            p.ChangeDutyCycle(10)
            GPIO.output(LED_PIN1, 1)

        elif GPIO.input(ra)==GPIO.HIGH:
            p.ChangeFrequency(scale[5])
            p.ChangeDutyCycle(10)
            GPIO.output(LED_PIN2, 1)

        elif GPIO.input(si)==GPIO.HIGH:
            p.ChangeFrequency(scale[6])
            p.ChangeDutyCycle(10)
            GPIO.output(LED_PIN1, 1)

        else:
            p.ChangeDutyCycle(0)
            

        GPIO.output(LED_PIN1, 0)
        GPIO.output(LED_PIN2, 0)

finally:
    p.stop()
    GPIO.cleanup()
    print('cleanup and exit')
       
        
