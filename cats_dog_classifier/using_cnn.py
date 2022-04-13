# importing necessary libraries

import random
import cv2
import os
import keras
import tensorflow
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from keras.models import Sequential                                # for adding layers
from keras.layers import Conv2D, MaxPooling2D, Dense, Flatten      # this is for applying the process of cnn
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score

# accessing the images folders
DIRECTORY = r"/home/neosoft/Downloads/extra_images"
CATEGORIES = ['cats', 'dogs']

# setting a fixed pixel size for all the images
IMG_SIZE = 100

# creating a list to store image array and it's label
data = []

# read every image, converting and  store it in an array


def image_preprocess():
    for category in CATEGORIES:
        fldr = os.path.join(DIRECTORY, category)
        # print(fldr) to check the paths of the folders

        """ labling if it is a dog/cat"""
        label = CATEGORIES.index(category)

        """looking through all the files inside the folder/dir"""
        for img in os.listdir(fldr):
            path_img = os.path.join(fldr, img)

            # print(path_img)   #to see the path
            # break

            """cv2 will read the image into an array"""
            arr_img = cv2.imread(path_img)
            # arr_img = cv2.cvtColor(arr_img,cv2.COLOR_BGR2GRAY)

            """using resize to change size of all images"""
            arr_img = cv2.resize(arr_img, (IMG_SIZE, IMG_SIZE))
            # print(arr_img)
            arr_img = arr_img / 255.

            # plt.imshow(arr_img)     #to display image
            # break
            data.append([arr_img, label])

image_preprocess()

print("length of the list storing all images: ", len(data))

# to shuffle the images, if not model will check all cat images first
random.shuffle(data)

#  For displaying an item(feature,label) of data
# print(data[0])
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
print("shape of y", y.shape)
print("array y:", y)

# creating the model

def cnn_model():
    model01 = Sequential()
    """ to add a convolution layer(number of feature detectors,size of feature detector(matrix),activation)"""
    model01.add(Conv2D(60, (3, 3), activation='relu'))
    model01.add(MaxPooling2D((2, 2)))

    # repeating above step
    model01.add(Conv2D(60, (3, 3), activation='relu'))
    model01.add(MaxPooling2D((2, 2)))

    model01.add(Flatten())
    """ Dense(number of neurons in hidden layer,(100,100,3))"""
    model01.add(Dense(128, input_shape=X.shape[1:], activation='relu'))

    # not the output layer
    """Dense(no.of output neurons [cat and dog so 2],..)"""
    model01.add(Dense(2, activation='softmax'))

    # compiling the model

    model01.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    # fitting the data

    model01.fit(X, y, epochs=5, validation_split=0.1)

cnn_model()
