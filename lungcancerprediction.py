# -*- coding: utf-8 -*-
"""LungCancerPrediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ff7qEm6nx1GA923aEudzHMvOXWs-qIn4
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
tf.random.set_seed(3)
from tensorflow import keras

data=pd.read_csv('/content/lung cancer.csv')

data.head()

data.shape

X=data.drop(columns=['GENDER','LUNG_CANCER'])
Y=data['LUNG_CANCER']

scaler=StandardScaler()
scaler.fit(X)
std_X=scaler.transform(X)

model=keras.Sequential(
    [
        keras.layers.Flatten(input_shape=(14,)),
        keras.layers.Dense(20,activation='relu'),
        keras.layers.Dense(2,activation='sigmoid')
    ]
)
model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])

Y = Y.replace("YES", 1)
Y = Y.replace("NO", 0)

model.fit(X,Y,validation_split=0.1,epochs=10)

a=[]
for i in range(14):
  a.append(input())

arr=np.array(a)

arrr=arr.reshape(1,-1)

std_data=scaler.transform(arrr)

prediction=model.predict(std_data)

label=[np.argmax(prediction)]

print(label)