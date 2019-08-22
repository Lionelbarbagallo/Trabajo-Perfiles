# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 17:28:46 2019

@author: lione
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 16:29:08 2019

@author: lione
"""

###Primero separo todo en train y test

X_train, X_test, y_train, y_test = train_test_split(df.iloc[:,:-1], df.iloc[:,-1], test_size=0.2)  

###Luego separo para entrenar modelos separados x segmento de la imagen

###Modelo con toda la imagen

X_train1, X_test1 = X_train.iloc[:,0:768], X_test.iloc[:,0:768]

###Modelo con la parte superior de la imagen

X_train2, X_test2 = X_train.iloc[:,768:1008], X_test.iloc[:,768:1008]

###Modelo con la parte inferior de la imagen

X_train3, X_test3 = X_train.iloc[:,1008:1248], X_test.iloc[:,1008:1248]

###Modelo con el centro de la imagen

X_train4, X_test4 = X_train.iloc[:,1248:], X_test.iloc[:,1248:]

###entreno modelos y genero prob. sobre test
classifier1 = RandomForestClassifier(n_estimators=200, max_depth= 15)  
classifier1.fit(X_train1, y_train) 
y_pred1 = classifier1.predict_proba(X_test1)

classifier2 = RandomForestClassifier(n_estimators=200, max_depth= 15)  
classifier2.fit(X_train2, y_train) 
y_pred2 = classifier2.predict_proba(X_test2)

classifier3 = RandomForestClassifier(n_estimators=200, max_depth= 15)  
classifier3.fit(X_train3, y_train) 
y_pred3 = classifier3.predict_proba(X_test3)

classifier4 = RandomForestClassifier(n_estimators=200, max_depth= 15)  
classifier4.fit(X_train4, y_train) 
y_pred4 = classifier4.predict_proba(X_test4)

###armo el df para evaluación (suma de probs. pred x distintos modelos)

df_ensamble=pd.DataFrame({'Column1':y_pred1[:,1],'Column2':y_pred2[:,1],'Column3':y_pred3[:,1],'Column4':y_pred4[:,1]})



###evaluo modelo 

fpr, tpr, thresholds = metrics.roc_curve(y_test, df_ensamble.sum(axis = 1)/4)
metrics.auc(fpr, tpr)