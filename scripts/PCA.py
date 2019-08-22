# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 13:48:40 2019

@author: lione
"""

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier

X_train, X_test, y_train, y_test = train_test_split(df, y, test_size=0.2)  


scaler = StandardScaler()


# Fit on training set only.
scaler.fit(X_train)

X_train_pca = scaler.transform(X_train)
X_test_pca = scaler.transform(X_test)

pca = PCA(n_components=10)

pca.fit(X_train_pca)

X_train_pca = pca.transform(X_train_pca)
X_test_pca = pca.transform(X_test_pca)


classifier = KNeighborsClassifier(n_neighbors=20)  
classifier.fit(X_train_pca, y_train) 

###curva roc en train
y_pred = classifier.predict_proba(X_train_pca)
fpr, tpr, thresholds = metrics.roc_curve(y_train, y_pred[:,1])
metrics.auc(fpr, tpr)

###curva roc en test
y_pred = classifier.predict_proba(X_test_pca)
fpr, tpr, thresholds = metrics.roc_curve(y_test, y_pred[:,1])
metrics.auc(fpr, tpr)

###transformo dataset Carp
pca_ds=scaler.transform(df_ds)
pca_ds=pca.transform(pca_ds)


pca_df=scaler.transform(df)
pca_df=pca.transform(pca_df)

ciu=pca_df[0:3000].sum(axis=0)
fio=pca_df[4000:].sum(axis=0)

dif2=pca_df[200:300].sum(axis=0)-pca_df[4100:4200].sum(axis=0)
dif3=ciu-fio
dif4=ciu-fio


cuba=pca_cuba.sum(axis=0)
carp=pca_carp.sum(axis=0)
ds=pca_ds.sum(axis=0)

dif=cuba-carp
dif1=pca_cuba[0:25,:].sum(axis=0)-pca_carp[0:25,:].sum(axis=0)
dif2=pca_cuba[25:50,:].sum(axis=0)-pca_carp[25:50,:].sum(axis=0)
dif3=pca_cuba[75:100,:].sum(axis=0)-pca_carp[75:100,:].sum(axis=0)
dif4=pca_cuba[100:125,:].sum(axis=0)-pca_carp[100:125,:].sum(axis=0)

dif=ds-carp


y_pred_pca_cuba2 = classifier.predict_proba(pca_cuba)


index=indices[0:200]