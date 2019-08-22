# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 12:37:34 2019

@author: lione
"""

import pandas as pd

###proceso el DataFrame de Labels para Ciu_Ita_Caba

###levanto el archivo 
f = open('caba_lab.txt')
labels = []
for linea in f:
    labels.append(linea)
f.close()

labels=' '.join(labels) ###separo los registros correspondientes a cada imagen
labels=labels.split(']]\n ')
    
datasets=pd.DataFrame()

for i in labels: ###itearo sobre los registros para obtener la info relevante
    columnas=['Archivo']
    scores=[]
    
    try:
        data=i.split(', ')
        scores.append([data[1][1:-1]][0]) ###corresponde al nombre del archivo
    
    
        for x in data[3:]: ###los datos relevantes comienzan en la cuarta posición de la lista
            
            columnas.append((x.split('\n ')[1].split(': ')[1][1:-1])) ###Corresponde a la Label   

            scores.append(float(x.split('\n ')[2].split(': ')[1])) ###Corresponde al Score
        
        ###Genero DF para cada registro
        df=pd.DataFrame(scores) 
        df.index=columnas
        
        ###Mergeo el DF del Registro con el de todos los datos
        datasets=pd.merge(datasets, df, how='outer',right_index=True, left_index=True)

                       
    except:
        pass
    
###luego agregar target=1 y transponer!!!
###Guardar el archivo
###Hacer lo mismo para Fiorito
        

datasets=datasets.transpose()
datasets=datasets.iloc[:,1:]###elimino la primer columna que es un índice viejo
datasets=datasets.fillna(0)###reemplazo NA's con 0
###guardo el archivo
datasets.to_csv('caba_lab.csv', index=False) ###guardo el archivo

###abrir=pd.read_csv('caba_lab.csv', index_col='Archivo') Si voy a abrir, ya dejar marcada la columna 'Archivo' como índice