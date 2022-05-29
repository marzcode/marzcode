import pickle
mydict = []
output = open('myfile.pkl', 'wb')
pickle.dump(mydict, output)
output.close()