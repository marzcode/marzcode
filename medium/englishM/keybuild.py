import os

file = open("temp/master", 'r')
lines = file.readlines()

list_word = []

for l in lines:
    list_word.append(l.split(" "))

my_list = [line.split(' , ')for line in open ("temp/master")]

df=open('waste/process.txt','w')

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


with open("waste/process.txt") as main:
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

with open("waste/b", 'w') as outfile2:
    outfile2.write(remove(text))

cond = "cat source/a waste/b source/c > temp/pickel.py"
comand = os.popen(cond)
print(comand.read())

condy = "python3 temp/pickel.py"
comandy = os.popen(condy)
print(comandy.read())