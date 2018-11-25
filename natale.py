#!/usr/bin/env python
#

import RPi.GPIO as GPIO, time
import sys
import signal
import time
import random


# Defining signal interrupt handler
def signal_term_handler(signal, frame):
	print("Someone is trying to kill me")
	print('Cleaning up the GPIOs')
	GPIO.cleanup()
	sys.exit()


signal.signal(signal.SIGTERM, signal_term_handler)
signal.signal(signal.SIGINT, signal_term_handler)

pin_map = [0,11,12,13,15,16,18,22,7]

# Defines the mapping of logical mapping to physical mapping
# 1 - 5 are lights from top to bottom on tree
# 6 = RED
# 7 = GREEN
# 8 = BLUE
logical_map = [i for i in range(9)]

# Setup the board
GPIO.setmode(GPIO.BOARD)
for i in range(1,9):
	GPIO.setup(pin_map[i], GPIO.OUT)
time.sleep(2.0)

while True :
	for i in range (1,6):
		GPIO.output(pin_map[logical_map[i]],1)
		if(i==1):
			GPIO.output (pin_map[logical_map[5]],0)
		else:
			GPIO.output (pin_map[logical_map[i-1]],0)
		time.sleep (0.2)
	GPIO.output (pin_map[logical_map[6]],random.choice([0,1]))