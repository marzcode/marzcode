import time
import os
import glob

dir_list = os.listdir('./')
dir_list.remove("st.py")
dir_list = sorted(dir_list)

for i in dir_list:
  with open(i, 'r') as f:
    lines = f.read()
  sexy = lines.replace("['","").replace("', '"," ").replace("']","")
  with open(i, 'w') as g:
    g.write(sexy+"\n")

dir_list = os.listdir('./')
dir_list.remove("st.py")
dir_list = sorted(dir_list)
my_string = " "
dir_list = [s + my_string for s in dir_list]
l = len(dir_list)
c = l / 4
t1 = 0
t2 = 1
t3 = 2
t4 = 3

while c > 0:
  d1 = dir_list[t1]
  d2 = dir_list[t2]
  d3 = dir_list[t3]
  d4 = dir_list[t4]
  col = str(int(c)) 
  message = "cat " + d1 + d2 + d3 + d4 + " > " + col + ".txt"
  command = os.popen(message)
  t1 += 4
  t2 += 4
  t3 += 4
  t4 += 4
  c-= 1

message = "cat *.txt > master"
command = os.popen(message)
time.sleep(1.)

message = "awk '{print $NF}' master > dict.txt"
command = os.popen(message)
time.sleep(1.)

file = open("dict.txt", 'r')
lines = file.read()
our_list = lines.splitlines()
chunked_list = list()
chunk_size = 10
for i in range(0, len(our_list), chunk_size):
  chunked_list.append(our_list[i:i+chunk_size])
final = str(chunked_list).replace("[[","[").replace("]]","]").replace("], [","]\n[")
up = open("dicts", 'w')
up.write(final)
up.close()

message = "cp master dicts ../"
command = os.popen(message)
time.sleep(.1)
message = "rm *"
command = os.popen(message)


