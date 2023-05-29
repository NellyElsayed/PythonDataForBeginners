# -*- coding: utf-8 -*-
"""
This code provides some examples of python Lists

@author: elsayeny
"""

# declaration a list in python
#String data type list
myList1 = ["dog", "cat", "cow"]
#int data type list
myList2 = [1, 2, 25, 34]
#float data type list
myList3 = [0.23, 1.23, 34.2, 12.3]
#boolean data type list
myList4 = [False, True, True, True, False]

# lists are defined as objects with the data type 'list'
print ( type(myList1) )
print ( type(myList2) )
print ( type(myList3) )
print ( type(myList3) )

#python list can be hold the same datatype values or different datatypes
#in the same list

x = [1, 2.365, "This is a string", 0, "a"]
#print the length of the list
print(len(x))
#print the elements of the list one by one, also here we use the for loop
#in different way that the previous example to show you that the default start of the for loop
#value in python equals to zero
for i in range(len(x)):
    print(x[i])

#Also, we can use the for loop to print list elements using another way:
for j in x:
    print(j)

#print the list as it (the whole list)
print(x)

###############################################################################
#slicing a list is very similar to slicing a string
y = x[0:3] #it saves the first three elements in the List x in the new list y
##note: Lists and strings indexes (elements postiions) starts from zero ( like arrays in Java)
print(y) 
###############################################################################
# append a value to a List
print("x before appending number 3: ", x)
x.append(3) # note: append function changes the list by appending directly 
            #without using assignment statement
print("x after appending number 3: ", x)

###############################################################################
# insert a value to a List
myList = ["green", 'yellow', 'red']
myList.insert(1,'blue')

##############################################################################

# Extends a list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#clear a list
thislist.clear()
print(thislist)







