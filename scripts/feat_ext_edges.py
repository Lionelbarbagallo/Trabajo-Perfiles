# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 20:17:24 2019

@author: lione
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
import os
import pandas as pd

###levanto los nombres de ciudadania italiana
files=os.listdir()

###genero vectores para ciu_ita

df=list()
for i in files:
    
    img= cv2.imread(i, -1)
    sup = img[0:10, 0:74]
    inf = img[64:74, 0:74]
    cent = img[22:58, 22:58]
    feat_vec=list() 
    
###histograma de la imagen original
    img = cv2.Laplacian(img,2, 3)
    feat_vec.extend(list(cv2.calcHist([img],[0],None,[256],[0,256]).flatten()))

    
          
            
###histograma del borde superior
            
    sup = cv2.Laplacian(sup,2, 3)
    feat_vec.extend(list(cv2.calcHist([sup],[0],None,[256],[0,256]).flatten()))
            
###histograma del borde inferior
            
    inf = cv2.Laplacian(inf,2, 3)
    feat_vec.extend(list(cv2.calcHist([inf],[0],None,[256],[0,256]).flatten()))
            
###histograma del centro
                
    cent = cv2.Laplacian(cent,2, 3)
    feat_vec.extend(list(cv2.calcHist([cent],[0],None,[256],[0,256]).flatten()))
                        
    feat_vec.append(1)
            
    df.append(feat_vec)

    
###genero vectores para fiorito
    
###levanto los nombres para fiorito
    
files=os.listdir()

for i in files:
    
    img= cv2.imread(i, -1)
    sup = img[0:10, 0:74]
    inf = img[64:74, 0:74]
    cent = img[22:58, 22:58]
    feat_vec=list() 
    
###histograma de la imagen original
    img = cv2.Laplacian(img,2, 3)
    feat_vec.extend(list(cv2.calcHist([img],[0],None,[256],[0,256]).flatten()))

    
          
            
###histograma del borde superior
            
    sup = cv2.Laplacian(sup,2, 3)
    feat_vec.extend(list(cv2.calcHist([sup],[0],None,[256],[0,256]).flatten()))
            
###histograma del borde inferior
            
    inf = cv2.Laplacian(inf,2, 3)
    feat_vec.extend(list(cv2.calcHist([inf],[0],None,[256],[0,256]).flatten()))
            
###histograma del centro
                
    cent = cv2.Laplacian(cent,2, 3)
    feat_vec.extend(list(cv2.calcHist([cent],[0],None,[256],[0,256]).flatten()))
                
            
    feat_vec.append(0)
       
    df.append(feat_vec)

    
###armo data set
df=pd.DataFrame(df)