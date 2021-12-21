import RPi.GPIO as GPIO
import time

BUZZER_PIN = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

# PWM 인스턴스 생성
# 주파수 설정(4옥타브 도음 : 262Hz)
pwm = GPIO.PWM(BUZZER_PIN, 262  )
pwm.start(90) #duty cycle(0~100)

#도레미파솔라시도 소리내기

melody =[262, 294, 330, 349, 392, 440, 494]
song = [5, 5, 6, 6, 5, 5, 3,\
        5, 5, 3, 3, 2,\
        5, 5, 6, 6, 5, 5, 3,\
        5, 3, 2, 3, 1]
#학교종이땡땡땡 솔솔라라솔솔미 솔솔미미레 솔솔라라솔솔미 솔미레미도
try:
    for i in range(0,24):
        pwm.ChangeFrequency(melody[song[i]])
        if i==6 or i==11 or i==18 or i==23:
            time.sleep(1.0)

        else:
            time.sleep(0.5)

finally:

  pwm.stop() 
  GPIO.cleanup()