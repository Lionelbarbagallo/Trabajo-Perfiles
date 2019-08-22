# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 12:00:31 2019

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


###REVISAR CANTIDAD DE BINS!!! CORREGIR Y REDUCIR!!! PUEDE AJUSTAR MEJOR AHÍ!
###PROBAR MODELO CON Y SIN "DESCRIPTIVOS" DE EDGES
###SI LA PERFORMANCE QUEDA MUY BAJA VOLVER A ANALIZAR EDGES SIN IMAGEN EN GRIS!
###INCORPORAR VARIANZA DEL FILTRO LAPLACIANDO
###ESTUDIAR AED ENTRE VARIABLES CONTINUAD (X EJ. VAR. DEL LAP. Y DISCRETAS, X EJ. TARGET)
###INCORPORAR DESCRIPTIVOS DE HISTOGRAMAS DE COLOR
###INCORPORAR HISTOGRAMAS 2D
###

archivo=list()

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
        archivo.append(i)
        img= cv2.imread(i, -1)
        sup = img[0:10, 0:74]
        inf = img[64:74, 0:74]
        cent = img[22:58, 22:58]

    
###genero vectores para imagen total
        
        feat_vec_h1d=list()
        feat_vec_h3d=list()
        feat_vec_edges=list()  
        
    ###vector de histograma 1d
        hist1d(img, bins1dt, feat_vec_h1d)

    
    ###vector de histograma 3d

        hist3d(img, bins3dt, feat_vec_h3d)

    
    ###vector de edges
        edges(img, feat_vec_edges, 40, 90)
          
        df_h1dt.append(feat_vec_h1d)
        df_h3dt.append(feat_vec_h3d)
        df_edgest.append(feat_vec_edges)
        
###genero vectores para superior
        
        feat_vec_h1d=list()
        feat_vec_h3d=list()
        feat_vec_edges=list() 
            
    ###vector de histograma 1d
        hist1d(sup, bins1ds, feat_vec_h1d)

    
    ###vector de histograma 3d
    
        hist3d(sup, bins3dt, feat_vec_h3d)
    
    ###vector de edges
        edges(sup, feat_vec_edges, 40, 90)
           
        df_h1ds.append(feat_vec_h1d)
        df_h3ds.append(feat_vec_h3d)
        df_edgess.append(feat_vec_edges)
        
###genero vectores para inferior
        
        feat_vec_h1d=list()
        feat_vec_h3d=list()
        feat_vec_edges=list() 
            
    ###vector de histograma 1d
        hist1d(inf, bins1ds, feat_vec_h1d)

    
    ###vector de histograma 3d
    
        hist3d(inf, bins3dt, feat_vec_h3d)
    
    ###vector de edges
        edges(inf, feat_vec_edges, 40, 90)
        
        df_h1di.append(feat_vec_h1d)
        df_h3di.append(feat_vec_h3d)
        df_edgesi.append(feat_vec_edges)
        
###genero vectores para centro
        
        feat_vec_h1d=list()
        feat_vec_h3d=list()
        feat_vec_edges=list()             
            
    ###vector de histograma 1d
    
        hist1d(cent, bins1ds, feat_vec_h1d)

    
    ###vector de histograma 3d
    
        hist3d(cent, bins3dt, feat_vec_h3d)
    
    ###vector de edges
        edges(cent, feat_vec_edges, 40, 90)
    
        df_h1dc.append(feat_vec_h1d)
        df_h3dc.append(feat_vec_h3d)
        df_edgesc.append(feat_vec_edges)
        
        target.append(1)
        
    except:
        pass
    
###genero vectores para fiorito


files=os.listdir()

for i in files:
    try:  
        archivo.append(i)
        img= cv2.imread(i, -1)
        sup = img[0:10, 0:74]
        inf = img[64:74, 0:74]
        cent = img[22:58, 22:58]

    
###genero vectores para imagen total
        
        feat_vec_h1d=list()
        feat_vec_h3d=list()
        feat_vec_edges=list()  
        
    ###vector de histograma 1d
        hist1d(img, bins1dt, feat_vec_h1d)

    
    ###vector de histograma 3d

        hist3d(img, bins3dt, feat_vec_h3d)

    
    ###vector de edges
        edges(img, feat_vec_edges, 40, 90)
          
        df_h1dt.append(feat_vec_h1d)
        df_h3dt.append(feat_vec_h3d)
        df_edgest.append(feat_vec_edges)
        
###genero vectores para superior
        
        feat_vec_h1d=list()
        feat_vec_h3d=list()
        feat_vec_edges=list() 
            
    ###vector de histograma 1d
        hist1d(sup, bins1ds, feat_vec_h1d)

    
    ###vector de histograma 3d
    
        hist3d(sup, bins3dt, feat_vec_h3d)
    
    ###vector de edges
        edges(sup, feat_vec_edges, 40, 90)
           
        df_h1ds.append(feat_vec_h1d)
        df_h3ds.append(feat_vec_h3d)
        df_edgess.append(feat_vec_edges)
        
###genero vectores para inferior
        
        feat_vec_h1d=list()
        feat_vec_h3d=list()
        feat_vec_edges=list() 
            
    ###vector de histograma 1d
        hist1d(inf, bins1ds, feat_vec_h1d)

    
    ###vector de histograma 3d
    
        hist3d(inf, bins3dt, feat_vec_h3d)
    
    ###vector de edges
        edges(inf, feat_vec_edges, 40, 90)
        
        df_h1di.append(feat_vec_h1d)
        df_h3di.append(feat_vec_h3d)
        df_edgesi.append(feat_vec_edges)
        
###genero vectores para centro
        
        feat_vec_h1d=list()
        feat_vec_h3d=list()
        feat_vec_edges=list()             
            
    ###vector de histograma 1d
    
        hist1d(cent, bins1ds, feat_vec_h1d)

    
    ###vector de histograma 3d
    
        hist3d(cent, bins3dt, feat_vec_h3d)
    
    ###vector de edges
        edges(cent, feat_vec_edges, 40, 90)
    
        df_h1dc.append(feat_vec_h1d)
        df_h3dc.append(feat_vec_h3d)
        df_edgesc.append(feat_vec_edges)
        
        target.append(0)

    except:
        pass
    
###armo data set´s

df_h1dt=pd.DataFrame(df_h1dt)
n_cols=df_h1dt.shape[1]
labels=['df_h1dt'+str(x) for x in list(range(0,n_cols))]
df_h1dt.columns=labels

df_h1ds=pd.DataFrame(df_h1ds)
n_cols=df_h1ds.shape[1]
labels=['df_h1ds'+str(x) for x in list(range(0,n_cols))]
df_h1ds.columns=labels

df_h1di=pd.DataFrame(df_h1di)
n_cols=df_h1di.shape[1]
labels=['df_h1di'+str(x) for x in list(range(0,n_cols))]
df_h1di.columns=labels

df_h1dc=pd.DataFrame(df_h1dc)
n_cols=df_h1dc.shape[1]
labels=['df_h1dc'+str(x) for x in list(range(0,n_cols))]
df_h1dc.columns=labels

df_h3dt=pd.DataFrame(df_h3dt)
n_cols=df_h3dt.shape[1]
labels=['df_h3dt'+str(x) for x in list(range(0,n_cols))]
df_h3dt.columns=labels

df_h3ds=pd.DataFrame(df_h3ds)
n_cols=df_h3ds.shape[1]
labels=['df_h3ds'+str(x) for x in list(range(0,n_cols))]
df_h3ds.columns=labels

df_h3di=pd.DataFrame(df_h3di)
n_cols=df_h3di.shape[1]
labels=['df_h3di'+str(x) for x in list(range(0,n_cols))]
df_h3di.columns=labels

df_h3dc=pd.DataFrame(df_h3dc)
n_cols=df_h3dc.shape[1]
labels=['df_h3dc'+str(x) for x in list(range(0,n_cols))]
df_h3dc.columns=labels

df_edgest=pd.DataFrame(df_edgest)
n_cols=df_edgest.shape[1]
labels=['df_edgest'+str(x) for x in list(range(0,n_cols))]
df_edgest.columns=labels

df_edgess=pd.DataFrame(df_edgess)
n_cols=df_edgess.shape[1]
labels=['df_edgess'+str(x) for x in list(range(0,n_cols))]
df_edgess.columns=labels


df_edgesi=pd.DataFrame(df_edgesi)
n_cols=df_edgesi.shape[1]
labels=['df_edgesi'+str(x) for x in list(range(0,n_cols))]
df_edgesi.columns=labels

df_edgesc=pd.DataFrame(df_edgesc)
n_cols=df_edgesc.shape[1]
labels=['df_edgesc'+str(x) for x in list(range(0,n_cols))]
df_edgesc.columns=labels


target=pd.DataFrame(target)
target.columns=['target']

###paso todo a un DF 

tot=pd.concat([target, df_h1ds,df_h3ds, df_edgess,df_h1di,df_h3di, df_edgesi, df_h1dc,df_h3dc, df_edgesc,df_h1dt,df_h3dt, df_edgest,], axis=1)

tot.index=archivo

tot.to_csv('global_feat.csv')
