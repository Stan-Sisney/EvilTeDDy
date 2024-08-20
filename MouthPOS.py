import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

def n ():
# lower jaw
 kit.servo[8].angle = 0
#upper Jaw
 kit.servo[4].angle = 0

n ()
time.sleep(2)

def cd ():
# lower jaw
 kit.servo[8].angle = 90
#upper Jaw
 kit.servo[4].angle = 180

cd ()

#move serovs to x position