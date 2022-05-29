import itertools
import shutil
import glob
import os

dir_list = os.listdir("./")
dir_list.remove("script.py")
dir_list = sorted(dir_list)

append_str = 't-'
n_list = [append_str + sub for sub in dir_list]

y = len(dir_list)
l = (n_list)

n = 1
t = int(y/n)
x = "120"
k = ""

if (t % len(x)) == 0:
  n = t / len(x)
  k = x * int(n)
else:
  n = t % len(x)
  core = int((t - n) / len(x))
  x = core*(x)
  split_string = [x[i:i+n] for i in range(0, len(x), n)]
  list1 = split_string[0:1]
  string1=""
  for i in list1:
    string1=string1+i
  k = x + string1

k = sorted((b:=sorted(range(len(k)), key=lambda x: k[x])), key=lambda x: b[x])
k = list(reversed(k))
k = [1 + i for i in sorted(range(len(k)), key=k.__getitem__)]
k = sorted((b:=sorted(range(len(k)), key=lambda x: k[x])), key=lambda x: b[x])

n_list = [x for _,x in sorted(zip(k,l))]
t = int(y-1)

while t >= 0:
  print(dir_list[t])
  with open(dir_list[t]) as f:
    lines = f.read()
  print(n_list[t])
  file = open(n_list[t], 'w')
  file.write(lines)
  file.close()
  t -= 1

def grouper(S, n):
  iterator = iter(S)
  while True:
    items = list(itertools.islice(iterator, n))
    if len(items) == 0:
      break
    yield items

beep = "rm x*"
cmnd = os.popen(beep)
print(cmnd.read())

beep = "rename -v 's/t-//' t*"
cmnd = os.popen(beep)
print(cmnd.read())

beep = "cat x* > sbase"
cmnd = os.popen(beep)
print(cmnd.read())

with open("sbase") as cr6:
    mn6 = cr6.read()
r6 = mn6.replace("\n","")
f6 = open("based.txt", "w")
f6.write(r6)
f6.close()

beep = "cp based.txt ../../../Decode"
cmnd = os.popen(beep)
print(cmnd.read())

beep = "cd ../../../Decode && python3 Degoed.py"
cmnd = os.popen(beep)
print(cmnd.read())

