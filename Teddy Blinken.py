import time
from adafruit_servokit import ServoKit

# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=16)


i = 0
while i < 10:
    # eyes
    kit.servo[2].angle = 180
    time.sleep(.25)
    kit.servo[2].angle = 0
    time.sleep(3)
    print(i)
    if i == 10:
        break
    i += 1