# Importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score

# reading csv and splitting IV and DV
dataset = pd.read_csv('/home/neosoft/Downloads/lung_cancer_examples.csv')
dataset = dataset.drop('AreaQ', axis=1)
print(dataset.sample(5))
X = dataset.iloc[:, 2:-1].values
y = dataset.iloc[:, -1].values

# splitting dataset for training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

# feature scaling
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Training the model
classifier = LogisticRegression(random_state=0)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)

# predicting result- w.r.t age smoking and drinking count
print(classifier.predict(sc.transform([[40, 5, 2]])))

# Making the confusion matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)
# checking the accuracy
score = accuracy_score(y_test, y_pred)
print(score)
