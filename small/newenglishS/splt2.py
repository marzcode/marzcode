from itertools import cycle
import pickle
import random
import string
import math
import ast
import os


def round_down(n, decimals=0):
  multiplier = 10 ** decimals
  return math.floor(n * multiplier) / multiplier
str = open('temp/based.txt', 'r').read()
v_ln = len(str)
v_dv = v_ln / 567
v_rd = round(round_down(v_dv))
v_ml = v_rd * 567
v_mi = v_ln - v_ml
v_mu = 567 * (3 - ((v_rd + 1)%3))
if v_mi == 0:
  v_mi += 567
#v_nln = 567 - v_mi + v_mu
v_nln = v_mu - v_ln
v_con = "% s" % v_nln

def randomword(length):
 letters = "abcdefghijklmnop"
 return ''.join(random.choice(letters) for i in range(length))

with open('waste/TopUp', 'w') as file:
  file.write(randomword(v_nln))

v_cmnd = "paste temp/based.txt waste/TopUp > waste/rdy"
print(v_cmnd)
command = os.popen(v_cmnd)
print(command.read())
print(command.close())

with open(r'waste/rdy', 'r') as file:
  data = file.read()
  data = data.replace("\n","").replace("	","")

with open(r'waste/sorted', 'w') as file:
  file.write(data)

v_fld = "fold -w63 waste/sorted > waste/xnew.txt && split -l 9 waste/xnew.txt"
command = os.popen(v_fld)
print(command.read())
print(command.close())

#with open(r"temp/dicts", 'r+') as fd:
#  dl = fd.readlines()
#  fd.seek(0)
#  fd.truncate()
#  fd.writelines(dl[int(groups):])

#with open(r"temp/master", 'r+') as fm:
#  ml = fm.readlines()
#  fm.seek(0)
#  fm.truncate()
#  fm.writelines(ml[output_count+1:])

beep = "mkdir mix && mv x* mix/ && cp source/script.py mix/"
# && cd mix && python3 script.py && rm s* && cp -r * ../"
cmnd = os.popen(beep)
print(cmnd.read())

#beep = "python3 numberset.py"
#cmnd = os.popen(beep)
#print(cmnd.read())












