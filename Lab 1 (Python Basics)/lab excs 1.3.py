# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 22:26:03 2021

@author: User
"""
x=[1,2,4]
y=[5,6,7]
mul= zip(x, y)
sum=0
for x,y in mul:
    sum+=x*y
print(sum)


pairs = ((4, 5), (5,7), (8,9),(7,7))
k=0
count=0
for i in pairs:
    if(pairs[k][0]%2!=0 and pairs[k][1]%2!=0):
       count+=1
    k+=1
print("Number of odd pairs:",count)

count=0
for j in range(0, 100):
    if (j%2 == 0):
       count+=1
print("The total number of even numbers in 0 to 99 is:",count)
