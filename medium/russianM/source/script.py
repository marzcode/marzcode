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

#REVERSE CODE
#k = [1 + i for i in sorted(range(len(k)), key=k.__getitem__)]
#k = sorted((b:=sorted(range(len(k)), key=lambda x: k[x])), key=lambda x: b[x])

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

fnames = sorted(glob.glob('t*'))
for i, fnames in enumerate(grouper(fnames, 3)):
  dirname = 'results%d' % i
  os.mkdir(dirname)
  for fname in fnames:
    shutil.move(fname, dirname)