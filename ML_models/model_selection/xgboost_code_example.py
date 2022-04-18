import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from xgboost import XGBClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder

dataset = pd.read_csv("/home/neosoft/Downloads/breast_cancer_data.csv")
print(dataset)
X = dataset.iloc[:, 1:-1]
y = dataset.iloc[:, -1]

le = LabelEncoder()
y = le.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=30)


# Feature scaling
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
print(X_train)
print(X_test)

log_classifier = LogisticRegression()
log_classifier.fit(X_train, y_train)
y_pred_log = log_classifier.predict(X_test)
cm1 = confusion_matrix(y_test, y_pred_log)
print("Logistic reg:")
print(cm1)
score1 = accuracy_score(y_test, y_pred_log)
print("Accuracy:", score1)

xgb_classifier = XGBClassifier()
xgb_classifier.fit(X_train, y_train)
y_pred_xgb = xgb_classifier.predict(X_test)
cm2 = confusion_matrix(y_test, y_pred_xgb)
print("xgboost:")
print("Confusion matrix")
print(cm2)
score2 = accuracy_score(y_test, y_pred_xgb)
print("Accuracy :", score2)

k_fold_accuracies = cross_val_score(estimator=xgb_classifier, X=X_train, y=y_train, cv=10)
print("Accuracies :", k_fold_accuracies)
acc_mean = k_fold_accuracies.mean()
acc_std = k_fold_accuracies.std()
print(f"Mean of Accuracies : {acc_mean}")
print(f"Standard deviation : {acc_std}")
