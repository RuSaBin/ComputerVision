# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 16:15:31 2018

@author: rutab
reference: https://medium.freecodecamp.org/the-power-of-a-neuron-9b5526c2ed46
"""
import os
from imageio import imread
import numpy as np
from scipy import misc
import pandas as pd

### DATA PREPARATION ###
#file names
train_files = os.listdir('train')

#import images and add labels
train_data = []
for i, im in enumerate(train_files):
    filename = 'train/' + im
    print(filename)
    image = np.asarray(imread(filename))
    train_data.append((image, 1 if im.split("_")[0] == 'thriller' else 0))

#list of arrays of pixels - x and list of labels - y; resizing
size = int(len(train_data))
train_x = np.zeros((size, 64,64,3))
train_y = np.zeros((1,size))  
for i in range(20):
    train_x[i]= misc.imresize(train_data[i][0], (64,64,3))
    train_y[:,i] = train_data[i][1]
    
    
#image flattening
train_flat = train_x.reshape(20, 12288).T

#normalizing
train_flat/=250.


### TRAINING ###
def sigmoid(x):
    return 1/(1+np.exp(-x))

W = np.random.randn(12288,1)
b = np.random.randn()

m=train_flat.shape[1]
α = 0.01

for iter in range(1000):
    
    Z = np.dot(W.T, train_flat)+b
    A = sigmoid(Z)
    dZ = A - train_y
    dA = dZ*sigmoid(A)*(1-sigmoid(A))
    dW = (1/float(m))*np.matmul(train_flat, dA.T)
    db = (1/float(m))*np.sum(dA)
    
    #updating parameters
    W = W - α*dW
    b = b - α*db
    
    

### TESTING ###

lin = np.dot(W.T, train_flat)+b
predictions = sigmoid(lin)

#Transform predictions into 1 or 0
predictions_bi = np.zeros((1,size))
for i in range(20):
    y = predictions[0][i]
    if y>0.5:
        predictions_bi[0][i]=1
#Compare predictions with actual values
crosstab = pd.crosstab(predictions_bi[0], train_y[0])

accuracy = ((crosstab[0][0]+crosstab[1][1])/20)*100

### TEST WITH NEW DATA ###

image = np.asarray(imread('Thriller_test.jpg'))
X = misc.imresize(image, (64,64,3))
X = X.reshape(1, 12288).T
X = X/250.

lin = np.dot(W.T, X)+b
predictions = sigmoid(lin)
predictions < 0.5
#neteisingai   
    