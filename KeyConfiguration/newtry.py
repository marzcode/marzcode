import time
import os

def mixfour(q,r,s,t):
  a,e,i,o = iter(q), iter(r), iter(s), iter(t)
  result = [item for sublist in zip(a,e,i,o) for item in sublist]
  result += [item for item in a]
  result += [item for item in e]
  result += [item for item in i]
  result += [item for item in o]
  return result

def mixeight(a,b,c,d,e,f,g,h):
  z,y,x,w,v,u,t,s = iter(a), iter(b), iter(c), iter(d), iter(e), iter(f), iter(g), iter(h)
  result = [item for sublist in zip(z,y,x,w,v,u,t,s) for item in sublist]
  result += [item for item in z]
  result += [item for item in y]
  result += [item for item in x]
  result += [item for item in w]
  result += [item for item in v]
  result += [item for item in u]
  result += [item for item in t]
  result += [item for item in s]
  return result

batch_amount = 420
groups = 4
group_amount = batch_amount * groups
file = open("mylsp", 'r')
lines = file.read()
words = lines.splitlines()
z = 0
n = 0
while n < group_amount:
  final = ''
  for i in range(batch_amount):
    final += words[n + i] + '\n'
  animal_group = open("sets" + str(z), 'w')
  animal_group.write(final)
  animal_group.close()
  n += batch_amount
  z += 1
setnums = [
[["0","1","2","3"],["4","5","6","7"],["8","9","10","11"]],
[["12","15","18","21"],["24","27","30","33"],["36","39","42","45"]],
[["13","16","19","22"],["25","28","31","34"],["37","40","43","46"]],
[["14","17","20","23"],["26","29","32","35"],["38","41","44","47"]]
]
t = 0
while t < 4:
  numnums = ["0","1","2","3"]
  numnums.remove(str(t))
  n = 0
  myset = setnums[t]
  while n < 3:
    q = numnums[n]
    with open('sets'+str(q)) as f:
      lines = f.read().splitlines()
      a=[]
      z=0
      while z < 4:
        a.append(lines[int(myset[n][z])])
        z += 1
      animal_group = open("mini" + str(t) + str(n), 'w')
      animal_group.write('\n'.join(a)+"\n")
      animal_group.close()
    n+=1
  beep = "mkdir set" + str(t)
  cmd = os.popen(beep)
  time.sleep(.1)
  beep = "cat sets" + str(t) + " mini" + str(t) + "*" + " > set" + str(t) + "/lot"
  cmd = os.popen(beep)
  beep = "cd set" + str(t) + "&& split -l 216 lot && rm lot"
  cmd = os.popen(beep) 
  time.sleep(.1)
  peters = [
  [98,150,88,46,3,185,133,45,75,130,186,49,12,21,207,19,201,18,142,195,60,214,30,77,13,24,10,168,78,179,79,53,63,189,156,167,140,203,37,39,89,76,174,110,84,4,81,93,213,132,90,208,143,128,124,154,113,107,32,96,50,197,196,172,161,34,5,138,42,159,211,148,119,173,71,169,94,158,112,56,122,31,64,72,82,33,210,182,115,2,162,170,68,111,180,131,59,183,97,85,116,108,125,70,36,198,152,43,92,205,41,74,139,27,202,29,164,35,155,87,23,58,20,176,123,199,80,127,192,144,99,212,126,91,52,103,61,141,175,166,48,106,105,66,114,145,136,102,194,104,38,16,101,118,22,160,149,7,14,65,165,120,67,121,26,206,83,47,146,54,215,1,25,73,193,147,187,137,181,135,163,6,216,171,117,109,8,15,69,55,157,28,190,86,188,204,178,11,209,57,151,95,9,62,191,51,100,129,153,184,134,177,17,44,200,40],
  [35,74,1,111,124,101,13,172,78,30,56,142,203,75,105,17,137,182,100,204,216,207,112,93,61,206,196,79,33,115,171,7,108,125,162,141,143,99,161,201,54,43,215,211,116,129,87,81,174,80,199,45,29,167,198,164,31,90,4,6,173,96,120,11,53,210,135,158,71,127,23,58,106,212,145,109,131,95,139,14,195,163,132,57,146,208,113,97,46,20,117,94,155,48,160,59,24,77,18,200,107,110,165,183,19,25,5,119,69,189,179,66,28,156,9,134,22,185,63,91,8,36,202,152,194,12,102,128,166,83,15,180,150,181,149,42,140,197,187,92,114,47,3,84,209,154,37,68,89,10,144,130,157,176,34,103,148,205,50,168,186,213,2,122,70,175,138,49,123,151,193,169,27,133,52,82,73,44,188,86,16,85,41,65,51,214,98,32,55,76,126,38,178,64,118,26,21,104,39,72,147,136,184,153,191,60,190,177,40,121,88,192,62,67,159,170],
  [211,203,123,41,28,171,157,181,67,214,90,4,46,13,156,101,175,160,108,200,92,15,152,44,33,76,117,213,163,122,105,129,120,74,134,77,36,82,26,31,64,79,174,189,186,45,94,127,48,97,18,11,138,25,80,125,10,202,118,210,69,199,17,161,119,21,126,8,128,5,32,109,49,114,135,56,136,1,209,208,190,158,83,2,58,206,93,168,62,100,155,66,7,139,147,205,78,40,16,84,65,111,73,197,133,187,182,89,141,145,59,130,149,140,87,113,107,61,162,53,185,196,215,154,85,121,180,116,195,132,104,27,99,95,51,143,20,150,103,112,178,42,57,193,60,142,148,34,153,176,207,86,23,198,35,14,30,39,47,201,166,179,184,88,24,37,81,70,96,106,91,216,188,151,72,170,204,63,172,167,71,3,177,146,50,22,115,144,43,55,68,173,124,38,9,194,131,6,110,169,75,54,19,183,12,165,137,212,52,164,102,159,29,191,192,98],
  [158,141,211,22,156,40,37,2,196,1,33,175,44,134,176,99,109,113,12,115,126,203,197,52,87,178,5,152,7,88,118,23,86,201,155,162,97,207,199,73,66,117,215,68,19,143,108,49,98,151,104,154,184,28,3,183,41,70,121,71,179,75,193,198,147,82,166,114,24,189,76,46,177,204,29,128,90,85,142,102,125,137,214,190,13,144,127,107,53,38,159,208,185,51,21,122,132,48,25,139,20,164,26,15,69,96,14,105,16,79,32,209,18,174,83,111,202,54,212,191,43,67,65,92,6,100,27,170,163,216,153,138,45,95,74,182,172,150,131,106,101,188,160,62,47,78,50,103,63,148,11,112,60,157,120,165,136,149,57,116,80,210,42,124,59,35,4,194,195,130,8,110,168,181,129,89,171,17,61,205,72,10,180,133,213,94,135,187,206,56,31,58,140,81,167,36,34,200,119,39,145,91,173,55,123,84,161,64,30,169,192,9,146,186,77,93]
  ]
  f1 = open('set'+str(t)+"/xaa")
  line1 = f1.read().splitlines()
  f1.close()
  f2 = open('set'+str(t)+"/xab")
  line2 = f2.read().splitlines()
  f2.close()
  def func(lst, ptr):
    return [lst[idx-1] for idx in ptr]
  lsta = line1
  lstb = line1
  lstc = line2
  lstd = line2
  ptr1 = peters[0]
  ptr2 = peters[1]
  ptr3 = peters[2]
  ptr4 = peters[3]
  a1 = []
  b2 = []
  c3 = []
  d4 = []

  for _ in range(400):
    lsta = func(lsta, ptr1)
    lstb = func(lstb, ptr2)
    lstc = func(lstc, ptr3)
    lstd = func(lstd, ptr4)
    a1.append(lsta)
    b2.append(lstb)
    c3.append(lstc)
    d4.append(lstd)
  agp1 = open('set'+str(t)+"/1", 'w')
  agp1.write(str(a1).replace("], [","]\n[").replace("[[","[").replace("]]","]\n"))
  agp1.close()
  agp2 = open('set'+str(t)+"/2", 'w')
  agp2.write(str(b2).replace("], [","]\n[").replace("[[","[").replace("]]","]\n"))
  agp2.close()
  agp3 = open('set'+str(t)+"/3", 'w')
  agp3.write(str(c3).replace("], [","]\n[").replace("[[","[").replace("]]","]\n"))
  agp3.close()
  agp4 = open('set'+str(t)+"/4", 'w')
  agp4.write(str(d4).replace("], [","]\n[").replace("[[","[").replace("]]","]\n"))
  agp4.close()

  ap = open('set'+str(t)+"/1")
  a = ap.read().splitlines()
  ap.close()
  bp = open('set'+str(t)+"/2")
  b = bp.read().splitlines()
  bp.close()
  cp = open('set'+str(t)+"/3")
  c = cp.read().splitlines()
  cp.close()
  dp = open('set'+str(t)+"/4")
  d = dp.read().splitlines()
  dp.close()

  me_numsets = [
  [[a,b,d,c],[a,d,b,c],[a,b,c,d],[b,c,a,d],[a,c,b,d],[c,a,b,d],[b,a,d,c],[b,d,a,c],[a,d,c,b],[a,c,d,b],[b,a,c,d],[c,b,a,d],[a,d,b,c],[b,c,a,d],[c,a,b,d],[b,d,a,c],[a,c,d,b],[c,b,a,d]],
  [[b,c,a,d],[a,d,b,c],[a,d,c,b],[b,a,c,d],[c,b,a,d],[a,b,d,c],[a,c,b,d],[c,a,b,d],[a,c,d,b],[a,b,c,d],[b,d,a,c],[b,a,d,c],[b,c,a,d],[a,d,c,b],[c,b,a,d],[a,c,b,d],[a,c,d,b],[b,d,a,c]],
  [[b,a,d,c],[b,c,a,d],[a,c,d,b],[c,b,a,d],[c,a,b,d],[b,d,a,c],[a,d,b,c],[a,b,d,c],[b,a,c,d],[a,d,c,b],[a,b,c,d],[a,c,b,d],[b,c,a,d],[c,b,a,d],[b,d,a,c],[a,b,d,c],[a,d,c,b],[a,c,b,d]],
  [[c,a,b,d],[a,b,c,d],[b,d,a,c],[a,c,b,d],[a,b,d,c],[a,d,c,b],[b,a,d,c],[b,a,c,d],[c,b,a,d],[b,c,a,d],[a,d,b,c],[a,c,d,b],[c,a,b,d],[b,d,a,c],[a,b,d,c],[b,a,d,c],[c,b,a,d],[a,d,b,c]]
  ]

  sets=me_numsets[t]
  q = 0
  while q < 16:
    a = sets[q][0]
    b = sets[q][1]
    c = sets[q][2]
    d = sets[q][3]
    e = a[::-1]
    f = b[::-1]
    g = c[::-1]
    h = d[::-1]

    a1 = a[0:200]
    a3 = a[200:400]
    b1 = b[0:200]
    b3 = b[200:400]
    c1 = c[0:200]
    c3 = c[200:400]
    d1 = d[0:200]
    d3 = d[200:400]
    a2 = a1[::-1]
    a4 = a3[::-1]
    b2 = b1[::-1]
    b4 = b3[::-1]
    c2 = c1[::-1]
    c4 = c3[::-1]
    d2 = d1[::-1]
    d4 = d3[::-1]

    if q == 0:
      ag = open('set'+str(t)+"/a"+str(t), 'w')
      ag.write( str(mixfour(a,b,c,d)).replace('["',"").replace('"]',"").replace('", "',"\n"))
      ag.close()
    elif q == 1:
      ag = open('set'+str(t)+"/b"+str(t), 'w')
      ag.write(str(mixfour(e,f,g,h)).replace('["',"").replace('"]',"").replace('", "',"\n"))
      ag.close()
    elif q == 2:
      ag = open('set'+str(t)+"/c"+str(t), 'w')
      ag.write(str(mixfour(a,f,c,h)).replace('["',"").replace('"]',"").replace('", "',"\n"))
      ag.close()
    elif q == 4:
      ag = open('set'+str(t)+"/d"+str(t), 'w')
      ag.write(str(mixfour(e,b,g,d)).replace('["',"").replace('"]',"").replace('", "',"\n"))
      ag.close()
    elif q == 6:
      ag = open('set'+str(t)+"/f"+str(t), 'w')
      ag.write(str(mixeight(a1,b1,c1,d1,a3,b3,c3,d3)).replace('["',"").replace('"]',"").replace('", "',"\n"))
      ag.close()
    elif q == 5:
      ag = open('set'+str(t)+"/e"+str(t), 'w')
      ag.write(str(mixeight(a1,b1,c1,d1,a4,b4,c4,d4)).replace('["',"").replace('"]',"").replace('", "',"\n"))
      ag.close()
    elif q == 7:
      ag = open('set'+str(t)+"/g"+str(t), 'w')
      ag.write(str(mixeight(a3,b3,c3,d3,a1,b1,c1,d1)).replace('["',"").replace('"]',"").replace('", "',"\n"))
      ag.close()
    elif q == 8:
      ag = open('set'+str(t)+"/h"+str(t), 'w')
      ag.write(str(mixeight(a4,b4,c4,d4,a1,b1,c1,d1)).replace('["',"").replace('"]',"").replace('", "',"\n"))
      ag.close()
    elif q == 9:
      ag = open('set'+str(t)+"/i"+str(t), 'w')
      ag.write(str(mixeight(a2,b2,c2,d2,a3,b3,c3,d3)).replace('["',"").replace('"]',"").replace('", "',"\n"))
      ag.close()
    elif q == 10:
      ag = open('set'+str(t)+"/j"+str(t), 'w')
      ag.write(str(mixeight(a2,b2,c2,d2,a4,b4,c4,d4)).replace('["',"").replace('"]',"").replace('", "',"\n"))
      ag.close()
    elif q == 11:
      ag = open('set'+str(t)+"/k"+str(t), 'w')
      ag.write(str(mixeight(a3,b3,c3,d3,a2,b2,c2,d2)).replace('["',"").replace('"]',"").replace('", "',"\n"))
      ag.close()
    elif q == 12:
      ag = open('set'+str(t)+"/l"+str(t), 'w')
      ag.write(str(mixeight(a4,b4,c4,d4,a2,b2,c2,d2)).replace('["',"").replace('"]',"").replace('", "',"\n"))
      ag.close()
    elif q == 13:
      ag = open('set'+str(t)+"/m"+str(t), 'w')
      ag.write( str(mixfour(d,c,b,a)).replace('["',"").replace('"]',"").replace('", "',"\n"))
      ag.close()
    elif q == 14:
      ag = open('set'+str(t)+"/n"+str(t), 'w')
      ag.write(str(mixfour(h,g,f,e)).replace('["',"").replace('"]',"").replace('", "',"\n"))
      ag.close()
    elif q == 15:
      ag = open('set'+str(t)+"/o"+str(t), 'w')
      ag.write(str(mixfour(h,c,f,a)).replace('["',"").replace('"]',"").replace('", "',"\n"))
      ag.close()
    else:
      ag = open('set'+str(t)+"/p"+str(t), 'w')
      ag.write(str(mixfour(d,g,b,e)).replace('["',"").replace('"]',"").replace('", "',"\n"))
      ag.close()

    q+=1

  t+=1
message = "rm mini* sets*"
command = os.popen(message)
message = "mkdir mix"
command = os.popen(message)
message = "mv -v set0/* mix/"
command = os.popen(message)
message = "mv -v set1/* mix/"
command = os.popen(message)
message = "mv -v set2/* mix/"
command = os.popen(message)
message = "mv -v set3/* mix/"
command = os.popen(message)
time.sleep(.1)
message = "cp st.py mix"
command = os.popen(message)
time.sleep(.1)
message = "cd mix && rm 1 2 3 4 x* && python3 st.py"
command = os.popen(message)





