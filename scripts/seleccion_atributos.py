# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 16:06:16 2019

@author: lione
"""
import pandas as pd
import random
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import seaborn as sns
import matplotlib.pyplot as plt


###cargo los datasets a utilizar. 
ciu=pd.read_csv('C:\\Users\\lione\\Dropbox\\Trabajo_perfiles\\datasets\\df_ciu.csv', index_col=0)
fio=pd.read_csv('C:\\Users\\lione\\Dropbox\\Trabajo_perfiles\\datasets\\df_fio.csv', index_col=0)

###voy a calcular las medias de cada atributo para cada clase. Luego busco si hay atributos que difieren según la clase
###por último, elimino aquellos que tienen una varianza muy alta (o son similares para ambas clases)

medias_ciu=ciu.iloc[:,:].mean(axis=0)
medias_fio=fio.iloc[:,:].mean(axis=0)

###calculo los SD
std_ciu=ciu.iloc[:,:].std(axis=0)
std_fio=fio.iloc[:,:].std(axis=0)

###calculo coef var
coef_var_ciu=std_ciu/medias_ciu
coef_var_fio=std_fio/medias_fio

coef_var_ciu=coef_var_ciu.sort_values()
coef_var_fio=coef_var_fio.sort_values()

###me voy a quedar con los features que no tengan una varianza muy elevada. Selecciono de cada clase todos los features con un CV<10
feat_ciu=set(coef_var_ciu.loc[coef_var_ciu<10].index)
feat_fio=set(coef_var_fio.loc[coef_var_fio<10].index)
feat=list(feat_ciu.union(feat_fio))

###calculo los ratios entre los features que fueron pre seleccionados
ratio=medias_ciu.loc[feat]/medias_fio.loc[feat]

ratio=ratio.loc[(ratio<0.5)|(ratio>2)]###me quedo con los features que impliquen un ODD ratio mayor a 2 para en cualquier dirección

feat_sel=list(ratio.index)###genero una lista para filtrar luego los datasets

###visulizo las ODD ratios. Por ahora me quedo sólo con las labels de la API de Google

serie_viz=pd.Series(ratio)

serie_viz.loc[serie_viz<1]=-1/serie_viz.loc[serie_viz<1]

serie_viz_idx=[x for x in serie_viz.index if 'df_' not in x]

serie_viz=serie_viz.loc[serie_viz_idx]

serie_viz=serie_viz.sort_values(ascending=True)

###hacer un buen gráfico!!!
###estas librerías son una porongaaaaaaaaaaaaaaaa
sns.set(style="whitegrid")

f, ax = figsize=(18, 45)

sns.set_color_codes("pastel")
sns.barplot(x=pd.DataFrame(serie_viz).iloc[:,0], y=serie_viz.index, data=pd.DataFrame(serie_viz),
            label="Total", color="b")
sns.set(font_scale=2)

# Add a legend and informative axis label
ax.axes.set_title("ODD ratio desagregados por atributos",fontsize=50)
ax.legend(ncol=2, loc="lower right", frameon=True)
ax.set(ylabel="Atributos",
       xlabel="ODD ratio de que una imagen de perfil pertenezca al grupo socioeconómico alto de acuerdo a sus atributos")


ax.savefig('lio.png')

###guardo los nuevos datasets en base al recorte de features propuesto
ciu.loc[:,feat_sel].to_csv('C:\\Users\\lione\\Dropbox\\Trabajo_perfiles\\datasets\\df_reducido_ciu.csv')
fio.loc[:,feat_sel].to_csv('C:\\Users\\lione\\Dropbox\\Trabajo_perfiles\\datasets\\df_reducido_fio.csv')







