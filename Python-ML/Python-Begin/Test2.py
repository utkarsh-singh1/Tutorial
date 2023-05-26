#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 12:13:16 2023

@author: ut
"""

# Sol1

import os
import shutil

for i in os.listdir():
    print(i)
    
# Sol2

for i in os.listdir('/usr/bin'):
    print(i)
    
# Sol3

fp = open('1.csv','w')
fp1 = open('2.csv','w')
fp2 = open('3.csv','w')

print(os.listdir())

for i in os.listdir():
    if i.endswith(".csv"):
        os.remove(i)

print(os.listdir())


# Sol4

for i in os.listdir():
    print("{} {}bytes".format(i,os.stat(i).st_size))
    
    
# Sol5

mk = os.mkdir('dir1')
mk1 = os.mkdir('dir2')

for file in os.listdir('source'):
    print(shutil.copy(file,'destination'))
    

print(os.listdir())

for i in os.listdir():
    if os.path.isfile(i):
        print(i)
        
print("\n")
print("-------------------------------")

for i in os.listdir():
    if os.path.isdir(i):
        print(i)
        
# Sol6

x = os.mkdir('source')
y = os.mkdir('destination')

for file in os.listdir('source'):
    shutil.copy(file,'destination')


for file in os.listdir('destination'):
    print(file)

# Sol7

os.rmdir('dir1')
os.rmdir('dir2')

for i in os.listdir():
    print(i)

for i  in range(1,100):
    os.mkdir("dir{}".format(i))
    
for i in os.listdir():
    if os.path.isdir(i):
        print(i)

# Sol8


