# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 18:37:23 2019

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

    feat_vec=list() 
    
###histograma de la imagen original
        

    hist=list()

    hist.append(cv2.calcHist([img], [0, 1, 2], None,	[8, 8,8], [0, 256, 0, 256, 0, 256]))
    
    hist=hist[0].flatten()
    hist=list(hist)
    
    
   
                        
    hist.append(1)
            
    df.append(hist)

    
###genero vectores para fiorito
    
###levanto los nombres para fiorito
    
files=os.listdir()

for i in files:
    
    
    img= cv2.imread(i, -1)

    feat_vec=list() 
    
###histograma de la imagen original
        

    hist=list()

    hist.append(cv2.calcHist([img], [0, 1, 2], None,	[8, 8,8], [0, 256, 0, 256, 0, 256]))
    
    hist=hist[0].flatten()
    hist=list(hist)
                            
    hist.append(0)
          
       
    df.append(hist)

    
###armo data set
df=pd.DataFrame(df)



    


    
    