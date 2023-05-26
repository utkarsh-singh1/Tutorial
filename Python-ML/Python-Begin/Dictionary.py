#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 09:58:31 2023

@author: ut
"""

book = {"chap1":10,"chap2":20,"chap3":40,"chap1":100}

# Display all the items in the dictionary
print(book)


# Display individual value
book["chap1"]

# Add new key and value

book["chap4"] = 40

print(book)



# Check key exit or not - method 1

print(book.get("chap10"))

print(book.items())

print(book.keys())

print(book.values())

# Check if keys exist or not -  method 2

if 'chap10' in book:
    print("Here is the value of book[chap10]",book["chap10"])
else:
    print("Nah it does not exist")
    
# Pop items from Dictionary

chook = book.copy()

print(chook)

print(chook.popitem())

print(chook)

print(chook.pop("chap3"))

#   


