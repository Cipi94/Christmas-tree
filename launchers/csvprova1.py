import csv
import sys
import time


with open('carol.csv', 'rb') as f:
  seq_data = f.readlines()
  for i in range(len(seq_data)):
    seq_data[i] = seq_data[i].rstrip()

start_time = int(round(time.time()*1000))
step = 1
print start_time
while True :
  next_step = seq_data[step].split(",");
  next_step[1] = next_step[1].rstrip()
  cur_time = int(round(time.time()*1000)) - start_time

  # time to run the command
  if int(next_step[0]) <= cur_time:

    print (next_step);
    
       # if the END command
    if next_step[1].rstrip() == "END":

      break
    step += 1
