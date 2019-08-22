# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 12:32:51 2019

@author: lione
"""
import pandas as pd
import numpy as np

caba=pd.read_csv('caba_lab.csv', index_col='Archivo')
fio=pd.read_csv('fio_lab.csv', index_col='Archivo')
global_feat=pd.read_csv('global_feat.csv', index_col=0)


labs=pd.concat([caba, fio])
labs=labs.fillna(0)

pd.merge(global_feat, labs, left_index=True, right_index=True).to_csv('datos.csv', index=True)

Target=[1]*len(caba)
Target.extend([0]*len(fio))

###caba['Target']=1
###fio['Target']=0

items_caba=set(caba.columns)
items_fio=set(fio.columns)

cols=items_caba.intersection(items_fio)

df=pd.concat([caba.loc[:,cols], fio.loc[:,cols]])

df_total=pd.merge(df2, tot, left_index=True, right_index=True)
target=ds.target
ds=ds.drop(['target'], axis=1)



importances = classifier.feature_importances_
std = np.std([tree.feature_importances_ for tree in classifier.estimators_],
             axis=0)
indices = np.argsort(importances)[::-1]

features=df.columns

feat_imp=features[indices]

feat_imp2=pd.DataFrame(feat_imp)

df2=pd.concat([caba, fio])
df2=df2.fillna(0)
target=pd.DataFrame(target)

analisis=pd.DataFrame([y_test.index, y_test, y_pred[:,1]]).transpose()
analisis.to_csv('preds_test_mod.csv', index=False)



import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline
x = y_pred_pca_cuba[:,1]
plt.hist(x, normed=True, bins=30)
plt.ylabel('Probability');

###ploteo los 1
x=analisis.loc[analisis.iloc[:,1]==1,2]
plt.hist(list(x), normed=True, bins=20)
plt.ylabel('Probability');

###ploteo los 0
x=analisis.loc[analisis.iloc[:,1]==0,2]
plt.hist(list(x), normed=True, bins=20)
plt.ylabel('Probability');

###obtengo nombre de archivos 1 clasificados como 0
caba_mal=x=analisis.loc[(analisis.iloc[:,1]==1) &( analisis.iloc[:,2]<0.50),0]

###obtengo nombre de archivos 0 clasificados como 1
fio_mal=x=analisis.loc[(analisis.iloc[:,1]==0) &( analisis.iloc[:,2]>0.50),0]

fio_mal=list(fio_mal)

for i in fio_mal:
    shutil.copy(i, 'C:\\Users\\lione\\Dropbox\\Trabajo_Perfiles\\fio_mal')


caba_mal=list(caba_mal)

for i in caba_mal:
    shutil.copy(i, 'C:\\Users\\lione\\Dropbox\\Trabajo_Perfiles\\caba_mal')




def plot_roc_curve(fpr, tpr):
    plt.plot(fpr, tpr, color='orange', label='ROC')
    plt.plot([0, 1], [0, 1], color='darkblue', linestyle='--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic (ROC) Curve')
    plt.legend()
    plt.show()
    
"""
Ordenar todos los scripts. Básicamente, hay que organizar uno con lo que hace a la construcción del modelo,
y otro para procesar nuevos inputs. Tareas a realizar:
    
1)Crear carpeta para scripts de construcción del modelo t análisis de resultados. Allí irán:
    Relativos a Features:
    
    a-Script con TODAS las funciones accesorias que se importarán más adelante.
    
    b-Script utilizado para feat extract. Debe correr automáticamente, sin necesidad de cambiar los path, directorios, ni nada.
    b-Debe ofrecer DataFrames parciales para ser guardados, tanto para feat globales, como para locales.
    b-Armado DF final, incluye los merges, target, etc
    
    c-Script que corre un modelo básico, con CV, para reducir dimensionalidad.
    c-Feat selection en base a este modelo. Guardado de este DF
    d-Analizar var impo. Generar gráficos.
    c-Entrenamiento modelo final. Guardado del modelo para usar más adelante.
    
    d-Análisis de resultados. Odds Ratio de Labels.
    d-Análisis de matriz de confusión. Generar script para separar las imágenes mlas clasificadas. Guardar en carpeta aparte.
    d-Generar Histogramas y demás gráficos para analizar las probabilidades por clase, etc.
    
2)En otra carpeta. Script para procesar nuevos inputs. Debe extraer features para nuevas imágenes y clasificarlas (levantar el modelo ya entrenado).
    
A realizar:
    
3)Estudios de clusterin y distribución
4)Aplicar el modelo a nuevas poblaciones y probar test de medias
"""