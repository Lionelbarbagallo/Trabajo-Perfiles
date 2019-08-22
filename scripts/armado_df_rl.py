# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 23:41:33 2019

@author: lione
"""

from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

cuba1=X_train_pca[0:50,:].sum(axis=0)/50
cuba2=X_train_pca[50:100,:].sum(axis=0)/50
cuba3=X_train_pca[100:150,:].sum(axis=0)/50
cuba4=X_train_pca[150:200,:].sum(axis=0)/50
cuba5=X_train_pca[200:250,:].sum(axis=0)/50
cuba6=X_train_pca[250:300,:].sum(axis=0)/50
cuba7=X_train_pca[300:350,:].sum(axis=0)/50
cuba8=X_train_pca[350:400,:].sum(axis=0)/50
cuba9=X_train_pca[400:450,:].sum(axis=0)/50
cuba10=X_train_pca[450:500,:].sum(axis=0)/50

carp1=X_train_pca[4000:4050,:].sum(axis=0)/50
carp2=X_train_pca[4050:4100,:].sum(axis=0)/50
carp3=X_train_pca[4100:4150,:].sum(axis=0)/50
carp4=X_train_pca[4150:4200,:].sum(axis=0)/50
carp5=X_train_pca[4200:4250,:].sum(axis=0)/50
carp6=X_train_pca[4250:4300,:].sum(axis=0)/50
carp7=X_train_pca[4300:4350,:].sum(axis=0)/50
carp8=X_train_pca[4350:4400,:].sum(axis=0)/50
carp9=X_train_pca[4400:4450,:].sum(axis=0)/50
carp10=X_train_pca[4450:4500,:].sum(axis=0)/50

df_rl=pd.DataFrame([cuba1, cuba2, cuba3, cuba4,cuba5,cuba6,cuba7,cuba8,cuba9,cuba10, carp1, carp2, carp3, carp4,carp5,carp6,carp7,carp8,carp9,carp10])

y=[sum(y_train[0:50])/50, sum(y_train[50:100])/50, sum(y_train[100:150])/50, sum(y_train[150:200])/50, sum(y_train[200:250])/50, sum(y_train[250:300])/50, sum(y_train[300:350])/50, sum(y_train[350:400])/50, sum(y_train[400:450])/50, sum(target[450:500])/50, sum(y_train[4000:4050])/50, sum(y_train[4050:4100])/50, sum(y_train[4150:4200])/50, sum(target[4200:4250])/50, sum(y_train[4250:4300])/50, sum(y_train[4300:4350])/50, sum(y_train[4350:4400])/50, sum(y_train[4400:4450])/50,sum(y_train[4450:4500])/50,sum(y_train[4500:4550])/50]

y.extend([0]*10)

regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(X_train_pca, y_train)

coef=regr.coef_

y_pred = regr.predict(clase_neg_pca)

x=pca_df[1000:2000].sum(axis=0)/1000

df=list()
while len(df)<1000:
    filas=list(np.random.randint(0,3500,4))
    muestra=df_original.iloc[filas,:].sum(axis=0)/4
    df.append(muestra)
while len(df)<2000:
    filas=list(np.random.randint(4000,7100,4))
    muestra=df_original.iloc[filas,:].sum(axis=0)/4
    df.append(muestra)
    
df=pd.DataFrame(df)
y=[1]*1000
y.extend([0]*1000)

r2_score(y_test, y_pred) 

y_pred[y_pred<0.40]=0
y_pred[y_pred>0.40]=1
    


