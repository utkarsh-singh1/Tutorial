#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 11:13:14 2023

@author: ut
"""


'''

Functions --->> Types -->> Bulit-in
                ||
            User-Defined
'''

## use -->> dict(__builtin__) to get list of built in functions

print(10,20)

# range

print(list(range(1,11,2)))

val = 10

name = "Utkarsh"

print(id(val))
print(id(name))

print(type(val))
print(type(name))

# To validate the object

print(isinstance(name, str))

print(isinstance(val, int))

print(isinstance(name, int))

print(isinstance(name, list))


name = input("Givw me a name ")


# User-Defined Functions

def func():
    print("Hello World")
    
func()

def add(x,y):
    print(x+y)

add(10,20)


# Fixed arguments
def ret_add(x,y):
    return x + y

print(ret_add(10, 20))

# pre-defined parameters, or Default arguments

def ret_sum(x=0,y=0):
    return x + y

ret_sum()

# Arbitrary arguments- if any object starts from * we call it as tuple
def pri_sum(*kwargs):
    print(kwargs)
    
    sum = 0
    for i in kwargs:
        sum += i
    return sum

pri_sum(10,20,4,6,7,8,9,9,0,1,56,3)


