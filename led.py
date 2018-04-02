import RPi.GPIO as GPIO
import time

LED_POWER=12
RED = 4
GREEN = 3
BLUE = 2
FREQ = 100

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_POWER, GPIO.OUT) #LED Power
GPIO.setup(RED, GPIO.OUT) #RED
GPIO.setup(GREEN, GPIO.OUT) #GREEN
GPIO.setup(BLUE, GPIO.OUT) #BLUE

LED_R = GPIO.PWM(RED, FREQ)
LED_G = GPIO.PWM(GREEN,FREQ)
LED_B = GPIO.PWM(BLUE, FREQ)
LED_R.start(0)
LED_G.start(0)
LED_B.start(0)

LED_R.ChangeDutyCycle(10)
LED_G.ChangeDutyCycle(10)
LED_B.ChangeDutyCycle(50)



time.sleep(5)
GPIO.cleanup()
