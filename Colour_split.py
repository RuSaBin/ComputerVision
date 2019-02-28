# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 17:36:07 2018

@author: rutab
"""

# Official website https://opencv.org/
# Install OpenCV instructions: https://pypi.org/project/opencv-python/
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
# plt.subplot(122);plt.imshow(pixel_list_image_rgb)
'''

# reduce dimensions leaving only list of pixels with rgb values
pixel_list_image_rgb = image_rgb.reshape(-1, 3)

pixels = image_rgb.reshape(-1, 3)

'''
cv2.imwrite('poster2.jpg', pixel_list_image_rgb)
'''

# we input plain list of pixel RGB values, without coordinates to create a covariance matrix for all image colour values
covariance = np.cov(pixel_list_image_rgb,  rowvar=False)

# 
eigvals, eigvecs = np.linalg.eig(covariance)
index_eigvec = np.argmax(eigvals)
eigenvector = eigvecs[index_eigvec]
'''
R = pixel_list_image_rgb.T[0]
G = pixel_list_image_rgb.T[1]
B = pixel_list_image_rgb.T[2]
'''
# We create a new image to apply colour segmentation on
image_bgr_colour_reduction = original_image_bgr


mean_pixel = np.array([r.mean(), g.mean(), b.mean()])

cof = mean_pixel@eigenvector

# DIVIDE PIXELS BY EIGENVALUE
#
#

# coords
C1 = []
# RGB values
pixels1 = []
C2 = []
pixels2 = []


# x,y pixel coordinates in an image (2D)
for x in range(image_rgb.shape[0]):
    for y in range(image_rgb.shape[1]):
        pixel = image_rgb[x,y]
        num = pixel@eigenvector
        if num>= cof:
            C1.append((x,y))
            pixels1.append(pixel)
            image_bgr_colour_reduction[x,y]= [0,0,0]
        else:
            C2.append((x,y)) 
            image_bgr_colour_reduction[x,y]= [255,255,255]
            pixels2.append(pixel)
 
'''R1= pixels1.T      '''     

        
plt.imshow(image_bgr_colour_reduction)  

# create tree with one node - all pixels
import trees_class as trees
newTree = trees.Tree(pixel_list_image_rgb)
# newTree.split()

#split tree branches until (??)
'''while True:
    maxNode = newTree.findMaxNode()
    if (maxNode.eigenvalue<10000000):
        break        
    maxNode.split() '''   



'''

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
        
'''        

            
        


  