word_replacement = {'i': 'a', 'j': 'b', 'k': 'c', 'l': 'd', 'm': 'e', 'n': 'f', 'o': 'g', 'p': 'h'}

with open("based.txt") as itt:

    str1 = ''.join(itt)
    main = " ".join(str1)
    words = main.split()

    replaced = []
    for y in words:
        replacement = word_replacement.get(y, y)
        replaced.append(replacement)
    text = ' '.join(replaced)

def remove(string):

	return string.replace(" ","")

print(remove(text))

with open("lev1.txt", 'w') as outfile:
    outfile.write(remove(text))

with open("lev1.txt") as line:

    str1 = ''.join(line)
    n = 4

    print(" ".join([str1[i:i+n] for i in range(0,len(str1),n)]))

with open("lev2.txt", 'w') as outfile:
    outfile.write(" ".join([str1[i:i+n] for i in range(0,len(str1),n)]))

with open("lev2.txt") as dumm:

    import pickle

    pkl_file = open('myfile.pkl', 'rb')
    word_replacement = pickle.load(pkl_file)
    pkl_file.close()

    print (word_replacement)

    input_str = ''.join(dumm)

    words = input_str.split()

    replaced = []
    dic_list_idx = 0
    list_len = len(word_replacement)
    for w in words:
        replacement = word_replacement[dic_list_idx % list_len].get(w, w)
        replaced.append(replacement)
        if replacement == "CG":
            dic_list_idx += 1
    text = ' '.join(replaced)

    print (text)

with open("lev3.txt", 'w') as outfile:
    outfile.write(text)

word_replacement = {'CG': ' ', '#': '"', '~': "'", '[': '(', ']': ')'}

with open("lev3.txt") as main:
    words = main.read().split()

    replaced = []
    for y in words:
        replacement = word_replacement.get(y, y)
        replaced.append(replacement)
    text = ' '.join(replaced)
    print(text)

string = ""

def remove(string):

	return string.replace(" ","")

print(remove(text))

with open("lev4.txt", 'w') as outfile:
    outfile.write(remove(text))
   
with open("lev4.txt") as main:
    merged = main.read()

cap_space = ''.join((' {}'.format(el) if el in 'ОЕАИНТСЛВРКМДПЫУБЯЬГЗЧЙЖХШЮЦЭЩФЁЪ—+' else el for el in merged))

symbol_space = ''.join(('{} '.format(el) if el in '—.,?!:;+' else el for el in cap_space))

with open("outs.txt", 'w') as outfile:
    outfile.write(symbol_space)

fin = open("outs.txt", "rt")
fout = open("output.txt", "wt")

for line in fin:
    fout.write(' '.join(line.split()))
	
fin.close()
fout.close()

with open("output.txt") as result:
    results = result.read()
print(results)
