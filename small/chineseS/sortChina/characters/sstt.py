
word_replacement = {
'A':"",
'a':"",
'B':"",
'b':"",
'C':"",
'c':"",
'D':"",
'd':"",
'E':"",
'e':"",
'F':"",
'f':"",
'G':"",
'g':"",
'H':"",
'h':"",
'I':"",
'i':"",
}

with open("chomp.txt") as main:

    word = main.read()
    words = " ".join(word)     

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

with open("chompye.txt", 'w') as outfile2:
    outfile2.write(remove(text))
    #outfile2.write(text)
