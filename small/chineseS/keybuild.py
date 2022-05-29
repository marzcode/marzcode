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

    a01 = splits[0:11]
    a02 = splits[11:22]
    a03 = splits[22:33]
    a04 = splits[33:44]
    a05 = splits[44:55]
    a06 = splits[55:66]
    a07 = splits[66:77]
    a08 = splits[77:87]
    a09 = splits[87:97]
    a10 = splits[97:107]
    a11 = splits[107:117]
    a12 = splits[117:127]
    a13 = splits[127:137]
    a14 = splits[137:147]
    a15 = splits[147:157]
    a16 = splits[157:167]
    a17 = splits[167:177] 
    a18 = splits[177:187]
    a19 = splits[187:196]
    a20 = splits[196:206]
    a21 = splits[206:215]
    a22 = splits[215:216]
    
    df.write(f" ('A': {a01}, 'B': {a02}, 'C': {a03}, 'D': {a04}, 'E': {a05}, 'F': {a06}, 'G': {a07}, 'a': {a08}, 'h': {a09}, 'b': {a10}, 'i': {a11}, 'c': {a12}, 'j': {a13}, 'd': {a14}, 'k': {a15}, 'e': {a16}, 'l': {a17}, 'f': {a18}, 'm': {a19}, 'g': {a20}, 'n': {a21}, 'CG': {a22})")
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
