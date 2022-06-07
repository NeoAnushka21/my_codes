import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# reading dataset , splitting it in IV and DV
dataset = pd.read_csv('/home/neosoft/Downloads/Position_Salaries.csv')
print(dataset.head())
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, -1].values

# scatter plot to see distribution of datasets
plt.scatter(X, y, color='green')

# training model on whole data for linear regression
reg_lin = LinearRegression()
reg_lin.fit(X, y)

# visualising the linear regression
plt.scatter(X, y, color='red')
plt.plot(X, reg_lin.predict(X), color='blue')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()

# training model on whole dataset for polynomial regression
poly_reg = PolynomialFeatures(degree=4)
X_poly = poly_reg.fit_transform(X)
reg_lin2 = LinearRegression()
reg_lin2.fit(X_poly, y)

# Visualising polynomial regression
plt.scatter(X, y, color='red')
plt.plot(X, reg_lin2.predict(X_poly), color='blue')
plt.title('Polynomial Regression')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

# predicting the salary for given experience

# using linear regression
reg_lin.predict([[6.5]])

# using polynomial regression
reg_lin2.predict(poly_reg.fit_transform([[6.5]]))
