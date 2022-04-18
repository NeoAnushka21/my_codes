import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier

dataset = pd .read_csv("/home/neosoft/Downloads/diabetes.csv")
print(dataset.head())
print(dataset.columns)

print(dataset.isnull().sum())

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Feature Scaling

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
print(X_train)
print(X_test)

scores = cross_val_score(DecisionTreeClassifier(), X, y, cv=5)
print("cross validation scores", scores)
print("mean of cross validation scores :", scores.mean())

bag_model = BaggingClassifier(base_estimator=DecisionTreeClassifier(),
                              n_estimators=100,
                              max_samples=0.8,
                              bootstrap=True,
                              oob_score=True,
                              random_state=0)
bag_model.fit(X_train, y_train)

score = bag_model.oob_score_
print("Accuracy score :", score)

