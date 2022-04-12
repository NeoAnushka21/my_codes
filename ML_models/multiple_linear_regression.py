import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Importing dataset and splitting it and converting to numpy array
dataset = pd.read_csv('/home/neosoft/Downloads/Fish.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
print(dataset.head())

# rena,img the column names
dataset.rename(columns={'Length1': 'Ver_len', 'Length2': 'Dia_len', 'Length3': 'Crs_length'}, inplace=True)

# displaying any 10 rows
dataset.sample(10)

# Encoding categorical data
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
X = np.array(ct.fit_transform(X))

# Splitting dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# training the model
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# predicting test results
y_pred = regressor.predict(X_test)
np.set_printoptions(precision=3)
print(np.concatenate((y_pred.reshape(len(y_pred), 1), y_test.reshape(len(y_test),1)),1))

# predicting weight of fish from it's dimensions
fish_weight = pd.DataFrame(y_pred, y_test)
print(fish_weight)

# checking the accuracy of model
score = r2_score(y_test, y_pred)
print(score)
