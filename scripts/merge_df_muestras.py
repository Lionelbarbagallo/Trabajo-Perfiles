# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 19:07:23 2019

@author: lione
"""
import pandas as pd

f = open('cols_lab.txt')
cols = []
for linea in f:
    cols.append(linea[:-1])
f.close()

###cuidado ver la posición de los índices en cada .csv...depende de como se guardó!
def completo_ds(file, file2, salida):###primer parámetro es el .csv con labels, el segundo con los global feat, el tercero el nombre del .csv de salida
    global cols
    ds_lab=pd.read_csv(file, index_col='Archivo')
    ds_lab_cols=set(ds_lab.columns)###genero set de columnas en dataset nuevo
    cols_mod=set(cols)###genero dataset de columnas en el modelo. Están en archivo cols_lab.txt

    crear=cols_mod.difference(ds_lab_cols)###genero set de columnas a crear en nuevos datos
    sacar=ds_lab_cols.difference(cols_mod)
    
    ds_lab=ds_lab.drop(columns=[x for x in sacar])
    
    for x in crear:
        ds_lab[x]=0
        
    ds_glob=pd.read_csv(file2, index_col=0)
    pd.merge(ds_glob, ds_lab.loc[:,cols], left_index=True, right_index=True).to_csv(salida)
    
    
        

    

