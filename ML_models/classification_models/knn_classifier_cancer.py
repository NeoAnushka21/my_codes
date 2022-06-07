# Importing required libraries
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.preprocessing import LabelEncoder

# Reading the dataset splitting the IV and DV
dataset = pd.read_csv('/home/neosoft/Downloads/breast_cancer_data.csv')
dataset.sample(10)
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values


le = LabelEncoder()
y = le.fit_transform(y)

# splitting data for training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)

# feature scaling
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


# training the model
knn_classifier = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2)
knn_classifier.fit(X_train, y_train)
y_pred = knn_classifier.predict(X_test)

# making the confusion matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)
score = accuracy_score(y_test, y_pred)
print("Accuracy:", score)

