# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 18:24:19 2019

@author: lione
"""
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

###analizo ODD Ratio

###calculo las medias
medias_clasepos=ds.iloc[0:3000,:].mean(axis=0)###emprolijar como se definen las filas
medias_claseneg=ds.iloc[4000:,:].mean(axis=0)

###calculo los SD
std_clasepos=ds.iloc[0:3000,:].std(axis=0)
std_claseneg=ds.iloc[4000:,:].std(axis=0)

###calculo coef var
coef_var_clasepos=std_clasepos/medias_clasepos
coef_var_claseneg=std_claseneg/medias_claseneg

coef_var_clasepos=coef_var_clasepos.sort_values()
coef_var_claseneg=coef_var_claseneg.sort_values()

###me voy a quedar con los features que no tengan una varianza muy elevada. Selecciono de cada clase todos los features con un CV<10
feat_pos=set(coef_var_clasepos.loc[coef_var_clasepos<10].index)
feat_neg=set(coef_var_claseneg.loc[coef_var_claseneg<10].index)
feat=list(feat_pos.union(feat_neg))

###calculo los ratios entre los features que fueron pre seleccionados
ratio=medias_clasepos.loc[feat]/medias_claseneg.loc[feat]

r=ratio.loc[(ratio<0.5)|(ratio>2)]

feat_sel=list(r.index)

###luego hago PCA para reducir la dimensionalidad

scaler = StandardScaler()


###normalizo las variables
scaler.fit(train.loc[:,feat_sel])

###genero datasets para construir y evaluar modelos
X_train_pca = scaler.transform(train.loc[:,feat_sel])
X_test_pca = scaler.transform(test.loc[:,feat_sel])

pca = PCA(n_components=10)


pca.fit(X_train_pca)###reduzco dimensionalidad


X_train_pca = pca.transform(X_train_pca)
X_test_pca = pca.transform(X_test_pca)

###genero datasets para evaluar performance sobre cada clase individual
clase_pos_pca=scaler.transform(ds_test_target.loc[:,feat_sel])
clase_neg_pca=scaler.transform(ds_test_neg.loc[:,feat_sel])

clase_pos_pca=pca.transform(clase_pos_pca)
clase_neg_pca=pca.transform(clase_neg_pca)

###funciona...pero da la impresión que sobreajusta a este dataset...probar reduciendo la cantidad de variables
###probar reducir a partir del análisis de la VAR IMP del modelo
###reducir al tun tun...
###hacer PCA
###probar si sirve algo del estilo coef var x ratio...luego ver si incluir la media
###probar todas las variantes...