from itertools import cycle
import pickle
import gc

str1 = "aeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiouaeiou"  
words_input = " ".join(str1)

L = ["r1.pkl","r2.pkl","r3.pkl"] 
cycled_list = cycle(L)

filename = "r3.pkl"

f = open(filename,'rb')
replacements = pickle.load(f)
f.close()

output = []
index_replace = 0
count_replace = {key: 0 for key in replacements[0].keys()}
index = 0

for word in words_input.split(): 
    if count_replace[word] == len(replacements[index_replace][word]):
        if index == 2:

            del replacements
            gc.collect()

            filename = next(cycled_list)
            f = open(filename,'rb')
            replacements = pickle.load(f)
            f.close()

            index = index - 3            
        output.append("L")
        index_replace = (index_replace + 1) % len(replacements)
        count_replace = {key: 0 for key in replacements[0].keys()}
        index += 1
    idx_word = count_replace[word]
    output.append(replacements[index_replace][word][idx_word])
    count_replace[word] += 1
output_words = ' '.join(output)
print(output_words)

