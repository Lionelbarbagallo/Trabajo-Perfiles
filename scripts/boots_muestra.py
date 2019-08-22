# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 21:27:49 2019

@author: lione
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 20:25:11 2019

@author: lione
"""
import numpy as np
import pandas as pd


###genero dataset de carp
cuba_boot=list()
while len(cuba_boot)<50:
    filas=list(np.random.randint(0,465,50))
    muestra=cuba.iloc[filas,:].sum(axis=0)/50
    cuba_boot.append(muestra)
    
cuba_boot=pd.DataFrame(cuba_boot)

cuba=pd.read_csv('cuba.csv', index_col=0)




carp_cols=set(carp.columns)
mod_cols=set(cols)

dif=carp_cols.difference(mod_cols)
dif=list(dif)
