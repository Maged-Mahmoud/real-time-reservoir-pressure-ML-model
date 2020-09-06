# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 20:19:00 2020

@author: Maged
"""



# Importing the libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset

dataset = pd.read_excel('data.xlsx')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1:].values

# Splitting the dataset into the Training set and Test set

# from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0, random_state = 0)

# Feature Scaling

# from sklearn.preprocessing import StandardScaler
# sc_X = StandardScaler()
# X = sc_X.fit_transform(X)
# X_test = sc_X.transform(X_test)
# sc_y = StandardScaler()
# y = sc_y.fit_transform(y)

# Training the Linear Regression model on the whole dataset

from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X, y)
print(lin_reg.score(X,y))
pred1 = lin_reg.predict(X)
print(lin_reg.coef_)
co=lin_reg.coef_
