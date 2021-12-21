# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 19:37:21 2021

@author: User
"""
import math
a=int(input("Enter the coefficent of x^2: "))
b=int(input("Enter the coefficent of x: "))
c=int(input("Enter the constant: "))
print()
root1=(-b+math.sqrt(b**2-4*a*c))/(2*a)
print("Root for plus sign:",root1)
root2=(-b-math.sqrt(b**2-4*a*c))/(2*a)
print("Root for minus sign:",root2)
