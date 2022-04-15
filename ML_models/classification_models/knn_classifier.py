# Importing required libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score

# Reading the dataset splitting the IV and DV
dataset = pd.read_csv('/home/neosoft/Downloads/IRIS.csv')
dataset.sample(10)
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# visualising scatter plots
sns.scatterplot(x="sepal_length", y="sepal_width", data=dataset, color="red")

sns.scatterplot(x="petal_length", y="petal_width", data=dataset, color="blue")

sns.scatterplot(x="sepal_length", y="petal_length", data=dataset, color="green")

sns.scatterplot(x="sepal_width", y="petal_width", data=dataset, color="pink")

# splitting data for training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0)

# feature scaling
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# training the model
classifier = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
print(np.concatenate((y_pred.reshape(len(y_pred), 1), y_test.reshape(len(y_test), 1)), 1))

# displaying actual result and predicted values in a dataframe
y_pred01 = y_pred.reshape(len(y_pred), 1)
y_test01 = y_test.reshape(len(y_test), 1)
df01 = pd.DataFrame(y_pred01, y_test01)
df01.sample(10)

# making the confusion matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)
accuracy_score(y_test, y_pred)

# predicting the type of flower based on it's dimensions
print(classifier.predict(sc.transform([[5.3, 2.9, 4, 0.9]])))

