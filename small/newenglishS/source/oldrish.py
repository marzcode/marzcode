import re, ast
import glob
import os

# Form into block shapes
for path in glob.glob("pic*"):
    with open(path) as f:
        lines = f.read()
    my_lis = lines.split()
    iter_len = len(my_lis)
    lst=[]
    for e in range(iter_len):
        p = my_lis[e].zfill(3)
        lst.append(p)
    string1=""
    for i in lst:
       string1=string1+i
    x = string1
    def litering_by_three(a):
        return '\n'.join([a[i:i + 756] for i in range(0, len(a), 756)])
    with open(path, 'w') as outfile:
        outfile.write(litering_by_three(x) + "\n")

# Form into columns
dir_list = os.listdir('./')
dir_list.remove("rish.py")
dir_list = sorted(dir_list)
my_string = " "
dir_list = [s + my_string for s in dir_list]
l = len(dir_list)
c = l / 4
t1 = 0
t2 = 1
t3 = 2
t4 = 3

while c > 0:
  d1 = dir_list[t1]
  d2 = dir_list[t2]
  d3 = dir_list[t3]
  d4 = dir_list[t4]
  col = str(int(c)) 
  message = "cat " + d1 + d2 + d3 + d4 + " > " + col + ".txt"
  command = os.popen(message)
  t1 += 4
  t2 += 4
  t3 += 4
  t4 += 4
  c-= 1


beep = "rename 'unless (/0+[0-9]{5}.txt/) {s/^([0-9]{1,4}\.txt)$/0000$1/g;s/0*([0-9]{5}\..*)/$1/}' *"
cmnd = os.popen(beep)
print(cmnd.read())


# columns of columns shuffeled
path, dirs, files = next(os.walk("./"))
file_count = len(files)
num = file_count - 1
bob = []

def func(lst, ptr):
  return [lst[idx-1] for idx in ptr]
lst = [132,167,14,165,71,74,227,225,58,224,154,73,1,17,139,22,238,81,195,131,191,76,49,34,53,13,64,109,223,108,149,60,218,24,208,199,119,91,243,40,151,239,180,89,111,220,61,51,178,221,200,150,52,229,7,156,136,138,185,248,104,118,59,15,25,31,63,187,4,181,133,249,67,146,214,117,170,226,80,236,106,173,216,207,120,234,65,99,19,115,48,202,86,41,166,233,147,35,190,88,68,93,201,182,39,69,66,137,30,54,169,203,42,144,87,242,183,209,245,121,231,100,174,240,12,110,252,162,160,3,102,179,177,152,50,33,6,153,18,107,103,94,164,197,5,112,237,222,130,212,96,105,84,44,8,215,70,140,92,213,16,114,244,158,9,159,27,55,116,143,128,37,124,145,204,98,247,85,45,2,57,250,43,20,21,95,251,163,211,75,32,228,127,28,36,79,142,11,171,38,122,217,219,206,82,10,56,168,175,193,192,72,241,161,126,176,62,77,184,155,186,188,125,157,47,29,189,194,83,230,246,101,210,148,232,134,23,26,113,135,46,123,196,129,90,235,198,97,141,205,78,172]
ptr = [154,12,179,147,145,96,76,137,45,70,236,171,98,13,196,64,4,237,117,191,55,32,106,63,33,216,163,15,116,29,99,30,182,174,2,81,42,187,146,204,167,199,50,201,149,84,11,28,79,80,173,162,124,192,235,36,16,217,195,82,100,169,93,249,77,240,57,21,22,212,73,164,210,228,247,44,183,209,153,227,6,129,26,85,1,114,128,75,180,208,5,108,125,107,225,132,48,186,92,221,178,139,245,91,110,3,65,200,20,130,104,135,176,229,34,17,35,175,181,158,219,103,90,230,112,115,37,71,151,222,119,150,142,242,126,189,165,56,170,207,231,40,49,111,14,109,53,211,250,134,248,246,113,105,218,123,172,143,87,148,224,161,215,166,138,9,94,155,97,18,7,118,68,60,202,244,78,25,184,23,160,193,214,46,141,168,198,52,239,152,190,59,177,206,43,31,226,223,66,54,188,51,39,102,203,41,74,157,140,19,61,232,58,24,252,83,133,89,213,197,101,251,127,159,241,69,10,238,72,243,121,234,185,122,38,67,156,131,220,88,205,86,27,8,233,144,62,47,194,120,136,95]
for _ in range(num):
  lst = func(lst, ptr)
  bob.append(lst)

cnt = 0

for name in sorted(glob.glob('*.txt')):
  with open(name) as f:
    lines = f.readlines()
  ll = len(lines)
  t = 0
  bk=open('nip','w')
  while (t < ll):
    string = lines[t]
    string = string.strip("\n")
    split_string = [string[i:i+3] for i in range(0, len(string), 3)]
    def func(lst, ptr):
      return [lst[idx-1] for idx in ptr]
    lst = split_string
    ptr = bob[cnt]
    lst = func(lst, ptr)
    nl = lst[2::3]
    del lst[3-1::3]
    bk.write(str(lst).replace("'",""))
    bk.write(str(nl).replace("'",""))
    bk.write("\n")
    t += 1
  bk.close()
  with open('nip') as f:
    lines = f.read()
    sort = lines.replace("][",", ").replace(", "," ")
    sort = sort[:-1]
  with open(name, 'w') as output:
    output.write(sort)
  cnt += 1


# column rows altered by maths
sums = []
ofs = []
def func(lst, ptr):
  return [lst[idx-1] for idx in ptr]

lst1 = [0,1,0,0,0,1,1,1,1,1,1,0,1,0,1,1,1,0,0,0,1,1,0,1,0,0,1,0,0,1,1,0,1,0,1,1,0,0,0,1,1,1,1,0,1,1,1,0,0,1,0,0,0,0,1,1,0,0,1,0,1,0,1,0,1,1,1,1,1,1,0,1,1,0,0,1,1,1,1,0,1,1,1,1,0,1,0,1,0,0,0,0,1,1,0,1,0,0,0,0,0,0,1,0,0,0,1,1,1,0,1,0,0,0,1,1,0,1,1,1,1,1,0,0,0,0,0,0,0,0,1,0,0,1,1,1,0,0,1,1,1,1,0,0,1,1,1,0,1,0,1,1,0,0,0,1,0,0,1,0,1,0,0,0,0,1,0,1,1,0,0,0,1,0,1,0,0,0,1,1,0,0,1,0,1,0,0,1,0,0,0,0,1,1,1,1,0,0,1,1,0,1,1,1,1,0,0,0,0,1,1,0,1,0,0,0,1,0,1,1,1,1,0,0,1,0,1,1,1,1,0,1,1,1,0,0,0,0,1,0,1,1,1,1,0,0,1,0,0,0,1,1]
ptr1 = [213,38,5,16,73,56,177,53,102,49,30,195,151,6,122,225,83,196,90,82,178,45,58,47,130,132,116,110,79,96,139,98,111,22,114,17,51,197,48,55,25,27,52,174,183,136,19,138,1,104,80,143,134,226,250,31,50,109,180,81,252,244,159,239,9,194,150,93,190,223,85,230,124,179,64,172,129,155,193,135,166,34,36,128,33,246,235,87,218,70,76,175,157,89,199,99,105,13,137,208,127,44,75,84,236,91,112,161,18,46,119,117,141,181,41,169,140,3,185,203,8,221,69,88,184,120,123,97,173,145,100,229,11,126,188,245,133,240,192,21,72,222,24,118,215,228,101,206,125,148,219,71,146,43,170,54,249,214,220,94,108,67,156,210,153,187,10,160,29,20,66,28,142,237,189,202,74,154,171,231,158,227,217,164,186,23,65,37,167,149,198,115,152,247,176,40,168,205,15,182,61,200,242,234,113,232,26,238,32,2,95,248,57,68,62,204,12,144,224,207,42,201,165,163,209,92,77,14,211,147,59,251,39,78,233,7,86,121,212,241,60,243,63,131,4,106,216,191,107,162,35,103]
lst2 = [x for x in range(0,252)]
ptr2 = [168,181,74,104,213,184,185,72,25,233,97,144,79,170,237,55,196,243,156,123,180,124,206,192,231,12,212,218,224,122,242,40,34,9,249,27,59,177,85,204,139,200,11,136,215,75,50,240,96,108,92,107,56,52,236,145,19,130,222,2,91,169,64,235,125,17,197,214,100,135,26,121,44,199,179,160,73,51,99,83,93,119,65,14,244,98,234,173,217,109,30,129,187,190,94,127,10,16,45,151,161,143,148,60,67,24,117,76,58,103,166,112,66,220,113,211,186,241,105,70,138,172,228,191,77,33,147,140,230,229,68,53,22,165,221,95,110,219,15,49,115,149,47,137,114,46,189,210,150,120,116,225,154,41,227,43,157,247,1,18,188,193,198,7,158,178,39,38,163,29,3,183,155,102,111,175,176,63,69,78,232,251,202,203,153,159,141,4,82,238,128,239,81,6,250,223,42,171,57,195,126,209,131,36,106,89,146,252,142,31,245,208,86,32,174,207,35,134,90,248,8,61,201,28,132,101,226,37,5,21,133,48,152,182,23,164,80,205,194,54,118,162,62,84,246,71,13,167,87,88,216,20]

for _ in range(252):
  lst1 = func(lst1, ptr1)
  sums.append(lst1)
  lst2 = func(lst2, ptr2)
  ofs.append(lst2[:252])

for name in sorted(glob.glob('*.txt')):
  with open(name) as f:
    lines = f.read()
    lines = lines.replace("[","").replace("]","")
  check = lines.split("\n")
  leck = len(check)
  num_range = [111,112,113,114,115,116,117,118,121,122,123,124,125,126,127,128,131,132,133,134,135,136,137,138,141,142,143,144,145,146,147,148,151,152,153,154,155,156,157,158,161,162,163,164,165,166,167,168,171,172,173,174,175,176,177,178,181,182,183,184,185,186,187,188,211,212,213,214,215,216,217,218,221,222,223,224,225,226,227,228,231,232,233,234,235,236,237,238,241,242,243,244,245,246,247,248,251,252,253,254,255,256,257,258,261,262,263,264,265,266,267,268,271,272,273,274,275,276,277,278,281,282,283,284,285,286,287,288,311,312,313,314,315,316,317,318,321,322,323,324,325,326,327,328,331,332,333,334,335,336,337,338,341,342,343,344,345,346,347,348,351,352,353,354,355,356,357,358,361,362,363,364,365,366,367,368,371,372,373,374,375,376,377,378,381,382,383,384,385,386,387,388,411,412,413,414,415,416,417,418,421,422,423,424,425,426,427,428,431,432,433,434,435,436,437,438,441,442,443,444,445,446,447,448,451,452,453,454,455,456,457,458,461,462,463,464,465,466,467,468,471,472,473,474,475,476,477,478,481,482,483,484,485,486,487,488,511,512,513,514,515,516,517,518,521,522,523,524,525,526,527,528,531,532,533,534,535,536,537,538,541,542,543,544,545,546,547,548,551,552,553,554,555,556,557,558,561,562,563,564,565,566,567,568,571,572,573,574,575,576,577,578,581,582,583,584,585,586,587,588,611,612,613,614,615,616,617,618,621,622,623,624,625,626,627,628,631,632,633,634,635,636,637,638,641,642,643,644,645,646,647,648,651,652,653,654,655,656,657,658,661,662,663,664,665,666,667,668,671,672,673,674,675,676,677,678,681,682,683,684,685,686,687,688,711,712,713,714,715,716,717,718,721,722,723,724,725,726,727,728,731,732,733,734,735,736,737,738,741,742,743,744,745,746,747,748,751,752,753,754,755,756,757,758,761,762,763,764,765,766,767,768,771,772,773,774,775,776,777,778,781,782,783,784,785,786,787,788,811,812,813,814,815,816,817,818,821,822,823,824,825,826,827,828,831,832,833,834,835,836,837,838,841,842,843,844,845,846,847,848,851,852,853,854,855,856,857,858,861,862,863,864,865,866,867,868,871,872,873,874,875,876,877,878,881,882,883,884,885,886,887,888]
  p=0
  bk=open(name,'w')
  while p < leck:
    myList = check[p]
    myList = myList.split(" ")
    ct = []
    for element in myList:
      value = int(element)
      ct.append(value)
    length = len(ct)
    i = 0
    while i < length:
      x = ct[i]
      x = num_range.index(x)
      s = sums[p][i] 
      y = ofs[p][i]
      if s == 1:
        z = (x + y)%512
      else:
        z = (x - y)%512
      z = num_range[z]
      bk.write(str(z))
      bk.write(' ')
      i += 1
    bk.write('\n')
    p+=1
  bk.close()


# columns merged into one giant column
beep = "cat *.txt > look && split -l3 look && rm look nip *.txt"
cmnd = os.popen(beep)
print(cmnd.read())


##pt3
for path in glob.glob("x*"):
  with open(path) as f:
    lines = f.read()
  my_lis = lines.split()
  iter_len = len(my_lis)
  lst=[]
  for e in range(iter_len):
    p = my_lis[e].zfill(3)
    lst.append(p)
  string1=""
  for i in lst:
    string1=string1+i
  x = string1
  def litering_by_three(a):
    return '\n'.join([a[i:i + 42] for i in range(0, len(a), 42)])
  with open(path, 'w') as outfile:
    outfile.write(litering_by_three(x) + "\n")

def rot1():
  for name in sorted(glob.glob('x*'))[::4]:
    with open(name, "r") as myfile:
      x = myfile.readlines()
    test_list = [''.join(i) for i in list(zip(*x))]
    for idx, ele in enumerate(test_list):
      test_list[idx] = ele.replace('\n', '').replace(' ','')
    string = "".join(test_list)
    file = open(name, 'w')
    file.write(string)
    file.close()
rot1()

def rot2():
  for name in sorted(glob.glob('x*'))[1::4]:
    with open(name, "r") as myfile:
      x = myfile.readlines()
    test_list = [''.join(i)[::-1] for i in list(zip(*x))]
    for idx, ele in enumerate(test_list):
      test_list[idx] = ele.replace('\n', '').replace(' ','')
    string = "".join(test_list)
    file = open(name, 'w')
    file.write(string)
    file.close()
rot2()

def rot3():
  for name in sorted(glob.glob('x*'))[2::4]:
    with open(name, "r") as myfile:
      x = myfile.readlines()
    test_list = [''.join(i) for i in list(zip(*x))]
    test_list.reverse()
    for idx, ele in enumerate(test_list):
      test_list[idx] = ele.replace('\n', '').replace(' ','')
    string = "".join(test_list)
    file = open(name, 'w')
    file.write(string)
    file.close()
rot3()

def rot4():
  for name in sorted(glob.glob('x*'))[3::4]:
    with open(name, "r") as myfile:
      x = myfile.readlines()
    test_list = [''.join(i)[::-1] for i in list(zip(*x))]
    test_list.reverse()
    for idx, ele in enumerate(test_list):
      test_list[idx] = ele.replace('\n', '').replace(' ','')
    string = "".join(test_list)
    file = open(name, 'w')
    file.write(string)
    file.close()
rot4()

# rearrange new split blocks
dir_list = os.listdir("./")
dir_list.remove("rish.py")
dir_list = sorted(dir_list)

append_str = 'z'
n_list = [append_str + sub for sub in dir_list]

y = len(dir_list)
l = (n_list)

n = 1
t = int(y/n)
x = "2013"
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

n_list = [x for _,x in sorted(zip(k,l))]
t = int(y-1)

while t >= 0:
  with open(dir_list[t]) as f:
    lines = f.read()
  file = open(n_list[t], 'w')
  file.write(lines)
  file.close()
  t -= 1

beep = "cat zx* > all && rm z* x*"
cmnd = os.popen(beep)
print(cmnd.read())


# minimise
def func(lst, ptr):
   return [lst[idx-1] for idx in ptr]

lettr_range = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","Ð","Þ","Ƿ","Ȝ","Æ","Œ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","ð","þ","ƿ","ȝ","æ","œ"]
lettr_scram = [14, 35, 47, 8, 51, 24, 27, 15, 62, 50, 22, 49, 26, 37, 5, 44, 61, 52, 4, 41, 60, 31, 59, 20, 18, 13, 57, 36, 34, 32, 53, 1, 21, 17, 29, 0, 40, 3, 28, 54, 6, 46, 45, 30, 39, 63, 38, 48, 10, 58, 55, 43, 12, 16, 33, 7, 9, 42, 23, 56, 64, 25, 11, 2, 19]

for _ in range(1):
   nLet = func(lettr_range, lettr_scram)

with open('all') as f:
  txt = f.read()

def procesStng(txt):
  dictionary = {"11":nLet[0],"12":nLet[1],"13":nLet[2],"14":nLet[3],"15":nLet[4],"16":nLet[5],"17":nLet[6],"18":nLet[7],"21":nLet[8],"22":nLet[9],"23":nLet[10],"24":nLet[11],"25":nLet[12],"26":nLet[13],"27":nLet[14],"28":nLet[15],"31":nLet[16],"32":nLet[17],"33":nLet[18],"34":nLet[19],"35":nLet[20],"36":nLet[21],"37":nLet[22],"38":nLet[23],"41":nLet[24],"42":nLet[25],"43":nLet[26],"44":nLet[27],"45":nLet[28],"46":nLet[29],"47":nLet[30],"48":nLet[31],"51":nLet[32],"52":nLet[33],"53":nLet[34],"54":nLet[35],"55":nLet[36],"56":nLet[37],"57":nLet[38],"58":nLet[39],"61":nLet[40],"62":nLet[41],"63":nLet[42],"64":nLet[43],"65":nLet[44],"66":nLet[45],"67":nLet[46],"68":nLet[47],"71":nLet[48],"72":nLet[49],"73":nLet[50],"74":nLet[51],"75":nLet[52],"76":nLet[53],"77":nLet[54],"78":nLet[55],"81":nLet[56],"82":nLet[57],"83":nLet[58],"84":nLet[59],"85":nLet[60],"86":nLet[61],"87":nLet[62],"88":nLet[63]}
  pattern = re.compile('|'.join(sorted(dictionary.keys(), key=len, reverse=True)))
  result = pattern.sub(lambda x: dictionary[x.group()], txt)
  return result

file = open('done', 'w')
file.write(procesStng(txt))
file.close()
