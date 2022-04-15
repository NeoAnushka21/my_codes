from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.model_selection import cross_val_score
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('/home/neosoft/Downloads/Social_Network_Ads.csv')
print(dataset)
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# Splitting the dataset into the Training set and Test set

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=6)
print(X_train.shape)
print(X_test.shape)
# Feature Scaling

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Training the Kernel SVM model on the Training set

svm_classifier = SVC(kernel='rbf', random_state=5)
svm_classifier.fit(X_train, y_train)

# Making the Confusion Matrix

y_pred = svm_classifier.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
print(cm)
score = accuracy_score(y_test, y_pred)
print(score)

# Applying k-fold

k_fold_accuracies = cross_val_score(estimator=svm_classifier, X=X_train, y=y_train, cv=10)
print("Accuracies :", k_fold_accuracies)
acc_mean = k_fold_accuracies.mean()
acc_std = k_fold_accuracies.std()
print(f"Mean of Accuracies : {acc_mean}")
print(f"Standard deviation : {acc_std}")
