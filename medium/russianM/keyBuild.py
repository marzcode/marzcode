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
    
    b01 = splits[0:1]
    a01 = splits[1:10]
    a02 = splits[10:18]
    a03 = splits[18:24]
    a04 = splits[24:30]
    a05 = splits[30:36]
    a06 = splits[36:42]
    a07 = splits[42:48]
    a08 = splits[48:54]
    a09 = splits[54:59]
    a10 = splits[59:64]
    a11 = splits[64:69]
    a12 = splits[69:74]
    a13 = splits[74:79]
    a14 = splits[79:84]
    a15 = splits[84:89]
    a16 = splits[89:94]
    a17 = splits[94:99]
    a18 = splits[99:103]
    a19 = splits[103:106]
    a20 = splits[106:109]
    a21 = splits[109:112]
    a22 = splits[112:115]
    a23 = splits[115:118]
    a24 = splits[118:121]
    a25 = splits[121:124]
    a26 = splits[124:127]
    a27 = splits[127:130]
    a28 = splits[130:133]
    a29 = splits[133:136]
    a30 = splits[136:139]
    a31 = splits[139:142]
    a32 = splits[142:145]
    a33 = splits[145:148]
    a34 = splits[148:151]
    a35 = splits[151:154]
    a36 = splits[154:157]
    a37 = splits[157:160]
    a38 = splits[160:163]
    a39 = splits[163:166]
    a40 = splits[166:169]
    a41 = splits[169:171]
    a42 = splits[171:173]
    a43 = splits[173:175]
    a44 = splits[175:177]
    a45 = splits[177:179]
    a46 = splits[179:181]
    a47 = splits[181:183]
    a48 = splits[183:184]
    a49 = splits[184:185]
    a50 = splits[185:186]
    a51 = splits[186:187]
    a52 = splits[187:188]
    a53 = splits[188:189]
    a54 = splits[189:190]
    a55 = splits[190:191]
    a56 = splits[191:192]
    a57 = splits[192:193]
    a58 = splits[193:194]
    a59 = splits[194:195]
    a60 = splits[195:196]
    a61 = splits[196:197]
    a62 = splits[197:198]
    a63 = splits[198:199]
    a64 = splits[199:200]
    a65 = splits[200:201]
    a66 = splits[201:202]
    a67 = splits[202:203]
    a68 = splits[203:204]
    a69 = splits[204:205]
    a70 = splits[205:206]
    a71 = splits[206:207]
    a72 = splits[207:208]
    a73 = splits[208:209]
    a74 = splits[209:210]
    a75 = splits[210:211]
    a76 = splits[211:212]
    a77 = splits[212:213]
    a78 = splits[213:214]
    a79 = splits[214:215]
    a80 = splits[215:216]

# the # symbol is to represent "
# the ~ symbol is to represent '
# the !!! symbol is to represent (
# the ??? symbol is to represent )

    df.write(f" ('%':{b01},'??':{a01},'??':{a02},'??':{a03},'??':{a04},'??':{a05},'??':{a06},'??':{a07},'??':{a08},'??':{a09},'??':{a10},'??':{a11},'??':{a12},'??':{a13},'??':{a14},'??':{a15},'??':{a16},'??':{a17},'??':{a18},'??':{a19},'??':{a20},'??':{a21},'??':{a22},'??':{a23},'??':{a24},'??':{a25},'??':{a26},'.':{a27},',':{a28},'??':{a29},'??':{a30},'??':{a31},'??':{a32},'??':{a33},'??':{a34},'??':{a35},'??':{a36},'??':{a37},'??':{a38},'??':{a39},'??':{a40},'??':{a41},'??':{a42},'??':{a43},'??':{a44},'#':{a45},'!!!':{a46},'???':{a47},'??':{a48},'??':{a49},'??':{a50},'??':{a51},'??':{a52},'??':{a53},'??':{a54},'??':{a55},'??':{a56},'??':{a57},'??':{a58},'??':{a59},'??':{a60},'??':{a61},'??':{a62},'??':{a63},'??':{a64},'???':{a65},'?':{a66},'!':{a67},':':{a68},';':{a69},'0':{a70},'1':{a71},'2':{a72},'3':{a73},'4':{a74},'5':{a75},'6':{a76},'7':{a77},'8':{a70},'9':{a79},'CG':{a80})")
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
