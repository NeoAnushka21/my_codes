# Importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score

# Reading csv and splitting IV and DV
dataset = pd.read_csv('/home/neosoft/Downloads/lung_cancer_examples.csv')
dataset = dataset.drop('AreaQ', axis=1)
print(dataset.sample(5))
X = dataset.iloc[:, 2:-1].values
y = dataset.iloc[:, -1].values

# Splitting dataset for training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

# Feature scaling
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Training the model
log_reg_classifier = LogisticRegression(random_state=0)
log_reg_classifier.fit(X_train, y_train)
y_pred = log_reg_classifier .predict(X_test)

# Predicting result- w.r.t age smoking and drinking count
age = int(input("enter age : "))
drink = int(input("Enter number of drinks: "))
smoke = int(input("enter number of cig : "))
print(f"A person with age {age} ,who drinks {drink} times and smokes {smoke} time :")
predicted_value = log_reg_classifier .predict(sc.transform([[age, drink, smoke]]))
print(predicted_value)

if predicted_value == 0:
    print("This person may not get lung cancer")
elif predicted_value == 1:
    print("This person is likely to have cancer")


# Making the confusion matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion matrix:")
print(cm)
# Checking the accuracy
score = accuracy_score(y_test, y_pred)
print("The accuracy of model is :", score)
