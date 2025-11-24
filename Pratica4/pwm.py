import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
gpio.setup(23,gpio.OUT)
gpio.setwarnings(False)

pwm = gpio.PWM(23,100)
pwm.start(0)

dc = 0

while True:

	pwm.ChangeDutyCycle(dc)
	time.sleep(0.05)
	dc = dc+1
	if dc == 100:
		dc = 0
gpio.cleanup()

