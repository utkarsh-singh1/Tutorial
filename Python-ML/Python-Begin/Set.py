#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 10:34:22 2023

@author: ut
"""

aset = {1,2,3,4,5}

print(aset)

bset = {4,5,6,7,8}

print(bset)


## Union of 2 sets

print(aset.union(bset))

## Intersection

print(aset.intersection(bset))

## Add a new value

aset.add(90)

print(aset)


## Find difference

print(aset.difference(bset))

cset = aset.copy()

print(cset)

print(cset.discard(90))