# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 10:53:24 2019

@author: lione
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
import os
import pandas as pd
###histograma 1d - total - sup - inf - cent
###histograma 3d - total - sup - inf - cent
###edges - total - sup - inf - cent


###genero df por tipo de feature - a su interior pueden seguir segmentandose x total/sup/inf/cent

###bins
###imagen total
bins1dt=256
bins3dt=[8,8,8]
binsedt=250

###imagen segmentos
bins1ds=80
bins3ds=[6,6,6]
binseds=250



df_h1dt=list()
df_h1ds=list()
df_h1di=list()
df_h1dc=list()

df_h3dt=list()
df_h3ds=list()
df_h3di=list()
df_h3dc=list()

df_edgest=list()
df_edgess=list()
df_edgesi=list()
df_edgesc=list()

target=list()

###genero vectores para ciu_ita
files=os.listdir()

for i in files:
    try:    
        img= cv2.imread(i, -1)
        sup = img[0:10, 0:74]
        inf = img[64:74, 0:74]
        cent = img[22:58, 22:58]



###genero vectores para imagen total
        
        feat_vec_h1d=list()
        feat_vec_h3d=list()
        feat_vec_edges=list()  
    
    ###vector de histograma 1d
        color = ('b','g','r')
        hist_can=list()
        for channel,col in enumerate(color):
            histr = cv2.calcHist([img],[channel],None,[bins1dt],[0,256])
            hist_can.append(histr)
        
        
        for i in hist_can:
            for x in i:
                feat_vec_h1d.append(int(x))
    
    ###vector de histograma 3d
        
        hist=cv2.calcHist([img], [0, 1, 2], None,	bins3dt, [0, 256, 0, 256, 0, 256])
        
        hist=hist.flatten()
        feat_vec_h3d.extend(list(hist))
    
    ###vector de edges
        
        edges = cv2.Laplacian(img,2, 3)
        feat_vec_edges.extend(list(cv2.calcHist([edges],[0],None,[binsedt],[0,256]).flatten()))
        
        df_h1dt.append(feat_vec_h1d)
        df_h3dt.append(feat_vec_h3d)
        df_edgest.append(feat_vec_edges)

###genero vectores para superior
        
        feat_vec_h1d=list()
        feat_vec_h3d=list()
        feat_vec_edges=list() 
    
    ###vector de histograma 1d
        color = ('b','g','r')
        hist_can=list()
        for channel,col in enumerate(color):
            histr = cv2.calcHist([sup],[channel],None,[bins1ds],[0,256])
            hist_can.append(histr)
        
        
        for i in hist_can:
            for x in i:
                feat_vec_h1d.append(int(x))
    
    ###vector de histograma 3d
        
        hist=cv2.calcHist([sup], [0, 1, 2], None,	bins3ds, [0, 256, 0, 256, 0, 256])
        
        hist=hist.flatten()
        feat_vec_h3d.extend(list(hist))
    
    ###vector de edges
        
        edges = cv2.Laplacian(sup,2, 3)
        feat_vec_edges.extend(list(cv2.calcHist([edges],[0],None,[binseds],[0,256]).flatten()))
        
        df_h1ds.append(feat_vec_h1d)
        df_h3ds.append(feat_vec_h3d)
        df_edgess.append(feat_vec_edges)

###genero vectores para inferior
        
        feat_vec_h1d=list()
        feat_vec_h3d=list()
        feat_vec_edges=list() 
    
    ###vector de histograma 1d
        color = ('b','g','r')
        hist_can=list()
        for channel,col in enumerate(color):
            histr = cv2.calcHist([inf],[channel],None,[bins1ds],[0,256])
            hist_can.append(histr)
        
        
        for i in hist_can:
            for x in i:
                feat_vec_h1d.append(int(x))
    
    ###vector de histograma 3d
        
        hist=cv2.calcHist([inf], [0, 1, 2], None,	bins3ds, [0, 256, 0, 256, 0, 256])
        
        hist=hist.flatten()
        feat_vec_h3d.extend(list(hist))
    
    ###vector de edges
        
        edges = cv2.Laplacian(inf,2, 3)
        feat_vec_edges.extend(list(cv2.calcHist([edges],[0],None,[binseds],[0,256]).flatten()))
        
        df_h1di.append(feat_vec_h1d)
        df_h3di.append(feat_vec_h3d)
        df_edgesi.append(feat_vec_edges)

###genero vectores para centro
        
        feat_vec_h1d=list()
        feat_vec_h3d=list()
        feat_vec_edges=list()             
    
    ###vector de histograma 1d
        color = ('b','g','r')
        hist_can=list()
        for channel,col in enumerate(color):
            histr = cv2.calcHist([cent],[channel],None,[bins1ds],[0,256])
            hist_can.append(histr)
        
        
        for i in hist_can:
            for x in i:
                feat_vec_h1d.append(int(x))
    
    ###vector de histograma 3d
        
        hist=cv2.calcHist([cent], [0, 1, 2], None,	bins3ds, [0, 256, 0, 256, 0, 256])
        
        hist=hist.flatten()
        feat_vec_h3d.extend(list(hist))
    
    ###vector de edges
        
        edges = cv2.Laplacian(cent,2, 3)
        feat_vec_edges.extend(list(cv2.calcHist([edges],[0],None,[binseds],[0,256]).flatten()))
        
        
        df_h1dc.append(feat_vec_h1d)
        df_h3dc.append(feat_vec_h3d)
        df_edgesc.append(feat_vec_edges)
        
        target.append(1)
    
    except:
        pass
files=os.listdir()

for i in files:
    try:    
        img= cv2.imread(i, -1)
        sup = img[0:10, 0:74]
        inf = img[64:74, 0:74]
        cent = img[22:58, 22:58]



###genero vectores para imagen total
        
        feat_vec_h1d=list()
        feat_vec_h3d=list()
        feat_vec_edges=list()  
    
    ###vector de histograma 1d
        color = ('b','g','r')
        hist_can=list()
        for channel,col in enumerate(color):
            histr = cv2.calcHist([img],[channel],None,[bins1dt],[0,256])
            hist_can.append(histr)
        
        
        for i in hist_can:
            for x in i:
                feat_vec_h1d.append(int(x))
    
    ###vector de histograma 3d
        
        hist=cv2.calcHist([img], [0, 1, 2], None,	bins3dt, [0, 256, 0, 256, 0, 256])
        
        hist=hist.flatten()
        feat_vec_h3d.extend(list(hist))
    
    ###vector de edges
        
        edges = cv2.Laplacian(img,2, 3)
        feat_vec_edges.extend(list(cv2.calcHist([edges],[0],None,[binsedt],[0,256]).flatten()))
        
        df_h1dt.append(feat_vec_h1d)
        df_h3dt.append(feat_vec_h3d)
        df_edgest.append(feat_vec_edges)

###genero vectores para superior
        
        feat_vec_h1d=list()
        feat_vec_h3d=list()
        feat_vec_edges=list() 
    
    ###vector de histograma 1d
        color = ('b','g','r')
        hist_can=list()
        for channel,col in enumerate(color):
            histr = cv2.calcHist([sup],[channel],None,[bins1ds],[0,256])
            hist_can.append(histr)
        
        
        for i in hist_can:
            for x in i:
                feat_vec_h1d.append(int(x))
    
    ###vector de histograma 3d
        
        hist=cv2.calcHist([sup], [0, 1, 2], None,	bins3ds, [0, 256, 0, 256, 0, 256])
        
        hist=hist.flatten()
        feat_vec_h3d.extend(list(hist))
    
    ###vector de edges
        
        edges = cv2.Laplacian(sup,2, 3)
        feat_vec_edges.extend(list(cv2.calcHist([edges],[0],None,[binseds],[0,256]).flatten()))
        
        df_h1ds.append(feat_vec_h1d)
        df_h3ds.append(feat_vec_h3d)
        df_edgess.append(feat_vec_edges)

###genero vectores para inferior
        
        feat_vec_h1d=list()
        feat_vec_h3d=list()
        feat_vec_edges=list() 
    
    ###vector de histograma 1d
        color = ('b','g','r')
        hist_can=list()
        for channel,col in enumerate(color):
            histr = cv2.calcHist([inf],[channel],None,[bins1ds],[0,256])
            hist_can.append(histr)
        
        
        for i in hist_can:
            for x in i:
                feat_vec_h1d.append(int(x))
    
    ###vector de histograma 3d
        
        hist=cv2.calcHist([inf], [0, 1, 2], None,	bins3ds, [0, 256, 0, 256, 0, 256])
        
        hist=hist.flatten()
        feat_vec_h3d.extend(list(hist))
    
    ###vector de edges
        
        edges = cv2.Laplacian(inf,2, 3)
        feat_vec_edges.extend(list(cv2.calcHist([edges],[0],None,[binseds],[0,256]).flatten()))
        
        df_h1di.append(feat_vec_h1d)
        df_h3di.append(feat_vec_h3d)
        df_edgesi.append(feat_vec_edges)

###genero vectores para centro
        
        feat_vec_h1d=list()
        feat_vec_h3d=list()
        feat_vec_edges=list()  
    
    ###vector de histograma 1d
        color = ('b','g','r')
        hist_can=list()
        for channel,col in enumerate(color):
            histr = cv2.calcHist([cent],[channel],None,[bins1ds],[0,256])
            hist_can.append(histr)
        
        
        for i in hist_can:
            for x in i:
                feat_vec_h1d.append(int(x))
    
    ###vector de histograma 3d
        
        hist=cv2.calcHist([cent], [0, 1, 2], None,	bins3ds, [0, 256, 0, 256, 0, 256])
        
        hist=hist.flatten()
        feat_vec_h3d.extend(list(hist))
    
    ###vector de edges
        
        edges = cv2.Laplacian(cent,2, 3)
        feat_vec_edges.extend(list(cv2.calcHist([edges],[0],None,[binseds],[0,256]).flatten()))
        
        
        df_h1dc.append(feat_vec_h1d)
        df_h3dc.append(feat_vec_h3d)
        df_edgesc.append(feat_vec_edges)
        
        target.append(0)
    
    except:
        break

###armo data set´s

df_h1dt=pd.DataFrame(df_h1dt)
df_h1ds=pd.DataFrame(df_h1ds)
df_h1di=pd.DataFrame(df_h1di)
df_h1dc=pd.DataFrame(df_h1dc)

df_h3dt=pd.DataFrame(df_h3dt)
df_h3ds=pd.DataFrame(df_h3ds)
df_h3di=pd.DataFrame(df_h3di)
df_h3dc=pd.DataFrame(df_h3dc)

df_edgest=pd.DataFrame(df_edgest)
df_edgess=pd.DataFrame(df_edgess)
df_edgesi=pd.DataFrame(df_edgesi)
df_edgesc=pd.DataFrame(df_edgesc)

target=pd.DataFrame(target)