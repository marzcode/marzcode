from itertools import cycle
import pickle
import random
import string
import math
import ast
import os

with open("temp/base.txt") as core:
  i = core.read().rstrip()
o = " ".join(word[0].upper()+word[1:] for word in i.split(" "))
str1 = ''.join(o)
def remove(str1):#
  return str1.replace(" ","").replace('“','#').replace('”','#').replace('—','-').replace("’",'~').replace('‘','~').replace('…','.').replace("(","[").replace(")","]").replace("_","").replace("ê","e").replace('à',"a").replace("&","And").replace('é','e').replace("\n","")
str2 = ''.join(remove(str1))
words_input = " ".join(str2)
replacements = [{'a':['t','t','t','t','t','t','t'],'e':['t','t','t','t','t','t','t'],'o':['t','t','t','t','t','t','t'],'t':['t','t','t','t','t','t','t'],'w':['t','t','t','t','t','t','t'],'y':['t','t','t','t','t','t','t'],'b':['t','t','t','t','t'],'c':['t','t','t','t','t'],'d':['t','t','t','t','t'],'f':['t','t','t','t','t'],'g':['t','t','t','t','t'],'h':['t','t','t','t','t'],'i':['t','t','t','t','t'],'k':['t','t','t','t','t'],'l':['t','t','t','t','t'],'m':['t','t','t','t','t'],'n':['t','t','t','t','t'],'p':['t','t','t','t','t'],'r':['t','t','t','t','t'],'s':['t','t','t','t','t'],'u':['t','t','t','t','t'],'v':['t','t','t','t','t'],'x':['t','t','t','t','t'],'z':['t','t','t','t','t'],'A':['t','t'],'B':['t','t'],'C':['t','t'],'D':['t','t'],'E':['t','t'],'F':['t','t'],'G':['t','t'],'H':['t','t'],'I':['t','t'],'J':['t','t'],'K':['t','t'],'L':['t','t'],'M':['t','t'],'N':['t','t'],'O':['t','t'],'P':['t','t'],'Q':['t','t'],'R':['t','t'],'S':['t','t'],'T':['t','t'],'U':['t','t'],'V':['t','t'],'W':['t','t'],'X':['t','t'],'Y':['t','t'],'Z':['t','t'],'.':['t','t'],',':['t','t'],'#':['t','t'],'@':['t'],'?':['t'],'!':['t'],'~':['t'],':':['t'],';':['t'],'$':['t'],'[':['t'],']':['t'],'+':['t'],'-':['t'],'/':['t'],'*':['t'],'j':['t'],'q':['t'],'0':['t'],'1':['t'],'2':['t'],'3':['t'],'4':['t'],'5':['t'],'6':['t'],'7':['t'],'8':['t'],'9':['t'],'CG':['t']}]
output = []
index_replace = 0
count_replace = {key: 0 for key in replacements[0].keys()}

for word in words_input.split():
  if count_replace[word] == len(replacements[index_replace][word]):
    output.append("v")
    index_replace = (index_replace + 1) % len(replacements)
    count_replace = {key: 0 for key in replacements[0].keys()}
  idx_word = count_replace[word]
  output.append(replacements[index_replace][word][idx_word])
  count_replace[word] += 1
output_words = ' '.join(output)

def check_space(string):
  count = 0
  for i in range(0, len(string)):
    if string[i] == "v":
      count += 1
  return count

output_count = check_space(output_words)
random_string = output_words.replace(" ","")
installers = random_string.replace("v"," ")
lines = installers.split()
output = ''
step_size = 10

for i in range(0, len(lines), step_size):
  output += ' v '.join(lines[i:i + step_size]) + ' Z '
output=output.replace(" v ","")
random_string = output[:-1].replace(" ","")
some_text = words_input.replace(" ","")

text_split = []
current_i = 0
for random_substr in random_string.split('Z'):
  text_substr = some_text[current_i:current_i+len(random_substr)]
  text_split.append(text_substr)
  current_i += len(random_substr)

file = open("temp/master", 'r')
lines = file.read()
words = lines.splitlines()
n = 0
while n < len(words):
  words[n] = words[n].rstrip()
  n+=1
span = 10
sets = ["\n".join(words[i:i+span]) for i in range(0, len(words), span)]
list_word = []
for l in sets:
  list_word.append(l.split("\n"))
z = 0

tstr = text_split[0:-1]

while z < len(text_split)-1:
  list = list_word[z]
  my_list = [[''.join(elem)] for elem in list]

  df=open('waste/titsy' + str(z),'w')
  for string in my_list:
    string = string[0]
    splits = string.split(" ")
    a01 = splits[0:7]
    a02 = splits[7:14]
    a03 = splits[14:21]
    a04 = splits[21:28]
    a05 = splits[28:35]
    a06 = splits[35:42]
    a07 = splits[42:47]
    a08 = splits[47:52]
    a09 = splits[52:57]
    a10 = splits[57:62]
    a11 = splits[62:67]
    a12 = splits[67:72]
    a13 = splits[72:77]
    a14 = splits[77:82]
    a15 = splits[82:87]
    a16 = splits[87:92]
    a17 = splits[92:97]
    a18 = splits[97:102]
    a19 = splits[102:107]
    a20 = splits[107:112]
    a21 = splits[112:117]
    a22 = splits[117:122]
    a23 = splits[122:127]
    a24 = splits[127:132]
    a25 = splits[132:134]
    a26 = splits[134:136]
    a27 = splits[136:138]
    a28 = splits[138:140]
    a29 = splits[140:142]
    a30 = splits[142:144]
    a31 = splits[144:146]
    a32 = splits[146:148]
    a33 = splits[148:150]
    a34 = splits[150:152]
    a35 = splits[152:154]
    a36 = splits[154:156]
    a37 = splits[156:158]
    a38 = splits[158:160]
    a39 = splits[160:162]
    a40 = splits[162:164]
    a41 = splits[164:166]
    a42 = splits[166:168]
    a43 = splits[168:170]
    a44 = splits[170:172]
    a45 = splits[172:174]
    a46 = splits[174:176]
    a47 = splits[176:178]
    a48 = splits[178:180]
    a49 = splits[180:182]
    a50 = splits[182:184]
    a51 = splits[184:186]
    a52 = splits[186:188]
    a53 = splits[188:190]
    a54 = splits[190:191]
    a55 = splits[191:192]
    a56 = splits[192:193]
    a57 = splits[193:194]
    a58 = splits[194:195]
    a59 = splits[195:196]
    a60 = splits[196:197]
    a61 = splits[197:198]
    a62 = splits[198:199]
    a63 = splits[199:200]
    a64 = splits[200:201]
    a65 = splits[201:202]
    a66 = splits[202:203]
    a67 = splits[203:204]
    a68 = splits[204:205]
    a69 = splits[205:206]
    a70 = splits[206:207]
    a71 = splits[207:208]
    a72 = splits[208:209]
    a73 = splits[209:210]
    a74 = splits[210:211]
    a75 = splits[211:212]
    a76 = splits[212:213]
    a77 = splits[213:214]
    a78 = splits[214:215]
    a79 = splits[215:216] 

    df.write(f" ('a': {a01}, 'e': {a02}, 'o': {a03}, 't': {a04}, 'w': {a05}, 'y': {a06}, 'b': {a07}, 'c': {a08}, 'd': {a09}, 'f': {a10}, 'g': {a11}, 'h': {a12}, 'i': {a13}, 'k': {a14}, 'l': {a15}, 'm': {a16}, 'n': {a17}, 'p': {a18}, 'r': {a19}, 's': {a20}, 'u': {a21}, 'v': {a22}, 'x': {a23}, 'z': {a24}, 'A': {a25}, 'B': {a26}, 'C': {a27}, 'D': {a28}, 'E': {a29}, 'F': {a30}, 'G': {a31}, 'H': {a32}, 'I': {a33}, 'J': {a34}, 'K': {a35}, 'L': {a36}, 'M': {a37}, 'N': {a38}, 'O': {a39}, 'P': {a40}, 'Q': {a41}, 'R': {a42}, 'S': {a43}, 'T': {a44}, 'U': {a45}, 'V': {a46}, 'W': {a47}, 'X': {a48}, 'Y': {a49}, 'Z': {a50}, '.': {a51}, ',': {a52}, '#': {a53}, '@': {a54}, '?': {a55}, '!': {a56}, '~': {a57}, ':': {a58}, ';': {a59}, '$': {a60}, '[': {a61}, ']': {a62}, '+': {a63}, '-': {a64}, '/': {a65}, '*': {a66}, 'j': {a67}, 'q': {a68}, '0': {a69}, '1': {a70}, '2': {a71}, '3': {a72}, '4': {a73}, '5': {a74}, '6': {a75}, '7': {a76}, '8': {a77}, '9': {a78}, 'CG': {a79})")
    df.write('\n')
  df.close()

  word_replacement = {
  '(':"{",
  ')':"},",
  }
  with open('waste/titsy' + str(z)) as main:
    word = main.read()
    words = " ".join(word)     
    replaced = []
    for y in words:
      replacement = word_replacement.get(y, y)
      replaced.append(replacement)

    text = ' '.join(replaced)

  string = ""

  def remove(string):
    return string.replace(" ","")

  begin = """import pickle\nmydict = [\n"""
  endin = """]\noutput = open('picked""" + str(z) + """.pkl', 'wb')\npickle.dump(mydict, output)\noutput.close()"""

  with open("waste/bib"+ str(z) + ".py", 'w') as outfile2:
    outfile2.write(begin + remove(text) + endin)

  condy = "python3 waste/bib"+str(z)+".py"
  comandy = os.popen(condy)
  print(comandy.read())
  z += 1

z = 0
L = []
while z < len(tstr):
  a = "picked" + str(z) + ".pkl"
  L.append(a)
  z+=1

t = 0
while t < len(tstr):
  cycled_list = cycle(L)
  filename = L[t]
  words_input = " ".join(tstr[t])
  f = open(filename,'rb')
  replacements = pickle.load(f)
  f.close()
  output = []
  index_replace = 0
  count_replace = {key: 0 for key in replacements[0].keys()}
  for word in words_input.split():
    if count_replace[word] == len(replacements[index_replace][word]):
      output.append("L")
      index_replace = (index_replace + 1) % len(replacements)
      count_replace = {key: 0 for key in replacements[0].keys()}
    idx_word = count_replace[word]
    output.append(replacements[index_replace][word][idx_word])
    count_replace[word] += 1
  output_words = ' '.join(output)
  output_words = output_words + " L"

  with open("xfile"+str(t), 'w') as outfile2:
    outfile2.write(output_words)

  t+=1

batch_amount = 1
groups = (output_count+1)/10 #10

group_amount = batch_amount * groups

file = open("temp/dicts", 'r')
lines = file.read()
words = lines.splitlines()

z = 0
n = 0
while n < group_amount:
  final = ''
  for i in range(batch_amount):
    final += words[n + i] + '\n'
  animal_group = open("temp/dictionarys" + str(z), 'w')
  animal_group.write(final)
  animal_group.close()
  n += batch_amount
  z += 1

xt=0
while groups > xt:
  span = 10
  sets = ["\n".join(words[i:i+span]) for i in range(0, len(words), span)]
  list_word = []
  for l in sets:
    list_word.append(l.split("\n"))
  z = 0

  file_reader = open( r'temp/dictionarys' +str(xt), 'r' )
  temp_data = ast.literal_eval(file_reader.read())
  word_replacement = {'L':temp_data}

  with open("xfile"+str(xt)) as main:
    words = main.read().split()
  replace_idx = 0

  for i, y in enumerate(words):
    if y in word_replacement:
      words[i] = word_replacement[y][replace_idx]
      replace_idx  = (replace_idx  + 1)%10  #edit the 4 depending on list count <<<

  str1 = ''.join(words)
  str2 = " ".join(str1)+"\n"

  new_main = open("zxfile" + str(xt), 'w')
  new_main.write(str2)
  new_main.close()

  xt += 1

beep = "cat zxfile* > waste/lev2.txt && rm pick* xf* zx*"
print(beep)
cmd = os.popen(beep)
print(cmd.read())
print(cmd.close())


word_replacement = {'a': 'i', 'b': 'j', 'c': 'k', 'd': 'l', 'e': 'm', 'f': 'n', 'g': 'o', 'h': 'p'}

with open("waste/lev2.txt") as main:
  words = main.read().split()

  replaced = []
  for y in words:
    replacement = word_replacement.get(y, y) if random.random() > 0.6 else y
    replaced.append(replacement)
  text = ' '.join(replaced)
    
def remove(text):
  return text.replace(" ","")

with open("temp/based.txt", 'w') as outfile:
  outfile.write(remove(text))

def round_down(n, decimals=0):
  multiplier = 10 ** decimals
  return math.floor(n * multiplier) / multiplier
str = open('temp/based.txt', 'r').read()
v_ln = len(str)
v_dv = v_ln / 5103
v_rd = round(round_down(v_dv))
v_ml = v_rd * 5103
v_mi = v_ln - v_ml
v_mu = 5103 * (3 - ((v_rd + 1)%3))
if v_mi == 0:
  v_mi += 5103
v_nln = 5103 - v_mi + v_mu
v_con = "% s" % v_nln


def randomword(length):
 letters = "abcdefghijklmnop"
 return ''.join(random.choice(letters) for i in range(length))

with open('waste/TopUp', 'w') as file:
  file.write(randomword(v_nln))

v_cmnd = "paste temp/based.txt waste/TopUp > waste/rdy"
print(v_cmnd)
command = os.popen(v_cmnd)
print(command.read())
print(command.close())

with open(r'waste/rdy', 'r') as file:
  data = file.read()
  data = data.replace("\n","").replace("	","")

with open(r'waste/sorted', 'w') as file:
  file.write(data)

v_fld = "fold -w63 waste/sorted > waste/xnew.txt && split -l 81 waste/xnew.txt"
command = os.popen(v_fld)
print(command.read())
print(command.close())

with open(r"temp/dicts", 'r+') as fd:
  dl = fd.readlines()
  fd.seek(0)
  fd.truncate()
  fd.writelines(dl[int(groups):])

with open(r"temp/master", 'r+') as fm:
  ml = fm.readlines()
  fm.seek(0)
  fm.truncate()
  fm.writelines(ml[output_count+1:])

beep = "mkdir mix && mv x* mix/ && cp source/script.py mix/ && cd mix && python3 script.py && rm s* && cp -r * ../"
cmnd = os.popen(beep)
print(cmnd.read())

#beep = "python3 numberset.py"
#cmnd = os.popen(beep)
#print(cmnd.read())












