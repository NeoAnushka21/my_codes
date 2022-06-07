import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score

dataset = pd.read_csv("/home/neosoft/Downloads/breast_cancer_data.csv")
# print(dataset.isnull().sum())

X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

log_classifier = LogisticRegression()
log_classifier.fit(X_train, y_train)
y_pred_log = log_classifier.predict(X_test)

c_matrix = confusion_matrix(y_test, y_pred_log)
print("Confusion matrix:")
print(c_matrix)
score = accuracy_score(y_test, y_pred_log)
print("Accuracy :", score)
