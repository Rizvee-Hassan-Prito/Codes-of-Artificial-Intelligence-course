# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 17:46:26 2021

@author: User
"""
print(1/10 + 2/100 + 5/1000)
print(0/2 + 0/4 + 1/8)
print(1/3)
print(format(1/3, '.2f'))
import math
print(format(math.pi, '.12g'))
print(format(math.pi, '.6f'))
print(2**52 <= 2**56 // 10 < 2**53)
print(2**52)
print(2**56 // 10)
season = "Winter is coming"
print(season)
length= len(season)
print(length)
last=season[length-1]
print(last)
middle = season[length - 8]
print(middle)
for char in season: #in operator
    print(char)
ch = 0
while(ch < length):
    print(season[ch])
    ch+=1
print(season[6:])
print(season[:4])
new = season.upper()
print(new)
cricket = ' BD beat AUS '
cricket.strip()
a = [12, 10, 20, 30]
print(a)
print(type(a))
a[2] = "52"
print(a)
mixed = ["Rahat", "Shamim", "Arif", 10, 20, 30]
print(mixed)
nested = ["Arif", "Sagor", "Rahul", [10, 20, 30], "EWU", "AUST", "BUET", "DU"]
print(nested)
nested.append("Wahid")
print(nested)
if True:
    print('The morning was very charming')
a = False
if a:
    print("a was True")
else:
    print("a was not True")
x = (1, 2 , 3 , 2)
print(type(x))
numbers = (10, 20, 30)
x, y, z = numbers
dictionary = {"EWU": "Dhaka", "RU": "Rajshahi", "KUET": "Khulna"}
print(dictionary)
print(dictionary['EWU'])
s = {'a', 'b'}
s1 = {'b' , "c"}
print(s.intersection(s1))
for x in range(0, 100):
    if x%2 == 0:
        print(x)