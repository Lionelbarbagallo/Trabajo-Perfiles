# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 12:30:12 2019

@author: lione
"""
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import make_classification
from sklearn.ensemble import ExtraTreesClassifier

###entreno un modelo con todas las variables
###separo train y test
X_train, X_test, y_train, y_test = train_test_split(tot, target, test_size=0.2)  


classifier = RandomForestClassifier(n_estimators=120, max_depth= 8)  
classifier.fit(X_train, y_train)  

###genero un nuevo DF solo con las 1000 Variables más relevantes
importances = classifier.feature_importances_
indices = np.argsort(importances)[::-1]

recorte=[x for x in indices[0:1000]]

df_filtrado=tot.iloc[:,recorte]


###sobre esta primera selección de variables, voy a volver a seleccionar. La idea es filtrar en
###una primera etapa a aquellas variables que no sirven siquiera para sobreajustar el modelo

###defino el modelo a utilizar
classifier = RandomForestClassifier(n_estimators=120, max_depth= 15)  

###cantidad de iteraciones
repeticiones=3

rep=0
ciclos=list()

while rep<repeticiones:
    
    ###para cada repetición, generará una nueva partición del dataset
    X_train, X_test, y_train, y_test = train_test_split(df_filtrado, target, test_size=0.2) 
    var_utilizadas=list(range(0, X_train.shape[1])) ###genero una lista con los indices de las varoables del dataset
    
    ciclo=dict()
    i=0
    
    ###para cada repetición, seguira generando submodelos hasta haber utilizado al menos una vez cada variable
    while len(var_utilizadas)>0:    
        var=random.sample(list(range(0,1000)), 20) ###para cada submodelo solo utilizo 20 variables elegidas aleatoreamente
        var_utilizadas=[x for x in var_utilizadas if x not in var] ###una vez que fueron utilizadas estas variables, las saco de la lista
        classifier.fit(X_train.iloc[:,var], y_train) 
    
        y_pred = classifier.predict_proba(X_train.iloc[:,var])
        fpr, tpr, thresholds = metrics.roc_curve(y_train, y_pred[:,1])
        train=metrics.auc(fpr, tpr) ###evalúo modelo en train


        y_pred = classifier.predict_proba(X_test.iloc[:,var])
        fpr, tpr, thresholds = metrics.roc_curve(y_test, y_pred[:,1])
        test=metrics.auc(fpr, tpr) ###evalúo modelo en test
    
        ciclo.update({str(i):{'Vars':var,'Auc_train':train,'Auc_test':test}}) ###guardo todos los datos del modelo, input de variables y AUC en train y test en un diccionario
        
        i+=1
        
        print(rep)
        print(i)
        print(train)
        print(test)

    ciclos.append(ciclo) ###guardo los diccionarios en una lista    
    rep+=1
    
###comienzo a sumarizar la información antes generada    
variables=dict() ###genero un diccionario donde se almacenara la información para cada variable

for c in ciclos: ###itero sobre cada ciclo previo
    for key in c.keys(): ###itero sobre cada sub modelo
        for var in c[key]['Vars']: ###itero sobre cada variable incluida en ese submodelo
            if str(var) in variables.keys(): ###busco esa variable en el diccionario de variables
                variables[str(var)]['Repeticiones']+=1 ###almaceno la data de la variable
                variables[str(var)]['Auc'].append(c[key]['Auc_test'])  
            else: ###si la variable no está en el diccionario la agrego
                variables.update({str(var):{'Repeticiones':1,'Auc':[c[key]['Auc_test']],'Av_Auc':0}})

###calculo el AUC medio de los modelos en los que se usa cada variable
auc=list()
for key in variables.keys():
    variables[key]['Av_Auc']=np.array(variables[key]['Auc']).mean()
    auc.append(np.array(variables[key]['Auc']).mean())
    
###genero histograma sencillo para una primera visualización
plt.hist(auc)
plt.title('Random Gaussian data (fixed bin size)')
plt.xlabel('variable X (bin size = 5)')
plt.ylabel('count')

plt.show()

###seleccionó las más explicativas

filtro=[int(x) for x in variables.keys() if variables[x]['Av_Auc']>0.6355]

###armo nuevo data set para entrenar modelos. Cuidado, usar el filtrado previamente "df_filtrado"

df_reducido=df_filtrado.iloc[:,filtro]
