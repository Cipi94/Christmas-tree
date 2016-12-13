import sys

logical_map = [0 for i in range(9)]
with open("setup.txt",'r') as f:
  data = f.readlines()
  for i in range(8):
    logical_map[i+1] = int(data[i])
	
print (logical_map)