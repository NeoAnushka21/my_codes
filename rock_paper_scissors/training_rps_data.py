from keras.preprocessing import image
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
import numpy as np
import random
import cv2
import os


# accessing the images folders
DIRECTORY = r"/home/neosoft/Downloads/rock_paper_scissors_dataset"
CATEGORIES = ['paper1', 'rock1', 'scissors1']

# setting a fixed pixel size for all the images
IMG_SIZE = 150

# creating a list to store image array with it's label
data = []

# read every image, converting and  store it in an array


for category in CATEGORIES:
    fldr = os.path.join(DIRECTORY, category)
    # print(fldr) to check the paths of the folders

    # labeling if it is a rock/paper/scissors as 0 1 2
    label = CATEGORIES.index(category)
    print("Lables:", label)

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
X = X.reshape(2368, 3 * 150 * 150)
print("shape of X after reshape:", X.shape)

print(X)
print(y)

# Random forest
print("Training model using random forest:")
rf_classifier = RandomForestClassifier(n_estimators=10, criterion='entropy', random_state=10)
rf_classifier.fit(X, y)


# cv2 will read the image into an array
arr_img = cv2.imread("/home/neosoft/Downloads/20220426_191010.jpg")
arr_img = cv2.resize(arr_img, (IMG_SIZE, IMG_SIZE))
print(arr_img)
print(arr_img.shape)

arr_img = np.array(arr_img)
arr_img = np.expand_dims(arr_img, axis=0)
print(arr_img)

print("shape of arr_img:", arr_img.shape)

arr_img = arr_img.reshape(1, 3 * 150 * 150)
print(arr_img.shape)

arr_img = arr_img/255
print(arr_img)
print(arr_img.shape)

predticed_class = rf_classifier.predict(arr_img)
print(predticed_class)
