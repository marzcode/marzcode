import itertools
import shutil
import glob
import re
import os

def grouper(S, n):
  iterator = iter(S)
  while True:
    items = list(itertools.islice(iterator, n))
    if len(items) == 0:
      break
    yield items

fnames = sorted(glob.glob('x*'))
for i, fnames in enumerate(grouper(fnames, 4)):
  dirname = 'results%d' % i
  os.mkdir(dirname)
  for fname in fnames:
    shutil.move(fname, dirname)

beep = "ls -d r* > waste/folders"
cmnd = os.popen(beep)
print(cmnd.read())

with open('waste/folders') as f:
  nm = len(f.readlines())

with open("source/Za") as cr4:
    mn4 = cr4.read()
n4 = nm*mn4
r4 = n4.strip()
f4 = open("waste/cd", "w")
f4.write(r4)
f4.close()

with open("source/Zb") as cr5:
    mn5 = cr5.read()
n5 = nm*mn5
r5 = n5.strip()
f5 = open("waste/string", "w")
f5.write(r5)
f5.close()

with open("source/Zc") as cr6:
    mn6 = cr6.read()
n6 = nm*mn6
r6 = n6.strip()
f6 = open("waste/bk", "w")
f6.write(r6)
f6.close()

with open("source/Ze") as cr4:
    mn4 = cr4.read()
n4 = nm*mn4
r4 = n4.strip()
f4 = open("waste/Ze", "w")
f4.write(r4)
f4.close()

with open("source/Zf") as cr5:
    mn5 = cr5.read()
n5 = nm*mn5
r5 = n5.strip()
f5 = open("waste/Zf", "w")
f5.write(r5)
f5.close()

beep = "paste waste/Ze waste/folders > waste/cmd1"
cmnd = os.popen(beep)
print(cmnd.read())

with open("waste/cmd1") as core:
    fix = core.read()
r1 = fix.replace("	"," ")
f1 = open("waste/cmd1", "w")
f1.write(r1)
f1.close()

beep = "paste waste/cd waste/folders > waste/cmpt1"
cmnd = os.popen(beep)
print(cmnd.read())

with open("waste/cmpt1") as core:
    fix = core.read()
r1 = fix.replace("	"," ")
f1 = open("waste/cmpt1", "w")
f1.write(r1)
f1.close()

beep = "paste waste/cmpt1 waste/Zf waste/bk > waste/cmd2"
cmnd = os.popen(beep)
print(cmnd.read())

with open("waste/cmd2") as core:
    fix = core.read()
r1 = fix.replace("	","\n")
f1 = open("waste/cmd2", "w")
f1.write(r1)
f1.close()

beep = "cat waste/cmd1 waste/cmd2 > CC && chmod +x CC && ./CC && rm CC"
cmnd = os.popen(beep)
print(cmnd.read())

with open('source/codes') as f:
  for line in f:
    listedline = line.strip().split('=')

listedline[3] = listedline[3].split(" ")
z = 0
with open(r"waste/folders", 'r') as fp:
  z = len(fp.readlines())

def func(lst, ptr):
  return [lst[idx-1] for idx in ptr]
lst = ['111','112','113','114','115','116','117','118','121','122','123','124','125','126','127','128','131','132','133','134','135','136','137','138','141','142','143','144','145','146','147','148','151','152','153','154','155','156','157','158','161','162','163','164','165','166','167','168','171','172','173','174','175','176','177','178','181','182','183','184','185','186','187','188','211','212','213','214','215','216','217','218','221','222','223','224','225','226','227','228','231','232','233','234','235','236','237','238','241','242','243','244','245','246','247','248','251','252','253','254','255','256','257','258','261','262','263','264','265','266','267','268','271','272','273','274','275','276','277','278','281','282','283','284','285','286','287','288','311','312','313','314','315','316','317','318','321','322','323','324','325','326','327','328','331','332','333','334','335','336','337','338','341','342','343','344','345','346','347','348','351','352','353','354','355','356','357','358','361','362','363','364','365','366','367','368','371','372','373','374','375','376','377','378','381','382','383','384','385','386','387','388','411','412','413','414','415','416','417','418','421','422','423','424','425','426','427','428','431','432','433','434','435','436','437','438','441','442','443','444','445','446','447','448','451','452','453','454','455','456','457','458','461','462','463','464','465','466','467','468','471','472','473','474','475','476','477','478','481','482','483','484','485','486','487','488','511','512','513','514','515','516','517','518','521','522','523','524','525','526','527','528','531','532','533','534','535','536','537','538','541','542','543','544','545','546','547','548','551','552','553','554','555','556','557','558','561','562','563','564','565','566','567','568','571','572','573','574','575','576','577','578','581','582','583','584','585','586','587','588','611','612','613','614','615','616','617','618','621','622','623','624','625','626','627','628','631','632','633','634','635','636','637','638','641','642','643','644','645','646','647','648','651','652','653','654','655','656','657','658','661','662','663','664','665','666','667','668','671','672','673','674','675','676','677','678','681','682','683','684','685','686','687','688','711','712','713','714','715','716','717','718','721','722','723','724','725','726','727','728','731','732','733','734','735','736','737','738','741','742','743','744','745','746','747','748','751','752','753','754','755','756','757','758','761','762','763','764','765','766','767','768','771','772','773','774','775','776','777','778','781','782','783','784','785','786','787','788','811','812','813','814','815','816','817','818','821','822','823','824','825','826','827','828','831','832','833','834','835','836','837','838','841','842','843','844','845','846','847','848','851','852','853','854','855','856','857','858','861','862','863','864','865','866','867','868','871','872','873','874','875','876','877','878','881','882','883','884','885','886','887','888']
ptr = [int(ele) for ele in listedline[2].split()]
q = listedline[3]
s = list(map(int, q))
n = list(reversed(s))
t = itertools.cycle(s)
d = itertools.cycle(n)

df=open('source/core','w')
for _ in range(z):
  ch = next(d)
  lst = (func(lst, ptr))
  if ch == 0:
    lst2 = lst[next(t):]
  else:
    lst2 = lst[next(t):-ch]
  df.write(str(lst2).replace(' ',''))
df.close()

with open("source/core") as core:
    fix = core.read()
fix = fix.replace('][',']\n[')
filit = open("source/core", "w")
filit.write(fix)
filit.close()

with open('source/codes') as f:
    for line in f:
        listedline = line.strip().split('=')
z = 0

with open(r"waste/folders", 'r') as fp:
  z = len(fp.readlines())

def func(lst, ptr):
  return [lst[idx-1] for idx in ptr]

lst = list(listedline[1])
ptr = [int(ele) for ele in listedline[0].split()]   

df=open('waste/pwds','w')
for _ in range(z):
  lst = func(lst, ptr)
  df.write(str(lst).replace("['","").replace("', '","").replace("']",""))
  df.write('\n')
df.close()

beep = "paste waste/string waste/pwds > waste/set"
cmnd = os.popen(beep)
print(cmnd.read())

with open("waste/set") as core:
    fix = core.read()
r1 = fix.replace("	"," ")
f1 = open("waste/set", "w")
f1.write(r1)
f1.close()

beep = "paste waste/cd waste/folders > waste/cg"
cmnd = os.popen(beep)
print(cmnd.read())

with open("waste/cg") as core:
    fix = core.read()
r1 = fix.replace("	"," ")
f1 = open("waste/cg", "w")
f1.write(r1)
f1.close()

beep = "paste waste/cg waste/set waste/bk > waste/CC"
cmnd = os.popen(beep)
print(cmnd.read())

with open("waste/CC") as core:
    fix = core.read()
r1 = fix.replace("	","\n")
f1 = open("waste/CC", "w")
f1.write(r1)
f1.close()

beep = "cat waste/CC source/up >> source/CC"
cmnd = os.popen(beep)
print(cmnd.read())

beep = "cd source && python3 onesc.py"
cmnd = os.popen(beep)
print(cmnd.read())

