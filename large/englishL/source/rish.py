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
        return '\n'.join([a[i:i + 486] for i in range(0, len(a), 486)])
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
  print(d1)
  print(d2)
  print(d3)
  print(d4)
  message = "cat " + d1 + d2 + d3 + d4 + " > " + col + ".txt"
  command = os.popen(message)
  print(command.read())
  print(command.close())
  t1 += 4
  t2 += 4
  t3 += 4
  t4 += 4
  c-= 1

beep = "rm pic*"
cmnd = os.popen(beep)
print(cmnd.read())

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
lst = [155,10,29,67,36,27,12,93,16,73,160,77,22,105,28,113,51,133,106,55,43,58,46,21,40,128,39,76,132,45,99,1,23,146,111,114,25,53,152,14,35,136,34,141,83,87,153,32,126,19,18,138,151,24,137,13,75,159,89,31,143,48,33,78,125,127,104,139,108,30,47,2,72,70,5,20,44,162,79,11,145,63,110,91,88,134,156,109,157,80,101,82,62,148,140,66,74,121,38,161,142,115,56,59,100,103,150,94,123,69,52,95,4,149,85,154,68,8,129,118,116,50,57,15,122,49,26,119,60,86,81,147,120,42,61,124,3,65,97,6,90,112,17,54,37,98,135,92,84,102,131,7,158,130,144,96,107,71,41,117,9,64]
ptr = [37, 156, 40, 155, 104, 122, 131, 148, 111, 36, 85, 157, 116, 149, 39, 151, 51, 142, 48, 15, 98, 147, 14, 19, 55, 54, 132, 26, 135, 84, 59, 118, 140, 86, 103, 123, 8, 61, 45, 62, 25, 27, 107, 2, 109, 21, 18, 100, 5, 141, 120, 144, 73, 133, 87, 138, 101, 93, 136, 83, 88, 110, 33, 76, 53, 112, 12, 10, 79, 50, 16, 3, 7, 60, 89, 78, 56, 52, 75, 38, 128, 82, 30, 44, 74, 114, 69, 159, 94, 102, 42, 145, 65, 92, 119, 29, 127, 71, 35, 97, 106, 113, 121, 126, 162, 47, 158, 108, 115, 95, 31, 160, 6, 130, 91, 150, 70, 23, 129, 77, 64, 117, 1, 143, 81, 153, 124, 80, 24, 146, 90, 105, 28, 68, 4, 17, 161, 152, 13, 41, 137, 134, 99, 139, 72, 11, 34, 49, 58, 96, 46, 154, 9, 67, 22, 63, 43, 57, 125, 32, 20, 66]
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
lst1 = [0,0,0,1,0,1,1,1,1,0,0,0,1,1,0,0,0,0,0,1,0,1,0,1,0,1,1,0,1,0,1,0,0,1,0,0,0,1,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,1,1,1,0,0,0,1,0,0,0,1,1,0,1,1,1,0,1,1,0,0,1,1,1,1,1,0,1,0,0,1,0,1,1,1,1,0,0,0,0,0,0,1,1,1,0,0,0,0,1,1,0,1,0,1,1,1,1,0,1,0,0,1,1,0,1,1,0,1,1,1,1,0,1,1,1,0,1,0,0,1,1,0,1,0,0,0,0,1,0,0,1,1,0,0,1,0,0,1,0,1,0,1,1,1,0,1,1,1]
ptr1 = [109, 134, 125, 130, 95, 104, 129, 90, 160, 13, 19, 49, 39, 43, 45, 21, 124, 161, 107, 100, 33, 7, 118, 98, 105, 6, 71, 78, 147, 162, 88, 10, 55, 36, 108, 120, 1, 46, 64, 91, 47, 28, 9, 115, 77, 150, 135, 102, 16, 83, 132, 27, 123, 35, 127, 103, 156, 17, 65, 3, 154, 80, 37, 153, 22, 67, 26, 68, 75, 14, 25, 94, 15, 11, 42, 48, 110, 99, 144, 29, 44, 93, 116, 73, 97, 50, 34, 96, 146, 92, 32, 30, 131, 63, 138, 148, 85, 54, 87, 72, 81, 41, 59, 57, 18, 128, 86, 53, 155, 62, 61, 137, 76, 23, 151, 121, 84, 52, 51, 106, 112, 157, 145, 82, 70, 20, 152, 89, 141, 140, 60, 38, 12, 66, 114, 149, 159, 56, 101, 4, 111, 69, 136, 5, 158, 122, 8, 126, 58, 74, 139, 142, 31, 24, 40, 117, 79, 2, 143, 119, 113, 133]
lst2 = [x for x in range(0,512)]
ptr2 = [241, 59, 304, 354, 58, 140, 211, 434, 492, 332, 189, 435, 367, 365, 132, 125, 246, 479, 81, 282, 78, 504, 60, 205, 9, 290, 388, 438, 96, 375, 294, 35, 1, 273, 506, 385, 419, 376, 239, 5, 350, 136, 141, 443, 54, 420, 76, 250, 66, 417, 327, 288, 411, 176, 100, 402, 183, 135, 224, 184, 396, 418, 339, 281, 46, 72, 127, 360, 44, 471, 163, 139, 133, 237, 426, 319, 118, 353, 267, 175, 503, 208, 90, 431, 18, 24, 25, 91, 461, 210, 497, 404, 225, 389, 301, 171, 485, 131, 369, 156, 160, 373, 381, 73, 311, 86, 137, 146, 502, 476, 95, 82, 92, 340, 50, 88, 474, 481, 392, 220, 89, 150, 261, 495, 195, 203, 147, 441, 221, 508, 416, 279, 331, 260, 377, 199, 460, 330, 103, 346, 415, 121, 157, 45, 247, 120, 455, 437, 414, 390, 30, 313, 238, 324, 57, 67, 77, 200, 447, 245, 173, 427, 509, 359, 314, 457, 64, 144, 422, 23, 284, 165, 36, 192, 94, 113, 110, 316, 226, 155, 4, 386, 254, 188, 356, 129, 270, 444, 240, 510, 318, 387, 405, 470, 428, 145, 15, 41, 196, 326, 84, 116, 181, 262, 345, 322, 187, 249, 468, 251, 433, 493, 152, 70, 148, 266, 473, 258, 364, 253, 2, 320, 0, 71, 351, 20, 212, 11, 62, 166, 478, 498, 190, 255, 31, 472, 34, 357, 215, 219, 214, 391, 180, 243, 505, 451, 109, 21, 159, 168, 194, 178, 126, 494, 317, 423, 335, 303, 49, 507, 206, 10, 315, 179, 115, 37, 406, 449, 323, 234, 299, 333, 454, 448, 182, 14, 204, 235, 16, 264, 477, 122, 68, 298, 174, 27, 213, 257, 265, 310, 274, 138, 285, 465, 112, 362, 293, 218, 99, 56, 169, 230, 276, 374, 256, 283, 432, 344, 371, 7, 244, 217, 252, 53, 450, 429, 349, 101, 370, 308, 248, 85, 231, 496, 501, 236, 104, 480, 399, 328, 321, 334, 277, 202, 162, 462, 400, 347, 278, 487, 232, 108, 409, 379, 452, 483, 292, 410, 425, 38, 384, 309, 341, 154, 394, 352, 312, 51, 26, 28, 102, 511, 61, 105, 280, 177, 291, 302, 490, 337, 300, 338, 271, 446, 107, 466, 413, 382, 491, 223, 412, 172, 40, 372, 407, 65, 467, 489, 167, 193, 424, 401, 55, 12, 209, 286, 380, 306, 128, 484, 93, 342, 442, 19, 117, 268, 259, 296, 74, 228, 436, 397, 287, 383, 275, 6, 368, 499, 475, 111, 43, 47, 151, 153, 87, 63, 52, 22, 80, 269, 398, 440, 358, 272, 39, 229, 79, 143, 459, 307, 98, 421, 393, 378, 106, 149, 75, 158, 161, 458, 69, 197, 295, 142, 329, 29, 222, 305, 186, 164, 348, 430, 170, 13, 500, 233, 97, 242, 408, 42, 361, 227, 289, 130, 486, 17, 363, 263, 456, 123, 488, 185, 48, 201, 439, 366, 191, 83, 463, 343, 207, 325, 453, 114, 216, 445, 33, 403, 355, 124, 32, 134, 469, 297, 464, 395, 482, 119, 3, 198, 336, 8]
for _ in range(168):
  lst1 = func(lst1, ptr1)
  sums.append(lst1)
  lst2 = func(lst2, ptr2)
  ofs.append(lst2[:162])

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
beep = "cat *.txt > look && split -l42 look && rm look nip *.txt"
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
    return '\n'.join([a[i:i + 486] for i in range(0, len(a), 486)])
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
#x = "13096857429130876425"
x = "26503147"
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
  print(dir_list[t])
  with open(dir_list[t]) as f:
    lines = f.read()
  print(n_list[t])
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
  pattern = re.compile(
    '|'.join(sorted(dictionary.keys(), key=len, reverse=True)))
  result = pattern.sub(lambda x: dictionary[x.group()], txt)
  return result
file = open('done', 'w')
file.write(procesStng(txt))
file.close()
