from flask import Flask
import RPi.GPIO as GPIO

LED_PIN = 4
LED_PIN2 = 5

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(LED_PIN2, GPIO.OUT)

@app.route("/")
def hello_world():
    return ''' 
    <p>Hello, Flask!</p>
    <a href ="/red/led/on">RED LED ON</a>
    <a href ="/red/led/off"> RED LED OFF</a>
    <a href ="/blue/led/on">BLUE LED ON</a>
    <a href ="/blue/led/off"> BLUE LED OFF</a>
    '''

@app.route("/<color>/led/<cmd>")
def led_op(cmd,color):
    if cmd == "on":
        if color == "red":
            GPIO.output(LED_PIN, GPIO.HIGH)
            return ''' 
            <p>RED LED ON</p>
            <a href ="/">Go Home</a>
            '''
        elif color == "blue":
            GPIO.output(LED_PIN2, GPIO.HIGH)
            return ''' 
            <p>BLUE LED ON</p>
            <a href ="/">Go Home</a>
            '''
    elif cmd == "off":
        if color == "red":
            GPIO.output(LED_PIN, GPIO.LOW)
            return ''' 
            <p>RED LED OFF</p>
            <a href ="/">Go Home</a>
            '''
        elif color == "blue":
            GPIO.output(LED_PIN2, GPIO.LOW)
            return ''' 
            <p>BLUE LED OFF</p>
            <a href ="/">Go Home</a>
            '''


if __name__ == "__main__":
    try:
        app.run(host = "0.0.0.0") 
    finally:
        GPIO.cleanup()
    
