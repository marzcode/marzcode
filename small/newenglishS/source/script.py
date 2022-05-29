import itertools
import re, ast
import shutil
import glob
import os
##pt3

dir_list = os.listdir("./")
dir_list.remove("script.py")
dir_list = sorted(dir_list)

n = len(dir_list) -1
l = len(dir_list) -2

append_str = 'n'
n_list = [append_str + sub for sub in dir_list]

while n >= 0:
  with open(dir_list[n]) as f:
    lines = f.read()
  file = open(n_list[n], 'w')
  file.write(lines)
  file.close()
  n -= 2

append_str = 'l'
n_list = [append_str + sub for sub in dir_list]
while l >= 0:
  with open(dir_list[l]) as f:
    lines = f.read()
  file = open(n_list[l], 'w')
  file.write(lines)
  file.close()
  l -= 2

nums = []
for name in sorted(glob.glob('n*')):
  nums.append(name)

lets = []
for name in sorted(glob.glob('l*')):
  lets.append(name)

q = 0
w = len(nums)
while q < w:
    z = len(lets)
    c = 0
    while c < z:
        name = "set" + str([c])
        with open(lets[c]) as l:
          lf = l.read()
        with open(nums[c]) as n:
          nf = n.read()
        moon = lf + nf
        l = moon.replace("\n","").replace(" ","")
        y = len(l)
        n = 3
        t = int(y/n)
        x = "9810203040"
        k = ""
        if (t % len(x)) == 0:
          y = t / len(x)
          k = x * int(y)
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
        n = 3
        l = [l[i:i+n] for i in range(0, len(l), n)]
        k = sorted((b:=sorted(range(len(k)), key=lambda x: k[x])), key=lambda x: b[x])
        k = list(reversed(k))
        st = [x for _,x in sorted(zip(k,l))]
        s = "".join(st)
        s1 = s[:len(s)//2]
        s2 = s[len(s)//2:]
        with open(lets[c], 'w') as outfile:
          outfile.write(s1)
        with open(nums[c], 'w') as outfile:
          outfile.write(s2)
        c += 1
    nums.append(nums.pop(0))
    q += 1


beep = "rm x* && mkdir jum && mv l* n* jum "
print(beep)
cmd = os.popen(beep)
print(cmd.read())
print(cmd.close())

beep = "cd jum && rename 's/.{1}(.*)/$1/' * && mv x* ../"
print(beep)
cmd = os.popen(beep)
print(cmd.read())
print(cmd.close())

beep = "rm -d jum && prename 's/^/t-/' x*"
print(beep)
cmd = os.popen(beep)
print(cmd.read())
print(cmd.close())

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


