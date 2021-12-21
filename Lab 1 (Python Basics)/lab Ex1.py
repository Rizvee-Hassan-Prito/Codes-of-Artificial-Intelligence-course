# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 04:35:29 2021

@author: User
"""

season = "Winter is coming"
i=0
while (i<len(season)):
    print(season[i])
    i+=1

print()
line="This is ME."
k=0
for char in line:
    k+=1
print('Total number of strings in "This is ME.":',k)

print()
nested = ["Arif", "Sagor", "Rahul", [10, 20, 30], "EWU", "AUST", "BUET", "DU"]
k=0
for g in nested:
    print(nested[k])
    k+=1