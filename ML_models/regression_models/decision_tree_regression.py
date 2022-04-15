import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeRegressor

# Reading the dataset splitting the IV and DV
dataset = pd.read_csv('/home/neosoft/Downloads/50_Startups.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# encoding categorical data
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [3])], remainder='passthrough')
X = np.array(ct.fit_transform(X))

# Training the whole dataset
regressor = DecisionTreeRegressor(random_state=0)
regressor.fit(X, y)

# predicting a result
regressor.predict([[1, 0, 0, 150000, 130000, 280000]])
