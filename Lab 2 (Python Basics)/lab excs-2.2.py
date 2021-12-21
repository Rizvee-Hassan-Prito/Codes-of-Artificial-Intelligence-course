# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 19:37:37 2021

@author: User
"""
def s_check(x,y):
    for i in x:
        c=False
        for j in y:
            if(i==j):
                c=True
        if(c==False):
            break
    return c        
            
x=input("Enter first sequence: ")
x= x.split()
y=input("Enter first sequence: ")
y= y.split()
print("\nEvery element in a sequence is also an element of second sequnce: ",s_check(x,y))
