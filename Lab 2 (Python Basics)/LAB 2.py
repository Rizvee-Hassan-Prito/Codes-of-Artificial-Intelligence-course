# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 23:53:15 2021

@author: User
"""

x_val = [1, 2, 3]
for x in x_val:
    print(x)
    
for i in range(len(x_val)):
    print(x_val[i])
    
names = ['A', 'B']
marks = ["C", 'D']
print(dict(zip(names, marks)))

cities = ('Dhaka', 'Tokyo', 'Seoul', 'Tehran', 'Doha')
countries = ('BD', 'JP', 'SK', 'IR', 'QR')
for city, country in zip(cities, countries):
    print(f'The city is {city} and corresponding country {country}')

for index, number in enumerate(x_val):
    print(f'xa_val[{index}] = {number}')

def f(string):
    count = 0
    for letter in string:
        if letter == letter.upper() and letter.isalpha():
            count = count + 1
    return count
f('Winter iS Bautiful but Scary')

def f(x):
    return x**3
print(f(3))


f = (lambda x: x**3)(3)
print(f)

import numpy as np

a = np.zeros(3, dtype = int)
print(a)
print(type(a))
print(a.shape)

a = np.zeros(10)
print(a)

a.shape = (5, 2)
print(a)

a = np.empty(3)
print(a)

a = np.linspace(2, 4, 50)
print(a)

import matplotlib.pyplot as plt
plt.plot(a)
plt.title("Hijbiji")
plt.xlabel("Hiji")
plt.ylabel("Biji")
plt.show()

x = np.identity(4)
print(x)

a = np.array((10, 20), dtype = float)
print(a)

z = np.linspace(1, 2, 5)
print(z[0])
print(z[-1])
b = np.array([[1,2], [3,4]])
print(b)
print(b[0,1])
print(b[0, :])
print(b[:,1])

d = np.array((12, 16 , 14, 18), dtype = float)
e = np.array((13, 17, 19, 21))
print(d@e)

a = np.random.randn(5)
print(a)
b = a
b[0] = 0.0
print(a)
print(b)
b = np.copy(a)
print(a)
b[0] = 0
print(b)
b[:] = 1
print(b)
print(a)
x = np.array([1,2,3])
print(np.sin(x))
print(np.sqrt(2 * np.pi))
print(np.where(x > 0, 1, 0))







