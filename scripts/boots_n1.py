# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 18:41:06 2019

@author: lione
"""
import pandas as pd
from acc_func import bootstrap_train_test
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, roc_curve, auc
from sklearn import metrics



###cargo los datasets a utilizar. 
ciu=pd.read_csv('C:\\Users\\lione\\Dropbox\\Trabajo_perfiles\\datasets\\df_reducido_ciu.csv', index_col=0)
fio=pd.read_csv('C:\\Users\\lione\\Dropbox\\Trabajo_perfiles\\datasets\\df_reducido_fio.csv', index_col=0)

###genero datasets bootstrapeados con cantidad de muestras = 1 (es decir tomo el dataset como está)

###pasar todo esto a función accesoria!!!
###prop. train y test, luego divido datasets
###defino una función para iterar sobre muestras de distintos tamaños
def evalua_n_muestras(n):
    global ciu
    global fio
    train_ciu, test_ciu = bootstrap_train_test(n, 3500, 0.8, ciu)
    train_fio, test_fio = bootstrap_train_test(n, 3500, 0.8, fio)

    train=pd.concat([train_ciu, train_fio])    
    test=pd.concat([test_ciu, test_fio])  

    ###genero lista de target
    y_train=[1]*len(train_ciu)
    y_train.extend([0]*len(train_fio))

    y_test=[1]*len(test_ciu)
    y_test.extend([0]*len(test_fio))

    ###normalizo el datset y aplico PCA
    scaler = StandardScaler()
    scaler.fit(train)

    X_train_norm = scaler.transform(train)
    X_test_norm = scaler.transform(test)

    pca = PCA(n_components=10)

    pca.fit(X_train_norm)

    X_train_pca = pca.transform(X_train_norm)
    X_test_pca = pca.transform(X_test_norm)

    ###entreno un modelo básico y analizo resultados
    classifier = RandomForestClassifier(n_estimators=200, max_depth= 4)  
    classifier.fit(X_train_pca, y_train)

    ###curva roc en test
    y_pred = classifier.predict_proba(X_test_pca)
    fpr, tpr, thresholds = metrics.roc_curve(y_test, y_pred[:,1])
    
    return(metrics.auc(fpr, tpr))

roc=list()
for i in [1,2,3,4,5,10,20,50]:   
    roc.append(evalua_n_muestras(i))

###matriz de confusión
y_pred = classifier.predict(X_test_pca)  
print(confusion_matrix(y_test,y_pred))  
print(classification_report(y_test,y_pred))  
print(accuracy_score(y_test, y_pred))  



