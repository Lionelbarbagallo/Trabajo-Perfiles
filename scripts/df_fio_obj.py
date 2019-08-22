# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 16:14:26 2019

@author: lione
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 14:20:15 2019

@author: lione
"""

import pandas as pd

###proceso el DataFrame de Labels para Ciu_Ita_Caba

###levanto el archivo 
f = open('fio_obj.txt')
obj = []
for linea in f:
    obj.append(linea)
f.close()

obj=' '.join(obj) ###separo los registros correspondientes a cada imagen
obj=obj.split(']]\n ')
    
###labels=labels[0:10]

datasets=pd.DataFrame()
for i in obj:

    items=dict()
    
    try:
        data=i.split(', ')
        items['Archivo']=[data[1][1:-1]][0]###nombre del archivo, hasta aquí idem
    
    
        for x in data[2:]:###creo que sigue parecido
            
            item=x.split('\n ')[1].split(': ')[1][1:-1]
           
            try:
                items[item]+=1
            except:
                items[item]=1
        
        items=pd.DataFrame.from_dict(items, orient='index')
        datasets=pd.merge(datasets, items, how='outer',right_index=True, left_index=True)
                  
    except:
        pass
   
datasets=datasets.transpose()
datasets=datasets.iloc[:,1:]###elimino la primer columna que es un índice viejo
datasets=datasets.fillna(0)###reemplazo NA's con 0
###guardo el archivo
datasets.to_csv('fio_obj.csv', index=False)    

###abrir=pd.read_csv('fio_obj.csv', index_col='Archivo') Si voy a abrir, ya dejar marcada la columna 'Archivo' como índice
