# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 21:26:39 2021

@author: elsayeny
"""

 
message1 ="Welcome back to school"
message2 = "New semester"
#Concatenate two strings
outmsg = message1 + message2
print (outmsg)

# add a string to an exisiting string
message1 += " Great day"
print(message1)
#############################################################################
###########substrings:
# padding a string
a =  "word"
# pad the string out to 24 spaces characters
l = 25 - len(a)
a += l*" "

# Extracting certain charaacter in a string
str = "Hello World"
print(len(str))
print(str[0])
print(str[1])
print("Print letter by letter: ")
#for loop syntax in python
for i in range(0,len(str)):
    print(str[i])
    
##############################################################################
#Slicing
#slicing multiple indexes from a string
print("Slicing examples:")
print(str[3:8])
print(str[:3])