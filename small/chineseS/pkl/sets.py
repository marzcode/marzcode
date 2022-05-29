import pickle

mydict = [
{'a':['1'],'e':['1'],'i':['1'],'o':['1'],'u':['1']},
{'a':['1'],'e':['1'],'i':['1'],'o':['1'],'u':['1']},
{'a':['1'],'e':['1'],'i':['1'],'o':['1'],'u':['1']},
]
output = open('r1.pkl', 'wb')
pickle.dump(mydict, output)
output.close()

mydict = [
{'a':['2'],'e':['2'],'i':['2'],'o':['2'],'u':['2']},
{'a':['2'],'e':['2'],'i':['2'],'o':['2'],'u':['2']},
{'a':['2'],'e':['2'],'i':['2'],'o':['2'],'u':['2']},
]
output = open('r2.pkl', 'wb')
pickle.dump(mydict, output)
output.close()

mydict = [
{'a':['3'],'e':['3'],'i':['3'],'o':['3'],'u':['3']},
{'a':['3'],'e':['3'],'i':['3'],'o':['3'],'u':['3']},
{'a':['3'],'e':['3'],'i':['3'],'o':['3'],'u':['3']},
]
output = open('r3.pkl', 'wb')
pickle.dump(mydict, output)
output.close()