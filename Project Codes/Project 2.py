# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 12:18:31 2022

@author: User
"""

import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-10,10)
plt.title("Plot of Parabolas")
y1=50*x**2+100*x+1000
plt.plot(x,y1)
plt.xlabel("Blue line-> 50x^2+100x+1000\nOrange Line-> -50x^2+100x-1000")
y2=-50*x**2+100*x-1000
plt.plot(x,y2)
plt.show()
