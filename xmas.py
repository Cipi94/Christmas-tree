#!/usr/bin/env python
#
# Command Line usage:
#   xmas.py <input sequence> <audio file>

import RPi.GPIO as GPIO, time
import sys
import time
import pygame
import random

pin_map = [0,11,12,13,15,16,18,22,7]

# Defines the mapping of logical mapping to physical mapping
# 1 - 5 are lights from top to bottom on tree
# 6 = RED
# 7 = GREEN
# 8 = BLUE

# Setup the board
GPIO.setmode(GPIO.BOARD)
for i in range(1,9):
  GPIO.setup(pin_map[i], GPIO.OUT)
time.sleep(2.0);

GPIO.output(7, True)

# Open the setup config file and parse it to determine 
# how GPIO1-8 are mapped to logical 1-8
'''logical_map = [0 for i in range(9)]
with open("setup.txt",'r') as f:
  data = f.readlines()
  for i in range(8):
    logical_map[i+1] = int(data[i])'''
logical_map = [0,1,2,3,4,5,6,7,8]

# Open the input sequnce file and read/parse it
with open(sys.argv[1],'r') as f:
  seq_data = f.readlines()
  for i in range(len(seq_data)):
    seq_data[i] = seq_data[i].rstrip()

# Current light states
lights = [False for i in range(8)]

# Start sequencing
start_time = int(round(time.time()*1000))
step       = 1 #ignore the header line

# Load and play the music
pygame.mixer.pre_init(44100,-16,2, 1024)
pygame.mixer.init()
pygame.mixer.music.load(sys.argv[2])
pygame.mixer.music.play()
 
while True :
  next_step = seq_data[step].split(",");
  next_step[1] = next_step[1].rstrip()
  cur_time = int(round(time.time()*1000)) - start_time

  # time to run the command
  if int(next_step[0]) <= cur_time:

    print (next_step);
    # if the command is Relay 1-8 
    if next_step[1] >= "1" and next_step[1] <= "8":

      # change the pin state
      if next_step[2] == "1":
        GPIO.output(pin_map[logical_map[int(next_step[1])]],True)
      else:
        GPIO.output(pin_map[logical_map[int(next_step[1])]],False)

       # if the END command
    if next_step[1].rstrip() == "END":
      for i in range(1,9):
        GPIO.output(pin_map[logical_map[i]],False)
      #print ('Cleaning up the GPIOs')
      #GPIO.cleanup()
      break
    step += 1

print ('Cleaning up the GPIOs')
GPIO.cleanup()