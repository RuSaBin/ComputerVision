# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 16:25:30 2018

@author: rutab
"""
import cv2

import numpy as np

import matplotlib.pyplot as plt



class Tree():
    def __init__(self, pixels):
        self.left = None
        self.right = None
        self.pixels = pixels 
        self.eigenvector = None        
        self.eigenvalue = None
        self.mean_colour = None
        
        
        # constructor gets plain list of pixel RGB values, without coordinates
        
        #calculate max eigenvalue and it's eigenvector
        covariance = np.cov(self.pixels,  rowvar=False)
        eigvals, eigvecs = np.linalg.eig(covariance)
        index_eigvec = np.argmax(eigvals)
        self.eigenvector = eigvecs[index_eigvec]        
        self.eigenvalue = eigvals[index_eigvec]
        
#        np.array(mean_data)[:,0]
        # calculate mean colour
        r = np.array(self.pixels)[:,0] 
        g = np.array(self.pixels)[:,1] 
        b = np.array(self.pixels)[:,2]    
        self.mean_colour = np.array([r.mean(), g.mean(), b.mean()])
    

    def max_var_leaf(self):
        if self.left == None:
            return self
        else:
            return 'hello'
    
    
    def split(self):
        
        
        cof = self.mean_colour@self.eigenvector
        
        # SPLIT PIXELS BY EIGENVALUE
        #
        #        
        leftPixels = []
        rightPixels = []        
        for i in range(self.pixels.shape[0]):
            num = self.pixels[i]@self.eigenvector
            if num>= cof:
                leftPixels.append(self.pixels[i])
            else:
                rightPixels.append(self.pixels[i])
        
        # create new branches for the split node
        self.left = Tree(leftPixels)
        self.right = Tree(rightPixels)
        
        return 'instance method called', self
    
    # FIND THE NODE WITH THE BIGGEST EIGENVALUE (highest variety of colours)
    def findMaxNode(self):
        
        if (self.left is not None ) and (self.right is not None ):
            if self.left.eigenvalue > self.right.eigenvalue:
                return self.left
            return self.right
        
        return self
        