# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 03:48:46 2022

@author: User
"""

import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('homeprice.csv')
print(df)

plt.xlabel('area')
plt.ylabel('price')
plt.grid()
plt.scatter(df.area, df.price, color = 'blue', marker = '*')

new_df = df.drop('price', axis = "columns")
print(new_df)

price = df.price
print(type(price))
print(np.array(price))

#create linear regression object
reg = linear_model.LinearRegression()
print(reg.fit(new_df, price))

###(1) Predict price of a home with area = 4500 sft
print(reg.predict([[4500]]))
print(reg.coef_) #value of m slope
print(reg.intercept_ )#value of intercept c

###Generate CSV file with list of home price predictions
area_df = pd.read_csv('area.csv')
print(area_df.head())

p = reg.predict(area_df)
print(p)

area_df['predicted_prices'] = p
print(area_df)
print('\n')
