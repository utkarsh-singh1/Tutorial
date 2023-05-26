#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 10:49:32 2023

@author: ut
"""

alist = [10,20,"ko","en","ww","de"]

# List

for i in alist:
    print(i,end="' ")

print("\n")


# Range of values

for i in range(1,23):
    print(i,end=", ")
    
print("\n")
    
for i in range(2,45,4):
    print(i,end=", ")
    
# Dictionary

book = {"chap1":10,"chap2":20,"chap3":40,"chap4":100}

for val in book.values():
    print(val)
    
for key in book.keys():
    print(key)
    
for key in book.keys():
    print(book[key])
    
## use -->> dict(__builtin__) to get list of built in functions