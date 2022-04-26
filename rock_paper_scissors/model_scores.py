import random
import cv2
import os
import numpy as np

from keras.preprocessing.image import ImageDataGenerator
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC


# accessing the images folders
DIRECTORY = r"/home/neosoft/Downloads/RPS_testing"
CATEGORIES = ['paper1', 'rock1', 'scissors1']

# setting a fixed pixel size for all the images
IMG_SIZE = 150

# creating a list to store image array with it's label
data = []

# read every image, converting and  store it in an array


def preprocess_image():
    for category in CATEGORIES:
        fldr = os.path.join(DIRECTORY, category)
        # print(fldr) to check the paths of the folders

        # labeling if it is a rock/paper/scissors as 0 1 2
        label = CATEGORIES.index(category)

        # looking through all the files inside the folder/dir
        for img in os.listdir(fldr):
            path_img = os.path.join(fldr, img)

            # print(path_img)   #to see the path
            # break

            # cv2 will read the image into an array
            arr_img = cv2.imread(path_img)

            # using resize to change size of all images
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

# displaying the label of 1st element of data
for i in len(data):
    print(data[i][1])
# print("data[0][1] : ", data[0][1])

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
print("Shape of X", X.shape)
print("Array y:", y)
print("Shape of y", y.shape)

# converting array to 2D
X = X.reshape(1500, 3 * 150 * 150)

# splitting data into training and testing
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=30)
print("shape of x_train:", x_train.shape)
print("shape of y_train:", y_train.shape)
print("shape of x_test:", x_test.shape)
print("shape of y_test:", y_test.shape)

# Logistic regression
print("This is the Logistic regression model \n It's confusion matrix and classification report")
logreg_classifier = LogisticRegression(random_state=10, solver='saga', n_jobs=-1)
logreg_classifier.fit(x_train, y_train)
y_pred01 = logreg_classifier.predict(x_test)
print(confusion_matrix(y_test, y_pred01))
print(classification_report(y_test, y_pred01))

# KNN
print("This is the KNN model \n It's confusion matrix and classification report")
knn_classifier = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2)
knn_classifier.fit(x_train, y_train)
y_pred02 = knn_classifier.predict(x_test)
print(confusion_matrix(y_test, y_pred02))
print(classification_report(y_test, y_pred02))

# Random forest
print("This is the Random forest model \n It's confusion matrix and classification report")
rf_classifier = RandomForestClassifier(n_estimators=10, criterion='entropy', random_state=0)
rf_classifier.fit(x_train, y_train)
y_pred03 = rf_classifier.predict(x_test)
print(confusion_matrix(y_test, y_pred03))
print(classification_report(y_test, y_pred03))

# Decision tree
print("This is the Decision tree model \n It's confusion matrix and classification report")
dt_classifier = DecisionTreeClassifier(criterion='entropy', random_state=0)
dt_classifier.fit(x_train, y_train)
y_pred04 = dt_classifier.predict(x_test)
print(confusion_matrix(y_test, y_pred04))
print(classification_report(y_test, y_pred04))

# SVC
print("This is the SVC model \n It's confusion matrix and classification report")
svc_classifier = SVC(kernel='linear', random_state=0)
svc_classifier.fit(x_train, y_train)
y_pred05 = svc_classifier.predict(x_test)
print(confusion_matrix(y_test, y_pred05))
print(classification_report(y_test, y_pred05))

# SVC kernel
print("This is the SVC kernel model \n It's confusion matrix and classification report")
svc_ker_classifier = SVC(kernel='rbf', random_state=0)
svc_ker_classifier.fit(x_train, y_train)
y_pred06 = svc_ker_classifier.predict(x_test)
print(confusion_matrix(y_test, y_pred06))
print(classification_report(y_test, y_pred06))
