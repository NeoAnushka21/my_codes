import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential                                # for adding layers
from keras.layers import Conv2D, MaxPooling2D, Dense, Flatten      # this is for applying the process of cnn

# Preprocessing the training data
training_datagen = ImageDataGenerator(rescale=1./255,
                                      shear_range=0.2,
                                      zoom_range=0.2,
                                      horizontal_flip=True)
training_dataset = training_datagen.flow_from_directory('/home/neosoft/Downloads/rock_paper_scissors_dataset',
                                                        target_size=(64, 64),
                                                        batch_size=32,
                                                        class_mode='sparse')

# Preprocessing the testing data
testing_datagen = ImageDataGenerator(rescale=1./255)
testing_dataset = \
    testing_datagen.flow_from_directory('/home/neosoft/Downloads/rock_paper_scissors/Rock-Paper-Scissors/test',
                                          target_size=(64, 64),
                                          batch_size=32,
                                          class_mode='sparse')

# Building the cnn model
cnn_model = tf.keras.models.Sequential()

cnn_model.add(tf.keras.layers.Conv2D(filters=64, kernel_size=3, activation='relu', input_shape=[64, 64, 3]))
cnn_model.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))
cnn_model.add(tf.keras.layers.Conv2D(filters=64, kernel_size=3, activation='relu', input_shape=[64, 64, 3]))
cnn_model.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))
cnn_model.add(tf.keras.layers.Conv2D(filters=64, kernel_size=3, activation='relu', input_shape=[64, 64, 3]))
cnn_model.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))

cnn_model.add(tf.keras.layers.Flatten())

cnn_model.add(tf.keras.layers.Dense(units=128, activation='relu'))

cnn_model.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))

# Training the model
cnn_model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
cnn_model.fit(x=training_dataset, validation_data=testing_dataset, epochs=10)
