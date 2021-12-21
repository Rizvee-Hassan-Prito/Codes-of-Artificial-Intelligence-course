# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 13:11:27 2021

@author: User
"""
import math
"""
x=[1,2,3]
y=[4,7,13]
for i,j in enumerate(y):
    print(f'Human->{i} = Number:{j}')
"""
def root1( x, y):
    root=(-y[1]+math.sqrt(y[1]**2-4*y[0]*x))/(2*y[0])
    return root
def root2( x, y):
    root=(-y[1]-math.sqrt(y[1]**2-4*y[0]*x))/(2*y[0])
    return root
   
a=int(input("Enter the coefficent of x^2: "))
b=int(input("Enter the coefficent of x: "))
print("\nRoot for plus sign:",root1(1,[a,b]))
print("Root for minus sign:",root2(1,[a,b]))


