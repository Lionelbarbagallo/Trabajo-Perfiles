# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 13:28:40 2019

@author: lione
"""

import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
%matplotlib inline

###reduzco dimensionalidad del dataset original

scaler = StandardScaler()
scaler.fit(ds)

ds_estandarizado=scaler.transform(ds)###normalizo dataset

pca = PCA(n_components=100)###defino dimesionalidad

pca.fit(ds_estandarizado)###entreno PCA

ds_estandarizado_pca = pca.transform(ds_estandarizado)###transformo PCA

kmeans = KMeans(n_clusters=1) # You want cluster the passenger records into 2: Survived or Not survived
kmeans.fit(ds_estandarizado_pca)
iter1a=kmeans.inertia_

kmeans = KMeans(n_clusters=1) # You want cluster the passenger records into 2: Survived or Not survived
kmeans.fit(ds_estandarizado_pca)
iter1b=kmeans.inertia_

kmeans = KMeans(n_clusters=2) # You want cluster the passenger records into 2: Survived or Not survived
kmeans.fit(ds_estandarizado_pca)
iter2a=kmeans.inertia_

kmeans = KMeans(n_clusters=2) # You want cluster the passenger records into 2: Survived or Not survived
kmeans.fit(ds_estandarizado_pca)
iter2b=kmeans.inertia_

kmeans = KMeans(n_clusters=3) # You want cluster the passenger records into 2: Survived or Not survived
kmeans.fit(ds_estandarizado_pca)
iter3=kmeans.inertia_

kmeans = KMeans(n_clusters=3) # You want cluster the passenger records into 2: Survived or Not survived
kmeans.fit(ds_estandarizado_pca)
iter3b=kmeans.inertia_


kmeans = KMeans(n_clusters=4) # You want cluster the passenger records into 2: Survived or Not survived
kmeans.fit(ds_estandarizado_pca)
iter4a=kmeans.inertia_

kmeans = KMeans(n_clusters=4) # You want cluster the passenger records into 2: Survived or Not survived
kmeans.fit(ds_estandarizado_pca)
iter4b=kmeans.inertia_

kmeans = KMeans(n_clusters=5) # You want cluster the passenger records into 2: Survived or Not survived
kmeans.fit(ds_estandarizado_pca)
iter5a=kmeans.inertia_

kmeans = KMeans(n_clusters=5) # You want cluster the passenger records into 2: Survived or Not survived
kmeans.fit(ds_estandarizado_pca)
iter5b=kmeans.inertia_

kmeans = KMeans(n_clusters=6) # You want cluster the passenger records into 2: Survived or Not survived
kmeans.fit(ds_estandarizado_pca)
iter6a=kmeans.inertia_

kmeans = KMeans(n_clusters=6) # You want cluster the passenger records into 2: Survived or Not survived
kmeans.fit(ds_estandarizado_pca)
iter6b=kmeans.inertia_

kmeans = KMeans(n_clusters=7) # You want cluster the passenger records into 2: Survived or Not survived
kmeans.fit(ds_estandarizado_pca)
iter7a=kmeans.inertia_

kmeans = KMeans(n_clusters=7) # You want cluster the passenger records into 2: Survived or Not survived
kmeans.fit(ds_estandarizado_pca)
iter7b=kmeans.inertia_

kmeans = KMeans(n_clusters=8) # You want cluster the passenger records into 2: Survived or Not survived
kmeans.fit(ds_estandarizado_pca)
iter8a=kmeans.inertia_

kmeans = KMeans(n_clusters=8) # You want cluster the passenger records into 2: Survived or Not survived
kmeans.fit(ds_estandarizado_pca)
iter8b=kmeans.inertia_

kmeans = KMeans(n_clusters=9) # You want cluster the passenger records into 2: Survived or Not survived
kmeans.fit(ds_estandarizado_pca)
iter9a=kmeans.inertia_

kmeans = KMeans(n_clusters=9) # You want cluster the passenger records into 2: Survived or Not survived
kmeans.fit(ds_estandarizado_pca)
iter9b=kmeans.inertia_

kmeans = KMeans(n_clusters=10) # You want cluster the passenger records into 2: Survived or Not survived
kmeans.fit(ds_estandarizado_pca)
iter10a=kmeans.inertia_

kmeans = KMeans(n_clusters=10) # You want cluster the passenger records into 2: Survived or Not survived
kmeans.fit(ds_estandarizado_pca)
iter10b=kmeans.inertia_

kmeans = KMeans(n_clusters=11) # You want cluster the passenger records into 2: Survived or Not survived
kmeans.fit(ds_estandarizado_pca)
iter11a=kmeans.inertia_

kmeans = KMeans(n_clusters=11) # You want cluster the passenger records into 2: Survived or Not survived
kmeans.fit(ds_estandarizado_pca)
iter11b=kmeans.inertia_

lab=kmeans.labels_
pred=kmeans.transform(ds_estandarizado_pca)

clusters_clase=pd.DataFrame([lab, target])