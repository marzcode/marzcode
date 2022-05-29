import pickle
import random
import string
import math
import ast
import os

with open("temp/base.txt") as core:
    str1 = ''.join(core)
def remove(str1):
	return str1.replace("n","п").replace("Ѣ","ъ").replace("ѣ","ъ").replace("І","и").replace("і","и").replace(" ","").replace('"','#').replace('–',"—").replace('-',"—").replace('«',"!!!").replace('(',"!!!").replace('<',"!!!").replace('»',"???").replace(')',"???").replace('>',"???").replace('„','#').replace('“','#')

str2 = ''.join(remove(str1))
words_input = " ".join(str2)

pkl_file = open('temp/myfile.pkl', 'rb')
replacements = pickle.load(pkl_file)
pkl_file.close()

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

new_main = open("waste/lev1.txt", 'w')
new_main.write(output_words)
new_main.close()

file_reader = open( r'temp/dict.txt', 'r' )
temp_data   = ast.literal_eval( file_reader.read( ) )
word_replacement = {'L':temp_data}

with open("waste/lev1.txt") as main:
    words = main.read().split()

replace_idx = 0
for i, y in enumerate(words):
    if y in word_replacement:
        words[i] = word_replacement[y][replace_idx]
        replace_idx  = (replace_idx  + 1)%26624
	#edit the 4 depending on list count <<<

str1 = ''.join(words)
str2 = " ".join(str1)

new_main = open("waste/lev2.txt", 'w')
new_main.write(str2)
new_main.close()

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

########

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
def randStr(chars = string.ascii_uppercase + string.digits, N=v_nln):
	return ''.join(random.choice(chars) for _ in range(N))
with open('waste/TopUp', 'w') as file:
    file.write(randStr(chars='abcdefghijklmnop'))
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

beep = "mkdir mix && mv x* mix/ && cp source/script.py mix/ && cd mix && python3 script.py && rm x* s* && cp -r * ../"
cmnd = os.popen(beep)
print(cmnd.read())

beep = "python3 numberset.py"
cmnd = os.popen(beep)
print(cmnd.read())
