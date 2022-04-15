import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Splitting independent features and target variable
# Converting them to numpy array
dataset = pd.read_csv('/home/neosoft/Downloads/data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
print(X)
print(y)

# line graph to see linearity
plt.plot(X, y)
plt.show()

# splitting data for training and testing

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

# training the model

regressor = LinearRegression()
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)

# visualization of trained data
plt.scatter(X_train, y_train, color='red')
plt.plot(X_train, regressor.predict(X_train), color='blue')
plt.title('Weight vs Height (Training set)')
plt.xlabel('height')
plt.ylabel('weight')
plt.show()

# visualization of test data
plt.scatter(X_test, y_test, color='red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('weight vs height (Test set)')
plt.xlabel('height')
plt.ylabel('weight')
plt.show()

# displaying predicted values and actual values
df1 = pd.DataFrame(y_test, y_pred)
print(df1)

# Checking score of model
score = r2_score(y_test, y_pred)
print(score)

# predicting weight from given height
print(regressor.predict([[1.5]]))
