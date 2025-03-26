# -*- coding: utf-8 -*-
"""
Created on Tue Mar 25 20:26:52 2025
Problem Set 0 from MIT OCW 6.001
This program will allow the user the define x and y, then
do a couple quick math problems with them.
@author: ralenjor
"""

import math

print("Enter the value of x.")
x = int(input())
print("Enter the value of y.")
y = int(input())
print("This is x to the power of y.")
print(x**y)
print("This is the base 2 logarithm of x.")
print(math.log2(x))
