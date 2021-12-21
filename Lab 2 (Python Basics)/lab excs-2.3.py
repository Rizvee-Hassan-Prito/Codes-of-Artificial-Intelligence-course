# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 19:23:45 2021

@author: User
"""
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,5,5)
plt.title("Plot of Sin")
plt.xlabel("Value of X")
plt.ylabel("Value of y")
plt.plot(np.sin(x))
plt.show()

x=np.linspace(0,10,5)
plt.title("Plot of Cos")
plt.xlabel("Value of X")
plt.ylabel("Value of y")
plt.plot(np.cos(x))
plt.show()

x=np.linspace(1,10,15)
plt.title("Plot of Tan")
plt.xlabel("Value of X")
plt.ylabel("Value of y")
plt.plot(np.tan(x))
plt.show()