#--------------------------
#CASE CONVERSION METHODS
#--------------------------

#LOWER METHOD
str = 'THIS IS PYTON'.lower()
#str.method
print(str)

#UPPER METHOD
str = 'THIS IS PYTON'.upper()
#str.method
print(str)

#CAPITALIZE METHOD
str = 'THIS IS PYTON'.capitalize()
#str.method
print(str)

#TITLE METHOD
str = 'THIS IS PYTON'.title()
#str.method
print(str)

#TITLE METHOD
str = 'THIS IS PYTON'.swapcase()
#str.method
print(str)

#--------------------------
#SEARCH AND REPLACE
#--------------------------

#FIND METHOD
text = "PYTHON PROGRAMMING"
print(text.find("G"))     #| Returns index of substring (−1 if not found)
print(text.rfind("G"))    #| Searches from the rightside.
print(text.index("G"))    #| Same as find() but gives error if not found.
print(text.rindex("G"))   #| Index from right.
print(text.count("G"))    #| Counts occurrences of substring.

#REPLACE METHOD
text = "PYTHON PROGRAMMING"
print(text.replace("PYTHON" , "JAVA"))

#SPLIT AND JOIN METHOD
str = "a,b,c"
s = str.split(",")
print('after splitting' , s)

result = ",".join(s)
print(result)




