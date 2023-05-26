#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 12:19:09 2023

@author: ut
"""

# Sol1

x = input("Enter any file here ")

print("filename: ",x[0:5])
print("extension: ",x[6:])

# Sol2

y = input("Enter any delimit string ").split(",")

print(y)

print(list(y))

print(len(y))

# Sol3

a  = int(input("Enter an number "))
b = int(input("Enter an number "))

print(a+b)

# SOl4

alist = [10,20,30,40,50,10]
blist = [40,50,60,70,80]

print(set(alist).union(set(blist)))

print(set(alist).intersection(set(blist)))

# SOL5

f = input("Give me a string:- ")

if f.isupper() :
    print(f.lower())
else:
    print(f.upper())
    

# SOL6

g = input("Give me a file name:- ")

if g.endswith(".py"):
    print("It is Python file")
elif g.endswith(".pl"):
    print("It is Perl file")
elif g.endswith(".c"):
    print("It is C file")
elif g.endswith(".json"):
    print("It is JSOn file")
else:
    print("It matches none")
    
# SOL7

book = {"chap1":[10,'UK','Mark'] ,"chap2":[20,'US','Pet']}


book["chap1"].append('200pages')

book["chap2"].append('400pages')

print(book["chap1"])

print(book)

# SOL8

s = input("Enter any string:- ")

print(s.isupper())

list(s)

print(list(s))

print(s.lower())

# SOL9

data = {"menu": {
  "id": "file",
  "value": "File",
  "popup": {
    "menuitem": [
      {"value": "New", "onclick": "CreateNewDoc()"},
      {"value": "Open", "onclick": "OpenDoc()"},
      {"value": "Close", "onclick": "CloseDoc()"}
    ]
  }
}}


w = data["menu"]["popup"]["menuitem"][0]["value"]

q = data["menu"]["popup"]["menuitem"][1]["value"]

p = data["menu"]["popup"]["menuitem"][2]["value"]

print(w)
print(q)
print(p)

# SOL 10

z = ()

print(type(z))

z = list(z)

print(type(z))

z.append('unix')

z.extend(['spark', 'scala','hadoop','sccm'])

z.extend(['c','cpp','java','salesforce','sap','unix'])

z.remove('java')

z.remove('salesforce')

z.insert(0,'oracle')

z.insert(5,'mongodb')

z.reverse()

print(len(z))

print(z.count("unix"))




