from itertools import chain
from itertools import cycle
import random
import string
import glob
import time
import os
import sys

def randStr(chars = string.ascii_uppercase + string.digits, N=567):
	return ''.join(random.choice(chars) for _ in range(N))
value = randStr(chars='abcdefghijklmnop')

ts1 = value[:-378]
with open('ts1', 'w') as file:
    file.write(ts1)

ts2 = value[189:-189]
with open('ts2', 'w') as file:
    file.write(ts2)

ts3 = value[378:]
with open('ts3', 'w') as file:
    file.write(ts3)

fnames = sorted(glob.glob('t*'))

beep = "cat " + fnames[0] + " ts1 " + fnames[1] + " ts2 " + fnames[2] + " ts3 " + " > tog.txt"
cmd = os.popen(beep)
print(cmd.read())

def mixed_scrambled():
  with open("tog.txt") as main:
    moon = main.read()
    l = moon.replace("\n","")
    y = len(l)
    n = 4
    t = int(y/n)
    x = sys.argv[1]
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

    n = 4
    l = [l[i:i+n] for i in range(0, len(l), n)]
    k = sorted((b:=sorted(range(len(k)), key=lambda x: k[x])), key=lambda x: b[x])
    k = list(reversed(k))
    st = [x for _,x in sorted(zip(k,l))]
    st = "".join(st)
    with open("tank", 'w') as outfile:
      outfile.write(st)

mixed_scrambled()
######

beep = "fold -w63 tank > tog.txt"
print(beep)
cmd = os.popen(beep)
print(cmd.read())
print(cmd.close())

with open("tog.txt", 'r') as file:
    data = file.read()
    data = data.replace("a","0010").replace("b","0001").replace("c","0011").replace("d","0110").replace("e","1111").replace("f","0111").replace("g","1011").replace("h","1010").replace("i","1000").replace("j","0100").replace("k","1100").replace("l","1001").replace("m","0000").replace("n","1101").replace("o","1110").replace("p","0101") 
with open("Blove", 'w') as file:  
    file.write(data)
with open("Blove") as input_file, open("tog.txt", 'w') as output_file:
  for line in input_file:
    line = line.rstrip() # remove trailing newline
    first_line = ''.join(chain.from_iterable(zip(line[0::4], line[1::4])))
    second_line = ''.join(chain.from_iterable(zip(line[2::4], line[3::4])))
    output_file.write(first_line + '\n')
    output_file.write(second_line + '\n')

######

with open("tog.txt") as main:
  buz = main.read()
bunny = buz.replace("\n","")
res = ' '.join(bunny[i:i + 3] for i in range(0, len(bunny), 3))
core = res.replace("000","1").replace("001","2").replace("010","3").replace("011","4").replace("100","5").replace("101","6").replace("110","7").replace("111","8").replace(" ","")

str1 = ''.join(core)
def remove(str1):
  return str1.replace(" ","")
qq = ''.join(remove(str1))

yy = ' '.join(qq[i:i + 2] for i in range(0, len(qq), 2))
zz = yy.replace("11","").replace("12","").replace("13","").replace("14","").replace("15","").replace("16","").replace("17","").replace("18","").replace("21","").replace("22","").replace("23","").replace("24","").replace("25","").replace("26","").replace("27","").replace("28","").replace("31","").replace("32","").replace("33","").replace("34","").replace("35","").replace("36","").replace("37","").replace("38","").replace("41","").replace("42","").replace("43","").replace("44","").replace("45","").replace("46","").replace("47","").replace("48","").replace("51","").replace("52","").replace("53","").replace("54","").replace("55","").replace("56","").replace("57","").replace("58","").replace("61","").replace("62","").replace("63","").replace("64","").replace("65","").replace("66","").replace("67","").replace("68","").replace("71","").replace("72","").replace("73","⊻").replace("74","■").replace("75","□").replace("76","▪").replace("77","▫").replace("78","▬").replace("81","▲").replace("82","▵").replace("83","▹").replace("84","►").replace("85","▼").replace("86","▿").replace("87","◃").replace("88","◄")
xl = zz.replace(" ","L")
xi = "L" + xl

import wrl
replacementL = wrl.rwl

one = ' '.join(xi[i:i + 1] for i in range(0, len(xi), 1))
words = one.split()
replace_idx = 0

for i, y in enumerate(words):
    if y in replacementL:
        words[i] = replacementL[y][replace_idx]
        replace_idx  = (replace_idx  + 1)%64
str1 = ''.join(words)
str2 = "".join(str1)

with open("tank.txt", 'w') as outfile:
    outfile.write(str2)

with open("du.py") as cr:
    st = cr.read()

st1 = st.replace("!"," ").replace("?","\n")

en1 = open("du.py", "w")
en1.write(st1)
en1.close()

exec(open("du.py").read())

import wr
replacementW = wr.rw

with open("tank.txt") as main:
    words = main.read().split()

replaced = []
for y in words:
    replacement = replacementW.get(y, y) if random.random() > 0.5 else y
    replaced.append(replacement)
text = ' '.join(replaced)

x = text.replace(" ","")

def litering_by_three(a):
    return '\n'.join([a[i:i + 2268] for i in range(0, len(a), 2268)])

with open("togged", 'w') as outfile:
    outfile.write(litering_by_three(x))

######

beep = "split -l1 togged"
print(beep)
cmd = os.popen(beep)
print(cmd.read())
print(cmd.close())



num_range = ['111','112','113','114','115','116','117','118','121','122','123','124','125','126','127','128','131','132','133','134','135','136','137','138','141','142','143','144','145','146','147','148','151','152','153','154','155','156','157','158','161','162','163','164','165','166','167','168','171','172','173','174','175','176','177','178','181','182','183','184','185','186','187','188','211','212','213','214','215','216','217','218','221','222','223','224','225','226','227','228','231','232','233','234','235','236','237','238','241','242','243','244','245','246','247','248','251','252','253','254','255','256','257','258','261','262','263','264','265','266','267','268','271','272','273','274','275','276','277','278','281','282','283','284','285','286','287','288','311','312','313','314','315','316','317','318','321','322','323','324','325','326','327','328','331','332','333','334','335','336','337','338','341','342','343','344','345','346','347','348','351','352','353','354','355','356','357','358','361','362','363','364','365','366','367','368','371','372','373','374','375','376','377','378','381','382','383','384','385','386','387','388','411','412','413','414','415','416','417','418','421','422','423','424','425','426','427','428','431','432','433','434','435','436','437','438','441','442','443','444','445','446','447','448','451','452','453','454','455','456','457','458','461','462','463','464','465','466','467','468','471','472','473','474','475','476','477','478','481','482','483','484','485','486','487','488','511','512','513','514','515','516','517','518','521','522','523','524','525','526','527','528','531','532','533','534','535','536','537','538','541','542','543','544','545','546','547','548','551','552','553','554','555','556','557','558','561','562','563','564','565','566','567','568','571','572','573','574','575','576','577','578','581','582','583','584','585','586','587','588','611','612','613','614','615','616','617','618','621','622','623','624','625','626','627','628','631','632','633','634','635','636','637','638','641','642','643','644','645','646','647','648','651','652','653','654','655','656','657','658','661','662','663','664','665','666','667','668','671','672','673','674','675','676','677','678','681','682','683','684','685','686','687','688','711','712','713','714','715','716','717','718','721','722','723','724','725','726','727','728','731','732','733','734','735','736','737','738','741','742','743','744','745','746','747','748','751','752','753','754','755','756','757','758','761','762','763','764','765','766','767','768','771','772','773','774','775','776','777','778','781','782','783','784','785','786','787','788','811','812','813','814','815','816','817','818','821','822','823','824','825','826','827','828','831','832','833','834','835','836','837','838','841','842','843','844','845','846','847','848','851','852','853','854','855','856','857','858','861','862','863','864','865','866','867','868','871','872','873','874','875','876','877','878','881','882','883','884','885','886','887','888']

sums = [
[0,0,1,1,1,1,1,1,0,1,0,0,0,1,1,1,1,1,0,1,1,1,1,0,0,0,0,0,1,1,0,0,1,1,0,1,0,0,0,1,0,0,1,0,1,1,1,0,1,1,0,0,0,1,0,1,0,0,1,0,1,1,0,0,0,1,1,0,1,1,1,0,0,0,0,0,0,1,1,0,1,0,0,0,0,0,0,0,0,1,0,0,1,1,0,0,0,0,1,0,0,0,1,0,0,1,0,0,0,0,1,1,0,0,1,1,1,1,0,0,1,0,1,1,1,0,1,1,1,0,1,1,1,0,0,0,0,0,0,1,0,1,0,0,1,0,1,1,0,0,1,1,0,1,1,0,0,1,1,1,1,1,1,1,1,1,1,0,0,1,0,1,1,1,1,0,0,0,0,1,0,1,0,1,1,1,1,0,1,1,1,1,1,1,0,0,1,0,1,0,0,0,0,1,1,1,1,1,0,0,1,1,1,1,1,1,0,1,1,1,0,1,0,1,1,0,1,0,1,1,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,1,0,1,1,1,1,0,0,0,0,1,1,0,0,1,0,0,0,0,1,1,0,1,1,1,1,0,0,0,1,1,0,0,1,0,1,1,0,1,1,1,1,0,1,0,0,0,1,0,1,1,1,0,1,0,0,1,0,0,1,0,0,0,0,0,0,1,1,0,1,1,1,1,1,1,0,0,0,0,1,0,0,1,1,0,0,0,1,1,1,1,0,0,0,1,1,0,0,1,1,1,1,1,1,0,1,0,0,0,0,1,0,1,0,1,1,1,1,1,1,0,0,0,0,1,1,0,0,0,1,0,1,1,0,1,0,1,1,1,1,0,1,1,1,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,1,0,1,0,0,1,1,1,1,0,0,1,0,0,1,0,1,1,1,0,0,0,0,1,0,0,0,0,1,0,1,0,1,1,1,0,1,1,0,0,1,0,0,1,1,0,1,0,0,1,1,0,0,0,1,1,0,1,0,0,0,0,0,0,1,1,0,0,1,1,1,0,1,0,0,0,1,0,1,0,1,0,1,0,0,1,0,1,1,0,0,1,0,0,1,1,1,1,1,1,0,0,0,1,0,1,1,0,0,1,0,0,1,1,1,1,0,1,0,1,0,0,1,0,0,0,0,1,1,1,1,0,0,1,0,1,0,1,0,0,1,1,0,1,1,0,1,1,1,1,0,0,1,1,0,0,0,0,1,1,0,1,0,1,0,1,1,1,1,0,0,1,0,0,0,0,1,0,0,0,1,0,0,1,1,1,1,1,1,1,0,0,0,1,1,1,0,0,0,1,1,1,0,1,0,1,1,1,1,0,0,0,1,0,1,1,1,1,0,0,1,0,0,0,0,1,1,1,1,1,1,1,0,1,1,1,0,0,1,0,0,1,0,0,1,1,1,1,0,0,1,0,1,0,1,0,0,1,0,0,1,0,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,1,1,1,0,1,0,0,0,1,1,0,0,1,0,1,1,1,0,1,0,1,0,0,1,1,1,1,0,0,1,1,0,1,0,1,0,0,1,0,0,1,0,0,0,0,0,0,1,1,0,1,0,1,0,0,1,0,1,1,1,0,0,1,1,1,1],
[0,0,1,0,1,0,1,0,1,1,0,0,1,0,0,0,1,0,1,1,1,0,1,0,1,0,1,0,1,0,1,1,1,0,0,0,1,0,1,0,0,1,0,1,1,0,1,0,1,0,1,1,0,1,0,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,1,1,0,0,0,1,1,1,0,1,0,0,1,1,1,0,0,1,0,0,0,0,1,0,1,0,0,0,0,1,1,0,0,1,0,0,1,0,1,0,0,0,0,0,0,0,1,1,1,1,0,0,1,0,1,0,0,1,1,0,0,0,1,0,0,1,0,1,0,0,1,1,0,1,1,0,1,0,1,0,0,1,1,1,1,0,0,0,1,0,1,1,1,1,0,0,1,1,1,1,0,0,0,0,0,1,1,1,1,1,0,0,1,1,0,1,0,0,0,1,0,1,1,0,0,1,1,0,1,0,0,1,0,0,1,0,1,0,1,1,1,0,1,1,0,0,0,1,0,0,0,1,1,1,0,1,0,1,1,1,1,0,1,0,1,0,1,1,0,0,1,1,0,0,0,1,1,1,0,0,0,1,0,1,1,1,0,1,0,1,0,0,1,0,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,1,1,1,1,0,1,1,0,0,1,0,1,1,0,1,0,0,0,1,0,0,0,0,1,0,1,0,1,0,1,1,1,1,0,0,1,0,1,1,1,0,0,0,0,1,0,0,1,1,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,0,1,0,0,1,0,1,1,1,0,1,1,0,1,1,0,0,1,1,0,0,0,1,1,1,0,1,1,0,0,1,1,1,0,0,0,1,1,1,0,0,0,0,1,0,1,0,1,0,1,0,0,0,1,1,0,1,0,1,1,1,1,0,0,0,0,0,1,1,1,1,0,0,1,1,1,1,1,1,1,0,1,1,0,0,1,0,0,0,0,0,0,1,0,1,0,0,0,0,1,1,0,0,1,0,1,0,1,0,1,0,0,1,0,0,1,0,0,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,0,0,1,1,1,0,1,1,1,0,0,0,1,0,1,0,0,0,0,0,0,1,1,1,0,1,1,0,1,0,0,1,1,1,1,1,0,0,1,1,1,1,1,1,1,0,1,0,1,0,0,0,1,0,0,0,0,1,1,1,0,1,1,0,0,0,0,1,1,1,0,1,0,1,1,1,0,0,0,0,0,1,0,0,1,1,1,0,1,0,1,1,1,1,1,1,1,0,1,1,0,0,1,0,1,1,0,0,0,0,1,1,1,0,1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,1,1,0,1,1,0,1,0,0,1,1,1,1,1,1,0,1,0,1,1,1,0,1,1,0,1,1,1,0,0,0,1,0,0,1,1,1,0,1,0,0,1,1,1,1,1,1,0,1,1,1,1,1,0,1,0,0,1,0,0,1,1,1,1,0,1,1,0,0,1,1,0,0,0,0,1,0,1,1,0,0,1,1,1,0,1,1,0,0,0,0,0,0,0,1,1,0,1,1,0,1,0,1,1,1,0,1,0,1,1,0,0,1,0,1,0,1,1,0,1,0,1,1,0,1,1,1,0,1,0,1,0,0,0,0,1,1,1,1,0],
[1,0,1,0,1,1,1,1,0,0,0,1,1,1,1,1,0,1,0,0,0,0,1,0,0,1,1,0,1,0,0,0,0,1,0,0,0,1,1,1,1,1,1,0,0,1,0,0,1,1,1,1,0,0,0,1,0,0,0,1,1,0,0,1,0,1,0,0,1,1,1,0,1,0,0,0,1,0,1,1,1,1,1,0,1,1,0,1,1,0,0,1,0,0,1,1,0,0,0,1,1,0,0,0,1,1,1,0,1,0,1,1,1,0,0,0,0,1,0,1,0,0,1,1,1,1,0,1,0,0,1,0,1,1,1,1,0,0,1,0,1,1,0,1,1,1,1,1,1,0,1,0,1,1,1,0,0,0,0,1,1,0,0,1,0,1,0,1,1,0,1,0,1,0,0,0,1,1,1,0,0,1,1,1,1,0,0,1,1,1,1,0,1,1,0,0,0,0,0,0,1,1,0,1,1,0,0,1,0,1,1,0,0,1,1,1,1,1,1,0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,0,0,1,1,1,1,1,0,0,1,0,0,0,1,1,1,1,1,0,1,0,1,1,0,0,0,1,1,0,0,1,0,0,1,0,1,0,0,0,1,1,0,1,1,1,1,1,1,0,1,1,0,1,0,0,0,0,0,0,0,1,0,1,0,0,1,1,0,1,0,0,1,1,0,1,0,1,0,1,0,0,0,1,1,0,1,1,0,1,1,1,0,0,1,0,1,0,0,1,0,0,0,1,1,1,0,0,0,0,1,1,0,0,1,1,0,0,0,0,1,0,0,0,1,1,1,0,0,1,1,0,1,1,1,0,0,0,0,1,0,1,0,0,0,1,1,0,0,1,0,1,0,0,1,0,0,1,0,1,0,1,0,1,0,0,1,0,0,1,0,1,0,0,0,1,0,1,0,0,0,1,1,0,1,0,0,0,0,1,1,1,1,1,1,0,1,1,0,0,1,1,1,0,0,0,1,0,0,0,1,0,0,1,0,0,0,0,0,1,0,1,1,1,1,0,1,0,1,0,0,1,1,1,1,1,1,0,1,1,1,0,0,0,0,0,0,1,0,1,1,0,0,1,0,0,0,0,1,1,1,1,0,0,0,1,0,1,0,0,0,1,0,1,0,1,0,0,1,0,1,0,0,1,0,1,1,0,1,0,1,0,0,0,1,0,1,1,1,0,1,1,0,1,1,1,0,1,1,1,1,0,1,0,1,0,0,0,0,1,0,1,1,0,0,1,0,0,0,0,1,1,0,0,1,0,0,1,0,1,1,1,0,0,0,0,0,0,1,0,1,1,1,0,1,0,1,0,0,0,1,1,1,1,1,0,0,1,0,1,0,1,0,1,1,0,1,0,1,1,1,0,1,1,0,1,0,1,1,1,1,0,1,1,1,1,1,0,0,1,0,1,0,0,1,1,0,0,1,0,0,1,0,0,0,1,0,1,1,0,0,1,1,0,0,1,1,1,0,1,1,0,0,1,0,0,1,0,0,1,0,1,1,0,1,1,1,0,0,1,0,0,0,1,0,0,1,0,0,0,0,0,0,1,0,0,0,1,1,1,1,1,0,0,0,1,1,0,1,1,1,0,0,1,0,1,1,1,1,1,0,0,1,0,0,0,0,1,1,1,1,1,1,0,1,1,0,1,1,1,0,1,0,0,0,1,1,0,0,0,0,1,1]
]

cycle_sum = cycle(sums)

sum = [0,0,0,1,1,0,0,0,1,1,1,1,1,1,1,0,1,1,0,0,0,1,0,0,1,1,1,1,0,0,1,0,0,1,0,0,0,1,0,1,0,1,1,0,1,1,1,0,0,1,0,0,0,1,1,0,0,1,0,1,1,0,1,1,1,0,1,0,0,0,1,1,1,1,1,0,0,1,1,0,0,1,1,1,1,1,1,1,1,0,1,1,1,0,1,0,0,1,0,0,0,1,0,1,1,1,1,1,1,0,0,0,0,0,0,1,0,1,1,0,0,1,0,0,0,0,1,0,1,1,0,1,1,1,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1,1,1,0,1,0,1,1,1,0,1,0,1,0,0,1,1,0,1,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,1,0,1,1,1,0,0,0,0,1,0,1,1,1,1,1,1,0,0,0,1,0,1,0,1,0,1,0,1,0,0,0,1,1,1,0,0,1,0,0,0,0,0,0,1,0,0,1,0,1,1,0,1,0,1,0,0,0,0,0,1,1,0,1,0,1,0,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,1,0,1,0,1,1,0,0,1,1,0,0,1,1,0,0,0,1,0,1,1,1,0,0,0,1,1,0,1,1,0,1,1,0,1,0,0,0,0,0,1,1,1,0,0,1,1,0,1,1,1,1,1,1,0,0,1,1,0,1,0,0,0,1,0,1,1,0,0,0,1,0,0,1,1,0,1,1,0,1,0,1,1,0,0,0,0,0,0,1,0,0,1,0,1,0,1,0,0,0,1,1,1,0,0,1,1,0,0,1,1,0,0,1,0,1,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,1,1,1,0,0,0,1,1,1,1,0,1,1,0,1,1,1,1,0,0,1,1,0,1,0,1,1,0,0,0,1,1,0,1,1,1,0,0,1,0,0,0,0,0,0,1,1,0,0,1,1,1,1,1,0,0,0,0,0,1,1,1,0,0,1,1,0,1,1,0,1,1,1,0,0,1,1,1,1,1,0,1,1,0,0,0,0,1,0,0,0,0,0,0,1,1,1,1,1,1,0,1,1,1,0,1,1,0,1,0,1,1,0,0,0,1,0,0,0,1,1,1,0,1,1,1,1,0,0,0,0,1,1,1,1,1,0,1,1,1,0,0,1,0,0,1,1,0,1,0,0,1,0,1,0,0,1,1,1,1,0,1,0,1,1,1,1,0,1,0,1,1,0,1,1,1,0,0,0,1,0,1,0,0,1,1,0,0,1,0,1,0,1,1,1,1,1,0,1,0,1,0,1,1,0,1,0,0,1,0,1,0,1,1,1,0,1,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,1,0,0,1,1,1,1,0,0,0,0,1,0,1,1,0,1,1,1,0,0,1,1,0,0,1,0,1,1,1,1,1,0,0,1,1,0,0,0,1,1,0,0,0,0,0,0,1,0,0,1,1,1,1,0,1,1,0,1,1,1,1,1,0,0,1,0,1,1,1,0,0,1,0,0,1,1,0,0,0,0,1,1,0,0,0,1,1,1,1,0,0,1,0,1,0,1,1,1]

for name in glob.glob('x*'):
  with open(name) as main:
    x = main.read()
    x = x.strip()

  def litering_by_three(a):
    return ','.join([a[i:i + 3] for i in range(0, len(a), 3)])

  b = litering_by_three(x).replace(",00",",").replace(",0",",")
  test_list = b.split(',')
  for i in range(0, len(test_list)):
    test_list[i] = int(test_list[i])

  check = test_list
  current_sum = sum
  leck = len(check)
  p = 0
  x = 0
  lst=[]

  while p < leck:
    ct = check[p]
    s = sum[p]
    if s == 1:
      z = (num_range[(num_range.index(str(ct))+256)%512])
    else:
      z = (ct)
    lst.append(z)
    p += 1

  listToStr = ' '.join([str(elem) for elem in lst])
  with open("p"+name+".txt", 'w') as output:
    output.write(listToStr)

  sum = next(cycle_sum)

beep = "rm -r -v B* C* t* x* *.py __pycache__"
print(beep)
cmd = os.popen(beep)
print(cmd.read())
print(cmd.close())
