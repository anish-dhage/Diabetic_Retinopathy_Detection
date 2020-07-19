import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
import pandas as pd
import tensorflow as tf
from tensorflow.python.keras.datasets import cifar10
from tensorflow.python.keras.preprocessing.image import ImageDataGenerator
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.python.keras.layers import Conv2D, MaxPooling2D
#from tqdm import tqdm

def getVal(x):
    if x>0:
        return 1
    else :
        return 0

DATADIR = "D:\College\DiabeticRetinopathyML\Trainingdata"

CATEGORIES = ["Healthy", "DR"]

data = pd.read_csv("D:\College\DiabeticRetinopathyML\DRData.csv")
X = data.iloc[:,0].values
Y = data.iloc[:,1].values

training_data = []

i = 0


for img in X:
    image = cv2.imread(os.path.join(DATADIR,img+'.jpg'), cv2.IMREAD_GRAYSCALE)
    newimage =  cv2.resize(image,(128, 128),interpolation=cv2.INTER_AREA)
    training_data.append([newimage, getVal(int(Y[i]))])
    i = i+1

X = []
y = []

for features, label in training_data:
    X.append(features)
    y.append(label)


X = np.array(X).reshape(-1, 128, 128, 1)
X = X/255.0
model = Sequential()

model.add(Conv2D(256, (3, 3), input_shape=X.shape[1:]))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(256, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors

model.add(Dense(64))

model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

model.fit(X, y, batch_size=16, epochs=1, validation_split=0.1)