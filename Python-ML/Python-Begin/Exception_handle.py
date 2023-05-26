#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 10:09:41 2023

@author: ut
"""

import os,shutil

book = {"chap1":10,"chap2":20}

print(book["chap3"])


try:
    book = {"chap1":10,"chap2":20}
    print(book["chap1"])

except Exception as err:
    
    print("something went wrong...Invalid key")
    print("system error",err)
    
print("regular code")

# use dir(__builtin__) to get builtin error list and other values

try: 
    
    book = {"chap1":10,"chap2":20}
    
    try:
        print(book["chap5"])
    except:
        print("Some error happened but i don't know")
    alist = [10,20,30]
    print(alist[8], ...)
    
except KeyError as err:
    print("Something went wrong...Invalid key")
    print("system generated error",err)
except TypeError as err:
    print("Invalid type",err)
except IndentationError as err:
    print("Invalid spece",err)
except IndexError as err:
    print("Invalid index...",err)
except FileNotFoundError as err:
    print("filename not found",err)
except Exception as err:
    print("some error found",err)
print("Some regular code")    



# Find files

for i in os.listdir():
    print(i)
    
try:
    print(os.path.getsize("Lopp.py"))
except Exception as err:
    print("You don't have the file that will give size", err)
    
    
