# -*- coding: utf-8 -*-
"""
A dictionary is a collection which is ordered*, changeable and does not allow duplicates.

"""
#Dictionaries are written with curly brackets, and have keys and values

mydict = {
  "make": "Ford",
  "model": "Mustang",
  "year": 2019
}
print(mydict)

#finding the dictionary keys
x= mydict.keys()

#get the value of "model" key
print(mydict.get("model"))