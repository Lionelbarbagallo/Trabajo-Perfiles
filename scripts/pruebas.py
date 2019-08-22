# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 22:28:25 2019

@author: lione
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
import os
import pandas as pd
from sklearn import svm
from sklearn.decomposition import PCA
import random
from PIL import Image


basewidth = 300
img = Image.open(i)
wpercent = (basewidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((basewidth,hsize), Image.ANTIALIAS)

img.save('sompic.jpg') 


files=os.listdir()

hist_grupo=list()
for i in files:
    img = cv2.imread(i, -1)
    

    color = ('b','g','r')
    hist_can=list()
    for channel,col in enumerate(color):
        histr = cv2.calcHist([img],[channel],None,[256],[0,256])
        hist_can.append(histr)
    hist_grupo.append(hist_can)
    
img = cv2.imread('75856_1710710972597_3713371_n.jpg', -1)

suma=cv2.add(img,img2)
img=suma

###
cont=0
for i in files:
    if cont==0:
        img = cv2.imread(i, -1)
        cont+=1
    else:
        try:
            cont+=1
            prop1=(cont-1)/cont
            prop2=1-prop1
            img=cv2.addWeighted(img,prop1,cv2.imread(i, -1),prop2,0)
            
        except:
            pass
        
        

color = ('b','g','r')
hist_can=list()
for channel,col in enumerate(color):
    histr = cv2.calcHist([img],[channel],None,[10],[0,10])
    hist_can.append(histr)
    

    plt.plot(histr,color = col)
    plt.xlim([0,10])

plt.title('Histogram for color scale picture')
plt.show()

while True:
   k = cv2.waitKey(0) & 0xFF     
   if k == 27: break             # ESC key to exit 
cv2.destroyAllWindows()

classifier = svm.SVC(probability=True, kernel='linear')
classifier.fit(X_train, y_train) 

###pruebo PCA

pca = PCA(.3)
pca.fit(X_train)


pca.n_components_

X_train_pca = pca.transform(X_train)
X_test_pca = pca.transform(X_test)

classifier = RandomForestClassifier(n_estimators=500, max_depth= 80)  
classifier.fit(X_train_pca, y_train) 

df_edges=pd.DataFrame(df)
df_edges2=df_edges.iloc[:,0:1024]

df3=df.iloc[0:3998,:]

df4=pd.concat([df_edges2, df3], axis=1)

df_tot=pd.concat([df_edges, df_h1d, df_h3d], axis=1)


def variance_of_laplacian(image):
    img = cv2.imread(image, -1)
	# compute the Laplacian of the image and then return the focus
	# measure, which is simply the variance of the Laplacian
    return cv2.Laplacian(img, 2,3).var()


variance_of_laplacian('1012846_207340579422545_1570121637_n.jpg')

from sklearn.model_selection import cross_val_score

scores = cross_val_score(classifier, df4.iloc[:,:-1], df4.iloc[:,-1], cv=10, scoring='roc_auc')
scores2 = cross_val_score(classifier, df5.iloc[:,:-1], df5.iloc[:,-1], cv=10, scoring='roc_auc')

scores.mean()

X_train, X_test, y_train, y_test = train_test_split(tot, target, test_size=0.2)  

###random forest
classifier = RandomForestClassifier(n_estimators=2500, max_depth= 120)  
classifier.fit(X_train, y_train) 

y_pred = classifier.predict_proba(X_test)
fpr, tpr, thresholds = metrics.roc_curve(y_test, y_pred[:,1])
metrics.auc(fpr, tpr)

df_tot=pd.concat([df_h1ds,df_h3ds, df_edgess], axis=1)

scores3 = cross_val_score(classifier, tot, target, cv=5, scoring='roc_auc')

auc=list()
cont=0
while cont<2:
    X_train, X_test, y_train, y_test = train_test_split(df_tot, target, test_size=0.2)  
    X_train1d, X_test1d=X_train.iloc[:,0:1170], X_test.iloc[:,0:1170]
    X_train3d, X_test3d=X_train.iloc[:,1170:1874], X_test.iloc[:,1170:1874]
    X_trainedg, X_testedg=X_train.iloc[:,1874:], X_test.iloc[:,1874:]
    
    classifier= RandomForestClassifier(n_estimators=300, max_depth= 15)  
    classifier.fit(X_train, y_train)
    
    y_pred = classifier.predict_proba(X_test)
    fpr, tpr, thresholds = metrics.roc_curve(y_test, y_pred[:,1])
    auc.append( metrics.auc(fpr, tpr))
    
    
    classifier.fit(X_train1d, y_train)
    y_pred1 = classifier.predict_proba(X_test1d)
    
    classifier.fit(X_train3d, y_train)
    y_pred2 = classifier.predict_proba(X_test3d)
    
    classifier.fit(X_trainedg, y_train)
    y_pred3 = classifier.predict_proba(X_testedg)
    
    avg=(y_pred1[:,1]+y_pred2[:,1]+y_pred3[:,1])/3
    
    fpr, tpr, thresholds = metrics.roc_curve(y_test, avg)
    auc.append( metrics.auc(fpr, tpr))
    
    cont+=1
    
    
auc1=list()
auc2=list()
cont=1    
for i in auc:
    if cont % 2!= 0:
        auc1.append(i)
    else:
        auc2.append(i)
    cont+=1
        
sum(scores)/10
sum(scores2)/12


import random

###genero series para separar en train y test
train=random.sample(range(0,4063), 3200)
test=[x for x in range(0,4063) if x not in train]

###organizo df x zona de imagen
df_sup=pd.concat([df_h1ds,df_h3ds, df_edgess], axis=1) ###sup
df_inf=pd.concat([df_h1di,df_h3di, df_edgesi], axis=1) ###inf
df_cent=pd.concat([df_h1dc,df_h3dc, df_edgesc], axis=1) ###cent
df_tod=pd.concat([df_h1dt,df_h3dt, df_edgest], axis=1) ###imagen_tod
###todo el dataset a lo bruto
tot=pd.concat([df_h1ds,df_h3ds, df_edgess,df_h1di,df_h3di, df_edgesi, df_h1dc,df_h3dc, df_edgesc,df_h1dt,df_h3dt, df_edgest,], axis=1)

auc_lr=list()
auc=list()
tot_auc=list()
cont=0

classifier= RandomForestClassifier(n_estimators=2500, max_depth=120 )

while cont<15:
    
    ###genero series para separar en train y test
    train=random.sample(range(0,4062), 3800)
    test=[x for x in range(0,4062) if x not in train]

    
    df_sup_train,df_sup_test = df_sup.iloc[train,:], df_sup.iloc[test,:]
    df_inf_train,df_inf_test = df_inf.iloc[train,:], df_inf.iloc[test,:]
    df_cent_train,df_cent_test = df_cent.iloc[train,:], df_cent.iloc[test,:]
    df_tod_train,df_tod_test = df_tod.iloc[train,:], df_tod.iloc[test,:] 
    tot_train,tot_test = tot.iloc[train,:], tot.iloc[test,:]
    
    
    y_train, y_test = target.iloc[train],target.iloc[test]
    
    classifier.fit(tot_train, y_train)
    y_pred0 = classifier.predict_proba(tot_test)
    
    
    classifier.fit(df_sup_train, y_train)
    y_pred = classifier.predict_proba(df_sup_test)
    
    classifier.fit(df_inf_train, y_train)
    y_pred1 = classifier.predict_proba(df_inf_test)
    
    classifier.fit(df_cent_train, y_train)
    y_pred2 = classifier.predict_proba(df_inf_test)
    
    classifier.fit(df_tod_train, y_train)
    y_pred3 = classifier.predict_proba(df_tod_test)
    
    avg=(0.52*y_pred[:,1]+0.65*y_pred1[:,1]-0.02*y_pred2[:,1]+0.97*y_pred3[:,1]-0.53)
    avg2=(y_pred[:,1]+y_pred1[:,1]+y_pred2[:,1]+y_pred3[:,1])/4
    
    fpr, tpr, thresholds = metrics.roc_curve(y_test, avg)
    auc_lr.append(metrics.auc(fpr, tpr))
    print('auc_lr: '+str(metrics.auc(fpr, tpr)))
    
    fpr, tpr, thresholds = metrics.roc_curve(y_test, avg2)
    auc.append(metrics.auc(fpr, tpr))
    print('auc: '+str(metrics.auc(fpr, tpr)))
    
    fpr, tpr, thresholds = metrics.roc_curve(y_test, y_pred0[:,1])
    tot_auc.append(metrics.auc(fpr, tpr))
    print('tot_auc: '+str(metrics.auc(fpr, tpr)))
    
    cont+=1
    
sum(auc)/15
sum(auc_lr)/15
sum(tot_auc)/15

    
    
    
    
    
    
    
    
    
    
    
    
