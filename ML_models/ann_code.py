# Importing the libraries

import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, accuracy_score

# Data preprocessing
df = pd.read_csv('/home/neosoft/Downloads/Churn_Modelling.csv')
print(df.columns)
print(df)

X = df.iloc[:, 3:-1].values
y = df.iloc[:, -1].values

print(X)
print(y)

# encoding categorical data

# for gender column
le = LabelEncoder()
X[:, 2] = le.fit_transform(X[:, 2])
print(X[:, 1])

# for geography
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [1])], remainder='passthrough')
X = np.array(ct.fit_transform(X))
print(X)

# splitting dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)

# feature scaling
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
print(X_train)

# building the ann

# Initiating the ann
#  ann variable represents neural network,
#  created as an instance of a sequential class initiates the sequence of layers
ann = tf.keras.models.Sequential()

# Adding input layer and first import layer
ann.add(tf.keras.layers.Dense(units=7, activation='relu'))

# Adding the second hidden layer
ann.add(tf.keras.layers.Dense(units=7, activation='relu'))
# Adding the output layer
ann.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))

# Training the ann model

# Compile the ann
ann.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# fitting the model on training data
ann.fit(X_train, y_train, batch_size=32, epochs=100)

# predicting result for a value
""" Geography: France
Credit Score: 600
Gender: Male
Age: 40 years old
Tenure: 3 years
Balance: $ 60000
Number of Products: 2
Does this customer have a credit card? Yes
Is this customer an Active Member: Yes
Estimated Salary: $ 50000
Let's predict if this customer will leave the bank or not"""
print(ann.predict(sc.transform([[1, 0, 0, 600, 1, 40, 3, 60000, 2, 1, 1, 50000]])) > 0.5)

# Predicting the Test set results
y_pred = ann.predict(X_test)
y_pred = (y_pred > 0.5)
print(np.concatenate((y_pred.reshape(len(y_pred), 1), y_test.reshape(len(y_test), 1)), 1))

# Making the Confusion Matrix

cm = confusion_matrix(y_test, y_pred)
print(cm)
accuracy_score(y_test, y_pred)
