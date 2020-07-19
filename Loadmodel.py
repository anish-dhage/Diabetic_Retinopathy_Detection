# load and evaluate a saved model
from numpy import loadtxt
import tensorflow as tf
from keras.models import load_model
import cv2
import numpy as np
import pandas as pd
import os

# load model
model = tf.keras.models.load_model('model.h5')
# summarize model.
model.summary()

model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

DATADIR = "D:\College\DiabeticRetinopathyML\Trainingdata"

CATEGORIES = ["Healthy", "DR"]

data = pd.read_csv("D:\College\DiabeticRetinopathyML\DRData.csv")
X = data.iloc[:,0].values
Y = data.iloc[:,1].values

training_data = []

i = 0


for img in X:
    image = cv2.imread(os.path.join(DATADIR,img+'.jpg'), cv2.IMREAD_GRAYSCALE)
    newimage =  cv2.resize(image,(64, 64),interpolation=cv2.INTER_AREA)
    training_data.append([newimage, int(Y[i])])
    i = i+1

X = []
y = []

for features, label in training_data:
    X.append(features)
    y.append(label)

X = np.array(X).reshape(-1, 64, 64, 1)
X = X/255.0

#model.fit(X, y, batch_size=8, epochs=3, validation_split=0.1)

pred = model.predict(X, batch_size = 1)

print (pred)
classes = (pred * 1000)
for i in classes:
    if i < 262:
        print(0)
    else:
        print(1)