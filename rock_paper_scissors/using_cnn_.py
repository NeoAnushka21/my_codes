from keras.preprocessing import image
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from keras.models import Sequential                                # for adding layers
from keras.layers import Conv2D, MaxPooling2D, Dense, Flatten      # this is for applying the process of cnn
import matplotlib.pyplot as plt
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


def preprocess_image():
    for category in CATEGORIES:
        fldr = os.path.join(DIRECTORY, category)
        # print(fldr) to check the paths of the folders

        # labeling if it is a rock/paper/scissors as 0 1 2
        label = CATEGORIES.index(category)
        print("Lables:",label)

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

# to shuffle the images, if not model will check all  paper images first
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

print(X)
print(y)

cnn_classifier_model = Sequential()
""" to add a convolution layer(number of feature detectors,size of feature detector(matrix),activation)"""
cnn_classifier_model.add(Conv2D(60, (3, 3), activation='relu'))
cnn_classifier_model.add(MaxPooling2D((2, 2)))

# repeating above step
cnn_classifier_model.add(Conv2D(60, (3, 3), activation='relu'))
cnn_classifier_model.add(MaxPooling2D((2, 2)))

cnn_classifier_model.add(Flatten())
""" Dense(number of neurons in hidden layer,(100,100,3))"""
cnn_classifier_model.add(Dense(128, activation='relu'))

# not the output layer
"""Dense(no.of output neurons [paper ,rock scissor so 3],..)"""
cnn_classifier_model.add(Dense(3, activation='softmax'))

# compiling the model

cnn_classifier_model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
# fitting the data

cnn_classifier_model.fit(X, y, epochs=5, validation_split=0.1)

cnn_classifier_model.summary()

hist = cnn_classifier_model.fit(X, y, epochs=5, validation_split=0.1)
print(hist.history)
