#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 13:39:44 2023

@author: ut
"""

a = 10
b = 2

# Example 1

if a<b :
    print("I am bigger")
else:
    print("Noooo")

name = "python"


# Example 2
if name.isupper() :
    print("Yes yes upper")
else:
    print("Hahah nooooo it is lower")

# Example 3
if name.startswith("p"):
    print("It is python")
else:
    print("It is Scala")


## Example4
if name.endswith("o"):
    print("It is Golang")
else:
    print("It is python")
    
# Example 5

if name.upper() == "PYTHON" :
    print("Yessss you are right")
else:
    print("Noo whyyyy!")


# example 6
    
if name.capitalize() == "Python" :
    print("Yes it is")
else:
    print("Go away you are lying")