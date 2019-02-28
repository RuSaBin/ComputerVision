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
    


    
    
    def split(self):
        
        cof = self.mean_colour@self.eigenvector    
        leftPixels =  np.full((0,3), 1)
        rightPixels = np.full((0,3), 1) 
          
 
        # SPLIT PIXELS BY EIGENVALUE
      
        for i in range(self.pixels.shape[0]):
            
            num = self.pixels[i]@self.eigenvector
            
            if num>= cof:
                leftPixels=np.vstack((leftPixels, self.pixels[i]))
            else:
                rightPixels=np.vstack((rightPixels, self.pixels[i]))
        
        print("shape l")       
        print(leftPixels.shape)
        print("shape r")      
        print(rightPixels.shape)
                
        # self.left = Tree(leftPixels)
        # self.right = Tree(rightPixels)
        
        return 'instance method called', self
    
    
    def getAllNodes(self):
        
        nodesArray = np.array([])
        
        #check if this is a node and append it, or it's nodes
        if (self.left is not None ) and (self.right is not None ):
            nodesArray += self.left.getAllNodes()
            nodesArray += self.right.getAllNodes()
        
        else:
            nodesArray += self
            
        return nodesArray
    
    
    
    
    # FIND THE NODE WITH THE BIGGEST EIGENVALUE (highest variety of colours)
    def findMaxNode(self):
        
        if (self.left is not None ) and (self.right is not None ):
            if self.left.findMaxNode().eigenvalue > self.right.findMaxNode().eigenvalue:
                return self.left.findMaxNode()
            return self.right.findMaxNode()
        
        return self
    
    
        