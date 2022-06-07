# importing necessary libraries

import random
import cv2
import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC

# accessing the images folders
DIRECTORY = r"/home/neosoft/Downloads/extra_images"
CATEGORIES = ['cats', 'dogs']

# setting a fixed pixel size for all the images
IMG_SIZE = 100

# creating a list to store image array with it's label
data = []

# read every image, converting and  store it in an array

def preprocess_image():
    for category in CATEGORIES:
        fldr = os.path.join(DIRECTORY, category)
        # print(fldr) to check the paths of the folders

        """ labeling if it is a dog/cat"""
        label = CATEGORIES.index(category)

        """looking through all the files inside the folder/dir"""
        for img in os.listdir(fldr):
            path_img = os.path.join(fldr, img)

            # print(path_img)   #to see the path
            # break

            """cv2 will read the image into an array"""
            arr_img = cv2.imread(path_img)

            """using resize to change size of all images"""
            arr_img = cv2.resize(arr_img, (IMG_SIZE, IMG_SIZE))
            # print(arr_img)
            arr_img = arr_img / 255.

            # plt.imshow(arr_img)     #to display image
            # break

            data.append([arr_img, label])


preprocess_image()

# print(data)
print("Total Number of images: ", len(data))

# to shuffle the images, if not model will check all cat images first
random.shuffle(data)

# displaying an item(feature,label) of data
print("data[0] : ", data[0])
# 0:cat , 1:Dog

# creating lists for storing features and labels separately
X = []
y = []
for features, labels in data:
    X.append(features)
    y.append(labels)

# converting lists to numpy arrays
X = np.array(X)
y = np.array(y)

print("The length of X and y are :", len(X), len(y))   # checking the lengths to see if they are same
print("shape of X", X.shape)
print("array y:", y)
print("shape of y", y.shape)

# converting array to 2D
X = X.reshape(3552, 3*100*100)

# splitting data into training and testing
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=0)
print("shape of x_train:", x_train.shape)
print("shape of y_train:", y_train.shape)
print("shape of x_test:", x_test.shape)
print("shape of y_test:", y_test.shape)

# Logistic regression
print("This is the Logistic regression model \n It's confusion matrix and classification report")
lr = LogisticRegression(random_state=0, solver='saga', n_jobs=-1)
lr.fit(x_train, y_train)
y_pred = lr.predict(x_test)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

# KNN
print("This is the KNN model \n It's confusion matrix and classification report")
classifier = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2)
classifier.fit(x_train, y_train)
y_pred = classifier.predict(x_test)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Random forest
print("This is the Random forest model \n It's confusion matrix and classification report")
classifier = RandomForestClassifier(n_estimators=10, criterion='entropy', random_state=0)
classifier.fit(x_train, y_train)
y_pred = classifier.predict(x_test)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Decision tree
print("This is the Decision tree model \n It's confusion matrix and classification report")
classifier = DecisionTreeClassifier(criterion='entropy', random_state=0)
classifier.fit(x_train, y_train)
y_pred = classifier.predict(x_test)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

# SVC
print("This is the SVC model \n It's confusion matrix and classification report")
classifier = SVC(kernel='linear', random_state=0)
classifier.fit(x_train, y_train)
y_pred = classifier.predict(x_test)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

# SVC kernel
print("This is the SVC kernel model \n It's confusion matrix and classification report")
classifier = SVC(kernel='rbf', random_state=0)
classifier.fit(x_train, y_train)
y_pred = classifier.predict(x_test)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
