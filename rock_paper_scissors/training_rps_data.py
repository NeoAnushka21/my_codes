import random
import cv2
import os
import numpy as np
from keras.preprocessing import image
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
        print(label)

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

# displaying the  1st element of data
print("data[0]: ", data[0])

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

print(X)
print(y)


# Random forest
print("Training model using random forest:")
rf_classifier = RandomForestClassifier(n_estimators=10, criterion='entropy', random_state=10)
rf_classifier.fit(X, y)

# for testing data
DIRECTORY_test = r"/home/neosoft/Downloads/rock_paper_scissors/rock-paper-scissors/Rock-Paper-Scissors/test"
CATEGORIES_test = ['paper_test', 'rock_test', 'scissors_test']

# creating a list to store image array with it's label
data_test = []
# read every image, converting and  store it in an array


def preprocess_image():
    for category in CATEGORIES_test:
        fldr = os.path.join(DIRECTORY_test, category)
        # print(fldr) to check the paths of the folders

        # labeling if it is a rock/paper/scissors as 0 1 2
        label = CATEGORIES_test.index(category)

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

            data_test.append([arr_img, label])


preprocess_image()

# print(data_test)
print("Total Number of images: ", len(data_test))

# to shuffle the images, if not model will check all cat images first
random.shuffle(data_test)

# displaying the  1st element of data_test
# print("data_test[0]: ", data_test[0])

# creating lists for storing features and labels separately
Xt = []
yt = []
for features, labels in data:
    Xt.append(features)
    yt.append(labels)

# converting lists to numpy arrays
X_test = np.array(Xt)
y_test = np.array(yt)

print("x_test shape:", X_test.shape)
X_test = X_test.reshape(1500, 3 * 150 * 150)
print("X_test shape after changing dimensions:", X_test.shape)

y_pred_testing = rf_classifier.predict(X_test)
print("Applying model on testing data:")
cm = confusion_matrix(y_test, y_pred_testing)
print(cm)
score = classification_report(y_test, y_pred_testing)
print(score)

