# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 01:51:39 2019

@author: lione
"""

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, roc_curve, auc
from sklearn import metrics
from sklearn.model_selection import cross_val_score
import random


###división del data set y entrenamiento del modelo


X_train, X_test, y_train2, y_test2 = train_test_split(ds, target, test_size=0.2)  

###random forest
classifier = RandomForestClassifier(n_estimators=200, max_depth= 4)  
classifier.fit(X_train_pca, y_train)  

###AdaBoost -- Difícil de tunear, seguir con RF
classifier = GradientBoostingClassifier(n_estimators=500, max_depth= 7, learning_rate=0.2)  
classifier.fit(X_train, y_train)



###evaluación del modelo

###curva roc en train
y_pred = classifier.predict_proba(train.loc[:,['Youth', 'Leisure','Fun','Child', 'Vacation','Landscape','Summer','Travel','Water']])
fpr, tpr, thresholds = metrics.roc_curve(y_train, y_pred[:,1])
metrics.auc(fpr, tpr)

###curva roc en test
y_pred = classifier.predict_proba(carp_boot_pca)
fpr, tpr, thresholds = metrics.roc_curve(y_test, y_pred[:,1])
metrics.auc(fpr, tpr)


###matriz de confusión
y_pred = classifier.predict(X_test_pca)  
print(confusion_matrix(y_test,y_pred))  
print(classification_report(y_test,y_pred))  
print(accuracy_score(y_test, y_pred))  


###esto sirve para hacer CV
scores2 = cross_val_score(classifier, df_total.iloc[:,index], target, cv=5, scoring='roc_auc')

###Lo que sigue hace CV con particiones Random, y compara diferentes modelos para la misma partición

###guardo el modelo
from sklearn.externals import joblib
filename = 'finalized_model.sav'
joblib.dump(classifier, filename)

loaded_model = joblib.load(filename)

###organizo df x zona de imagen --Estos son los nombres de los DF como los organiza el script feat_ext_total.py

df_sup=pd.concat([df_h1ds,df_h3ds, df_edgess], axis=1) ###sup
df_inf=pd.concat([df_h1di,df_h3di, df_edgesi], axis=1) ###inf
df_cent=pd.concat([df_h1dc,df_h3dc, df_edgesc], axis=1) ###cent
df_tod=pd.concat([df_h1dt,df_h3dt, df_edgest], axis=1) ###imagen_tod
###todo el dataset a lo bruto
tot=pd.concat([df_h1ds,df_h3ds, df_edgess,df_h1di,df_h3di, df_edgesi, df_h1dc,df_h3dc, df_edgesc,df_h1dt,df_h3dt, df_edgest,], axis=1)

###listas para guardar métricas x modelo
auc_lr=list()
auc=list()
tot_auc=list()
cont=0

###modelo a utilizar
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
    
    ###los coeficientes para el blend en avg salieron de una LR. Podrían volverse a calcular mejor
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

"""
Descriptivos de histogramas
Histogramas de 2d. Pensar si tienen sentido. Probar
Modelo de ensamble de features añadidos: feat_ext_edges y feat_ext_var_lap
feat_ext_var_lap no está terminado
Pensar cómo representar mejor los edges
Tiene sentido la var de Laplace?
Modelo lineal de ensamble
Edges ¿Cuantoa hay x imagen?Prop. de pisels que son edges. Definir umbral. Prop. de edges "definidos" sobre todos los edges, definir umbral.

###Algunos Insights:
-Pareciera que el árbol ya aprendió todo lo q puede aprender...no importa cómo represente los features
-Hay que agregar más features para mejorar el modelo.
-Lo único q se puede ajustar un poco es la cantidad de bins para edges
-Con más datos en CV el modelo dio mejor...ver si vale la pena sumar más observaciones.
-El modelo blended no está superando en performance RF sobre todo el Data Set a lo bruto...
-Clustering en imágenes...acá clasificamos entre dos grupos. Pero ¿Cuántos tipos de imágenes hay???? Escalar y PCA primero...
"""
scores.mean() ###tiene estadísticos 1d
scores2.mean() ###no los tiene
scores3.mean()
