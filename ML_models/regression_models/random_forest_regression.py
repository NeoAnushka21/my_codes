# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor

# Importing the dataset
dataset = pd.read_csv('/home/neosoft/Downloads/50_Startups.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# encoding categorical data
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [3])], remainder='passthrough')
X = np.array(ct.fit_transform(X))

# Training the Decision Tree Regression model on the whole dataset
regressor = RandomForestRegressor(n_estimators=25, random_state=0)
regressor.fit(X, y)
RandomForestRegressor(n_estimators=25, random_state=0)


# Predicting a new result
# company from newyork with R&D spend 150000 , Administration spend of 130000 and marketing spend of 280000

regressor.predict([[1, 0, 0, 150000, 130000, 280000]])
