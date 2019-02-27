# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 17:36:07 2018

@author: rutab
"""

# Official website https://opencv.org/
# Installation through Anaconda https://www.learnopencv.com/install-opencv-3-and-dlib-on-windows-python-only/
import cv2

import numpy as np

import matplotlib.pyplot as plt


# IMPORT IMAGE
original_image_bgr = cv2.imread('./poster1.jpg')


"""
type(original_image_bgr)
plt.subplot(121)

plt.imshow(original_image_bgr)
"""

# COLOUR SPLIT ALGORITHM (BATMAN)
# 
#

# CONVERT TO RGB
# cv2 imports image as BGR, so we convert to RGB for convenience

b,g,r = cv2.split(original_image_bgr)
image_rgb = cv2.merge([r,g,b])

'''
plt.pie([10, 20, 30, 40], labels =['black', 'yellow', 'green', 'red'] , colors = ['#FF00FF', '#00FFFF', '#FF0000', '#808000'], startangle = 90)
# plt.subplot(122);plt.imshow(img2)
'''
# reduce dimensions leaving only list of pixels with rgb values
img2 = image_rgb.reshape(-1, 3)


cv2.imwrite('poster2.jpg', img2)

cov = np.cov(img2,  rowvar=False)

eigvals, eigvecs = np.linalg.eig(cov)
ind = np.argmax(eigvals)
eigenvector = eigvecs[ind]
'''
R = img2.T[0]
G = img2.T[1]
B = img2.T[2]
'''

img_test = original_image_bgr


mean_pixel = np.array([r.mean(), g.mean(), b.mean()])

cof = mean_pixel@eigenvector

C1 = []
pixels1 = []
C2 = []
pixels2 = []

for i in range(image_rgb.shape[0]):
    for j in range(image_rgb.shape[1]):
        pixel = image_rgb[i,j]
        num = pixel@eigenvector
        if num>= cof:
            C1.append((i,j))
            pixels1.append(pixel)
            img_test[i,j]= [0,0,0]
        else:
            C2.append((i,j)) 
            img_test[i,j]= [255,255,255]
            pixels2.append(pixel)
 
R1= pixels1.T           

        
plt.imshow(img_test)  


class Tree(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None

    def method(self):
        root = Tree()
        root.data = "root"
        root.left = Tree()
        root.left.data = "left"
        root.right = Tree()
        root.right.data = "right" 
        return 'instance method called', self
        
        

            
        


  