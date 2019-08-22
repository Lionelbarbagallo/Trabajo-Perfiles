# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 20:25:11 2019

@author: lione
"""
import numpy as np
import pandas as pd


###identificar las filas exactas de cada clase!!!!!!!!
###probar el sum/division podria reemplaxzarse por el mean!!!

###divido datasets
ds_train_target=ds.iloc[0:2900,:]

ds_test_target=ds.iloc[2900:3700,:]

ds_train_neg=ds.iloc[4000:6200,:]

ds_test_neg=ds.iloc[6200:7100,:]

###genero dataset de train
train=list()
while len(train)<1000:
    filas=list(np.random.randint(0,2900,50))
    muestra=ds_train_target.iloc[filas,:].sum(axis=0)/50
    train.append(muestra)
while len(train)<2000:
    filas=list(np.random.randint(0,2200,50))
    muestra=ds_train_neg.iloc[filas,:].sum(axis=0)/50
    train.append(muestra)
    
train=pd.DataFrame(train)

y_train=[1]*1000
y_train.extend([0]*1000)

###genero dataset de test

test=list()
while len(test)<400:
    filas=list(np.random.randint(0,800,50))
    muestra=ds_test_target.iloc[filas,:].sum(axis=0)/50
    test.append(muestra)
while len(test)<800:
    filas=list(np.random.randint(0,900,50))
    muestra=ds_test_neg.iloc[filas,:].sum(axis=0)/50
    test.append(muestra)
    
test=pd.DataFrame(test)

y_test=[1]*400
y_test.extend([0]*400)