# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 04:14:46 2022

@author: User
"""

import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("insurance_data.csv")
print(df.head())
print(df.shape)
plt.scatter(df.age, df.bought_insurance, marker = '*', color = 'red')
    
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df[['age']], df.bought_insurance,test_size=0.3)
print(X_test)

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train, y_train)
y_predict = model.predict(X_test)
print(y_predict)
print(y_test)
print(model.predict_proba(X_test))
print(model.score(X_test, y_test))