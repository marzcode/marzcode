# Python3 code to demonstrate
# removal of bad_chars
# using replace()
with open("tol") as main:
    test_string = main.read()
# initializing bad_chars_list
    bad_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
 
# initializing test string
#test_string = "Ge;ek * s:fo ! r;Ge * e*k:s !"
 
# printing original string
    print ("Original String : " + test_string)
 
# using replace() to
# remove bad_chars
    for i in bad_chars :
        test_string = test_string.replace(i, '')
 
# printing resultant string
    print (str(test_string))

#Remove line breaks
with open("toll", 'w') as outfile2:
    outfile2.write(str(test_string))
