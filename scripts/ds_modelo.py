# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 19:54:47 2019

@author: lione
"""
from acc_func import glob_feat, get_labels, df_labels, completo_ds, bootstrap
import pandas as pd
import random

###defino los path a las carpetas que contienen las imágenes que serán usadas para la construcción de train y test del modelo
path_ciu_ita='C:\\Users\\lione\\Dropbox\\imagenes\\Perfiles_Ciudadania_Italiana_Caba'
path_fio='C:\\Users\\lione\\Dropbox\\imagenes\\Perfiles_Merca_Libre_Villa_Fiorito'

###genero archivos con global features

glob_feat(path_ciu_ita, 'C:\\Users\\lione\\Dropbox\\Trabajo_perfiles\\datasets\\ciu_glob.csv')
glob_feat(path_fio, 'C:\\Users\\lione\\Dropbox\\Trabajo_perfiles\\datasets\\fio_glob.csv')

###bajo las labels de la API de Google

get_labels(path_ciu_ita,'C:\\Users\\lione\\Dropbox\\Trabajo_perfiles\\ciu_lab', 'caba_lab')
get_labels(path_fio,'C:\\Users\\lione\\Dropbox\\Trabajo_perfiles\\fio_lab', 'fio_lab')

###genero el dataset con labels
df_labels('C:\\Users\\lione\\Dropbox\\Trabajo_perfiles\\ciu_lab', 'C:\\Users\\lione\\Dropbox\\Trabajo_perfiles\\datasets\\ciu_lab.csv')
df_labels('C:\\Users\\lione\\Dropbox\\Trabajo_perfiles\\fio_lab', 'C:\\Users\\lione\\Dropbox\\Trabajo_perfiles\\datasets\\fio_lab.csv')

###mergeo los datasets de global feat y labels, guardo los datasets, genero target
completo_ds('C:\\Users\\lione\\Dropbox\\Trabajo_perfiles\\cols_lab.txt', 'C:\\Users\\lione\\Dropbox\\Trabajo_perfiles\\datasets\\ciu_lab.csv', 'C:\\Users\\lione\\Dropbox\\Trabajo_perfiles\\datasets\\ciu_glob.csv', 'C:\\Users\\lione\\Dropbox\\Trabajo_perfiles\\datasets\\df_ciu.csv')
completo_ds('C:\\Users\\lione\\Dropbox\\Trabajo_perfiles\\cols_lab.txt', 'C:\\Users\\lione\\Dropbox\\Trabajo_perfiles\\datasets\\fio_lab.csv', 'C:\\Users\\lione\\Dropbox\\Trabajo_perfiles\\datasets\\fio_glob.csv', 'C:\\Users\\lione\\Dropbox\\Trabajo_perfiles\\datasets\\df_fio.csv')

###bootstrapeo y proceso los datasets para comenzar el proceso de análisis y construcción de modelos

###cargo data set de ciu_ita
ciu_ita=pd.read_csv('C:\\Users\\lione\\Dropbox\\Trabajo_perfiles\\datasets\\df_ciu.csv', index_col=0)
fio=pd.read_csv('C:\\Users\\lione\\Dropbox\\Trabajo_perfiles\\datasets\\df_fio.csv', index_col=0)

###prop. train y test, luego divido datasets
prop_train=0.8

filas_ciu_train=random.sample(range(len(ciu_ita)),round(len(ciu_ita)*prop_train))
filas_fio_train=random.sample(range(len(fio)),round(len(fio)*prop_train))

filas_ciu_test=[x for x in range(0, len(ciu_ita)) if x not in filas_ciu_train]
filas_fio_test=[x for x in range(0, len(fio)) if x not in filas_fio_train]

###genero datasets de train y test con bootstrapping, en este caso, con 1000 ejemplos por clase, cada muestra compuesta por 50 imágenes
train_ita=bootstrap(50, 1000, ciu_ita.iloc[filas_ciu_train,:])
train_fio=bootstrap(50, 1000, fio.iloc[filas_fio_train,:])

test_ita=bootstrap(50, 1000, ciu_ita.iloc[filas_ciu_test,:])
test_fio=bootstrap(50, 1000, fio.iloc[filas_fio_test,:])


train=pd.concat([train_ita, train_fio])    
test=pd.concat([test_ita, test_fio])  

###genero lista y columna de target
y_train=[1]*1000
y_train.extend([0]*1000)

y_test=[1]*1000
y_test.extend([0]*1000)

train['target']=y_train
test['target']=y_test

###guardo los data sets para train y test
train.to_csv('C:\\Users\\lione\\Dropbox\\Trabajo_perfiles\\datasets\\train.csv', index=False)
test.to_csv('C:\\Users\\lione\\Dropbox\\Trabajo_perfiles\\datasets\\test.csv', index=False)




