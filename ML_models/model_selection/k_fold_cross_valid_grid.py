from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('/home/neosoft/Downloads/Social_Network_Ads.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# Splitting the dataset into the Training set and Test set

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=6)

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

# Applying grid search

# Using 2 dictionaries as gamma is used only for rbf and not linear
parameters = [{'C': [0.25, 0.5, 0.75, 1], 'kernel': ['linear']},
              {'C': [0.25, 0.5, 0.75, 1], 'kernel': ['rbf'], 'gamma': [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]}]
grid_obj = GridSearchCV(estimator=svm_classifier, param_grid=parameters, scoring='accuracy', cv=10, n_jobs=-1)
grid_obj.fit(X_train, y_train)
best_accu = grid_obj.best_score_
best_paras = grid_obj.best_params_
print(f"The best accuracy is {best_accu}")
print(f"The best parameters are {best_paras}")
