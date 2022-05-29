from string import ascii_lowercase
from itertools import product
import os
import ast

with open("core") as f:
    lines = f.read().split()
x = 0
i = len(lines)
df=open('format','w')
while i > 0:
  s = lines[x]
  res = ast.literal_eval(s)
  del res[2::4]
  del res[2::3]
  string1=" "
  df.write(string1.join(res))
  df.write('\n')
  i -= 1
  x += 1
df.close()

with open("format", 'r') as cr2:
    for count, line in enumerate(cr2):
        pass
nm = count + 1

#print(nm)

clkd = nm*3 
def make_patterns(n):
  letters_iter = product(ascii_lowercase, ascii_lowercase)
  return [
    f'x{a}{b}'
    for _, (a, b) in zip(range(n), letters_iter)
  ]

orig = ' '.join(make_patterns(clkd))
orig = orig.replace(" ","! ")
spl = orig.split(" ") 
orig = "\n".join(["".join(spl[i:i+3]) for i in range(0,len(spl),3)])+"!"
orig = orig.replace("!"," ")
f1 = open("Orig", "w")
f1.write(orig)
f1.close()

with open("nonecor1") as cr3:
    mn2 = cr3.read()

n1 = nm*mn2.strip()

r1 = n1.replace('|n','|\nn')

f1 = open("d1", "w")
f1.write(r1)
f1.close()


with open("format") as cr4:
    mn3 = cr4.read()

r2 = mn3.replace(' ','\n').replace('\n\n','\n').strip()

f3 = open("d2", "w")
f3.write(r2)
f3.close()


with open("nonecor3") as cr5:
    mn4 = cr5.read()

n2 = nm*mn4.strip()

r3 = n2.replace(')|',')\n|')

f3 = open("d3", "w")
f3.write(r3)
f3.close()


c2 = "paste d1 d2 d3 > d4"
cm2 = os.popen(c2)
print(cm2.read())


with open("d4") as cr6:
    mn5 = cr6.read()

r4 = mn5.replace("	","").replace("\n","").replace(")none",")\nnone").replace("\n","\n#\n")

r5 = "\n" + r4 + "\n"

f4 = open("r1", "w")
f4.write(r5)
f4.close()

c3 = "rm d* format"
cm3 = os.popen(c3)
print(cm3.read())



bc1 = "cut -d, -f$(seq -s, 3 4 300) core > db1"
cm1 = os.popen(bc1)
print(cm1.read())

bc2 = "cut -d, -f$(seq -s, 4 4 300) core > db2"
cm2 = os.popen(bc2)
print(cm2.read())

with open("db1") as cr1:
    mn1 = cr1.read()
r1 = mn1.replace("[","").replace("]","").replace(","," ").replace("'","").replace(" ","!")
f1 = open("d1", "w")
f1.write(r1)
f1.close()

with open("db2") as cr2:
    mn2 = cr2.read()

r2 = mn2.replace("[","").replace("]","").replace(","," ").replace("'","").replace(" ","!")

f2 = open("d2", "w")
f2.write(r2)
f2.close()

with open("core", 'r') as cr3:
    for count, line in enumerate(cr3):
        pass
nm = count + 1

with open("pa") as cr4:
    mn4 = cr4.read()
n4 = nm*mn4
r4 = n4.strip()
f4 = open("da1", "w")
f4.write(r4)
f4.close()

with open("pb") as cr5:
    mn5 = cr5.read()
n5 = nm*mn5
r5 = n5.strip()
f5 = open("da2", "w")
f5.write(r5)
f5.close()

bc3 = "paste d1 da1 > dl1"
cm3 = os.popen(bc3)
print(cm3.read())

with open("dl1") as cr6:
    mn6 = cr6.read()
r6 = mn6.replace("	","")
f6 = open("d1", "w")
f6.write(r6)
f6.close()

bc4 = "paste d2 da2 > dl2"
cm4 = os.popen(bc4)
print(cm4.read())

with open("dl2") as cr7:
    mn7 = cr7.read()
r7 = mn7.replace("	","")
f7 = open("d2", "w")
f7.write(r7)
f7.close()

def solve(a, b, k):
    s = ""
 
    la = len(a)
 
    lb = len(b)
    l = la + lb
 
    indexa = indexb = 0
     
    while l:
        pa = pb = 0
 
        if la - indexa >= k:
            s = s + a[indexa : indexa + k]
            indexa = indexa + k
            pa = k

        elif la - indexa < k and la - indexa:
            s = s + a[indexa : la]
            pa = la - indexa
            indexa = la

        elif indexa >= la:
            pa = 0
 
        if lb - indexb >= k:
            s = s + b[indexb : indexb+k]
            pb = k
            indexb = indexb + k
 
        elif lb - indexb < k and lb - indexb:
            s = s + b[indexb : lb]
            pb = lb - indexb
            indexb = lb
 
        elif indexb >= lb:
            pb = 0
        l = l - pa - pb
         
    s1 = open("dear", "w")
    s1.write(s)
    s1.close()

with open("d1") as bc6:
    a = bc6.read()

with open("d2") as bc7:
    b = bc7.read()

k = 4
solve(a, b, k)

with open("dear") as cr8:
    mn8 = cr8.read()
n8 = mn8.strip()
r8 = n8.replace('\n','').replace('EEEEEEE','\n').replace('!',' ')
f8 = open("deer", "w")
f8.write(r8)
f8.close()

with open("dear", 'r') as pt1:
    for count, line in enumerate(pt1):
        pass
pn1 = count + 1

with open("chufcor1") as pt2:
    pm2 = pt2.read()

u2 = nm*pm2.strip()

h2 = u2.replace('"|c','"|\nc')

q2 = open("d1", "w")
q2.write(h2)
q2.close()

with open("deer") as pt3:
    pm3 = pt3.read()

h3 = pm3.replace(' ','\n').strip()

q3 = open("d2", "w")
q3.write(h3)
q3.close()

with open("chufcor3") as pt4:
    pm4 = pt4.read()

u4 = nm*pm4

h4 = u4.replace(')|',')\n|').replace("\n\n","\n")

q4 = open("d3", "w")
q4.write(h4)
q4.close()

bc5 = "paste d1 d2 d3 > d4"
cm5 = os.popen(bc5)
print(cm5.read())

with open("d4") as pt5:
    pm5 = pt5.read()

h5 = pm5.replace("	","").replace("\n","").replace(")chuff",")\nchuff")

q5 = open("r2", "w")
q5.write(h5)
q5.close()

bc6 = "rm d*"
cm6 = os.popen(bc6)
print(cm6.read())

bce = "chmod +x ./CC && cp CC Orig r1 r2 end.txt start.txt splitup.py grow.py ../ && cd ../ && python3 splitup.py"
cmd = os.popen(bce)
print(cmd.read())



