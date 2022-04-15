# Importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.metrics import confusion_matrix, accuracy_score

# reading csv and splitting IV and DV
dataset = pd.read_csv('/home/neosoft/Downloads/Wine.csv')
print(dataset.columns)
print(dataset.head(1))
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:, -1].values

# splitting dataset for training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
print("X_train dataset:", X_train[0])

# feature scaling
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
print("X_train after feature scaling:", X_train)
X_test = sc.transform(X_test)

"""# LDA
lda = LDA(n_components=2)
X_train = lda.fit_transform(X_train, y_train)
X_test = lda.transform(X_test)"""

# Training the model
# Using logistic model
log_classifier = LogisticRegression(random_state=1)
log_classifier.fit(X_train, y_train)
y_pred = log_classifier.predict(X_test)

"""# Using SVC model
svc_classifier = SVC(kernel="linear",random_state=3)
svc_classifier.fit(X_train,y_train)
y_pred = svc_classifier.predict(X_test)"""

# Making the confusion matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(cm)
# Checking the accuracy
score = accuracy_score(y_test, y_pred)
print("Accuracy score:",score)
