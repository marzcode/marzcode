import re, ast
import glob
import os
 
path = "./"
dir_list = sorted(os.listdir(path)) 
dir_list.remove("br.py")

n_list = ["txaa","txab","txac","txad"]

t = 0
while t < 4:
  with open(dir_list[t]) as f:
    lines = f.read()
  file = open(n_list[t], 'w')
  file.write(lines)
  file.close()
  t += 1

beep = "rm x*"
cmnd = os.popen(beep)
print(cmnd.read())

beep = "rename -v 's/t//' t*"
cmnd = os.popen(beep)
print(cmnd.read())

for name in glob.glob("x*"):
  with open(name) as f:
    lines = f.read()
  lines=lines.replace("\n","")
  s = ' '.join(lines[i:i + 3] for i in range(0, len(lines), 3))
  with open(name, 'w') as outfile:
    outfile.write(s)
