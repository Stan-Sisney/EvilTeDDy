import time
from adafruit_servokit import ServoKit

# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=16)

# lower jaw
kit.servo[8].angle = 180
time.sleep(1)
kit.servo[8].angle = 0
time.sleep(1)

#upper Jaw
kit.servo[4].angle = 180
time.sleep(1)
kit.servo[4].angle = 0
time.sleep(1)

#eyes
kit.servo[7].angle = 180
time.sleep(1)
kit.servo[7].angle = 0
# Test