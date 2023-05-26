#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 10:09:36 2023

@author: ut
"""

# Importing all methods

import math

print(math.floor(34.3))

print(math.log(1))

# Importing as alias

import math as m

print(m.tan(2))

print(m.ceil(23.4))


# Import required methods only
# . is not required here

from math import log,tan,floor

print(log(2))


# Import from local files

import mylib

mylib.find1()

# Import Pymongo

import pymongo

