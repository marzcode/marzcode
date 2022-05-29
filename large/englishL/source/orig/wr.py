file = open("dict.txt", 'r')
lines = file.read()
our_list = lines.splitlines()
chunked_list = list()
chunk_size = 10
for i in range(0, len(our_list), chunk_size):
  chunked_list.append(our_list[i:i+chunk_size])
final = str(chunked_list).replace("[[","[").replace("]]","]").replace("], [","]\n[")
up = open("dicts", 'w')
up.write(final)
up.close()
