#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 14:04:20 2023

@author: ut
"""

alist = [12,"um","90",90,True]

print(alist)

alist.append(56) # To append single value

print("After append",alist)

alist.extend([29,90,78,67]) # To append multiple values

print("After extend",alist)

alist.insert(1, 190)

print("after insert",alist)

alist.pop()

print("After pop",alist)

alist.remove(True)

alist.remove("90")

alist.remove("um")

print("After remove",alist)

alist.reverse()

print("After reverse", alist) # To reverse the list

alist.sort() # To sort the list

print("After sort",alist)

blist = alist.copy()

print("Afetr copy",blist)

blist.clear()

print("After clear",blist)