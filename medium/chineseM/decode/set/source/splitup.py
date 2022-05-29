import os

with open("Orig") as file:
  s = file.read()
s = s.split('\n')
for i,name in enumerate(s):
  f = open("results"+str(i)+"/Orig","w")
  f.write(name)
  f.close()

with open("r1") as file:
    s = file.read()
s = s.split('#')
for i,name in enumerate(s):
    f = open("results"+str(i)+"/r1.txt","w")
    f.write(name)
    f.close()

with open("r2") as file:
    s = file.read()
s = s.split('\n')
for i,name in enumerate(s):
    f = open("results"+str(i)+"/r2.txt","w")
    f.write(name)
    f.close()

bce = """for d in */; do cp source/*.txt grow.py "$d"; done"""
cmd = os.popen(bce)
print(cmd.read())

bce2 = "./CC"
cmd2 = os.popen(bce2)
print(cmd2.read())
