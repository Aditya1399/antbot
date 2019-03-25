'''
Team ID :		183
Author's list : 	Mohit,Mridul Baweja
Filename: 		Pick and Place(temporary)
Theme:			Theme name -- eYRC#AB
Functions:		SetAngle(),Snap()
Global Variables:	pwm
'''
import time
from time import sleep
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)   # SERVO connection
pwm = GPIO.PWM(7,50)     # PWM for servo
pwm.start(0) 
def SetAngle(angle):
   duty = angle / 18 + 2
   GPIO.output(7, True)
   pwm.ChangeDutyCycle(duty)
   sleep(1)
   GPIO.output(7, False)
   pwm.ChangeDutyCycle(0)
while(1):
    
  SetAngle(40)
  sleep(5)
  SetAngle(75)
  sleep(5)
