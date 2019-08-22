# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 13:40:18 2019

@author: lione
"""

from google.cloud import vision
from google.cloud.vision import types
import io
import os
from PIL import Image, ImageDraw
import cv2
import numpy as np
import pandas as pd
import random

def label_list(cols):
    f = open(cols)
    l_cols = []
    for linea in f:
        l_cols.append(linea[:-1])
    f.close()
    return(l_cols)
    

###función que se conecta a la API de Google para recuperar Labels

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = str('C:\\Users\\lione\\Imagenes-5cc20b0b7936.json')###seteo path a credencial de la API

client = vision.ImageAnnotatorClient()###instancio el cliente. No se puede hacer dentro de la función porque existe un Rate Limit

def detect_label(img):

    global client

    with io.open(img, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)
    

    response = client.label_detection(image=image)
    labels = response.label_annotations
            
    return([response, labels])
    
###comienzan funciones de extrancción de atributos globales!!! 
    
###genera el histograma de colores para cada canal
def hist1d(img, bins, vec): ###imagen, cantidad de bins para el hist, vector al cual agregar valores
    color = ('b','g','r')
    hist_can=list()
    for channel,col in enumerate(color):
        histr = cv2.calcHist([img],[channel],None,[bins],[0,256])
        hist_can.extend([int(x) for x in histr])

    vec.extend(hist_can)


###genera histograma en 3d
def hist3d(img, bins, vec): ###imagen, cantidad de bins para el hist, vector al cual agregar valores


    hist=cv2.calcHist([img], [0, 1, 2], None,	bins, [0, 256, 0, 256, 0, 256])
    hist=hist.flatten()
    vec.extend(hist)
    
def edges(img, vec, umbral1, umbral2):
        edges = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        edges = cv2.Laplacian(edges,2, 3)
      
        ###edges[edges<50]=0
        edges=cv2.calcHist([edges],[0],None,[256],[0,256])
        edges=list(edges.flatten())
        px_e=sum(edges[umbral1:])
        px_e_f=sum(edges[umbral2:])
        try:
            ppf=px_e_f/px_e
            ppf=ppf*100
            ppf=int(ppf)
        except:
            ppf=0
        vec.append(px_e)
        vec.append(px_e_f)
        vec.append(ppf)
        vec.extend(edges)

###genera estadísticos descriptivos para el histograma en 1d
def est_1d(img, vec): ###no utilizada!
    color = ('b','g','r')
    for channel,col in enumerate(color):
        histr = cv2.calcHist([img],[channel],None,[256],[0,256])
    
        ls=list()
        pos=0
        for i in list(histr.flatten()):
            ls.extend([pos]*int(i))
            pos+=1
        array=np.array(ls)    
        mean=array.mean()
        std=array.std()
        p25=np.percentile(array, 25)
        p50=np.percentile(array, 50)
        p75=np.percentile(array, 75)
        vec.extend([mean, std, p25,p50,p75])
        
###genera estadísticos descriptivos para el histograma en 3d        
def est_3d(img, vec): ###no utilizada! 
        histr = cv2.calcHist([img],[0, 1, 2],None,[8,8,8],[0,256, 0,256, 0,256])
        
        for i in list(histr):
            ls=list()
            pos=0
        
            for x in i.flatten():
                ls.extend([pos]*int(x))
                pos+=1
            array=np.array(ls)    
            try:    
                mean=array.mean()
                std=array.std()
                p25=np.percentile(array, 25)
                p50=np.percentile(array, 50)
                p75=np.percentile(array, 75)
            except:
                mean, std, p25, p50, p75= [0,0,0,0,0]
            vec.extend([mean, std, p25,p50,p75])
            
#########funciones para construir los datasets de las muestras, no los de entrenamiento!!!######
###Extraigo los Global_Feat de las nuevas muestras y genero un archivo de salida

def glob_feat(path, salida):###toma dos parámetros, el path a la carpeta que contiene las impagenes, y el path+nombre de archivo de la salida
###path debe ir sin los \\
###salida debe incruir la extensión. csv
###todo debe ir como string
    archivo=list()

    ###genero df por tipo de feature - a su interior pueden seguir segmentandose x total/sup/inf/cent

    ###bins
    ###imagen total
    bins1dt=256
    bins3dt=[8,8,8]
    binsedt=250

    ###imagen segmentos
    bins1ds=80
    bins3ds=[6,6,6]
    binseds=250



    df_h1dt=list()
    df_h1ds=list()
    df_h1di=list()
    df_h1dc=list()

    df_h3dt=list()
    df_h3ds=list()
    df_h3di=list()
    df_h3dc=list()

    df_edgest=list()
    df_edgess=list()
    df_edgesi=list()
    df_edgesc=list()

    files=os.listdir(path)

    for i in files:
        try: 
            archivo.append(i)
            img = Image.open(path+'\\'+i)
            img = img.resize((74,74), Image.ANTIALIAS)
            img=np.array(img)
            sup = img[0:10, 0:74]
            inf = img[64:74, 0:74]
            cent = img[22:58, 22:58]

    
    ###genero vectores para imagen total
        
            feat_vec_h1d=list()
            feat_vec_h3d=list()
            feat_vec_edges=list()  
        
        ###vector de histograma 1d
            hist1d(img, bins1dt, feat_vec_h1d)

    
        ###vector de histograma 3d

            hist3d(img, bins3dt, feat_vec_h3d)

    
        ###vector de edges
            edges(img, feat_vec_edges, 40, 90)
          
            df_h1dt.append(feat_vec_h1d)
            df_h3dt.append(feat_vec_h3d)
            df_edgest.append(feat_vec_edges)
        
        ###genero vectores para superior
        
            feat_vec_h1d=list()
            feat_vec_h3d=list()
            feat_vec_edges=list() 
            
        ###vector de histograma 1d
            hist1d(sup, bins1ds, feat_vec_h1d)

    
        ###vector de histograma 3d
    
            hist3d(sup, bins3dt, feat_vec_h3d)
    
        ###vector de edges
            edges(sup, feat_vec_edges, 40, 90)
           
            df_h1ds.append(feat_vec_h1d)
            df_h3ds.append(feat_vec_h3d)
            df_edgess.append(feat_vec_edges)
        
        ###genero vectores para inferior
        
            feat_vec_h1d=list()
            feat_vec_h3d=list()
            feat_vec_edges=list() 
            
        ###vector de histograma 1d
            hist1d(inf, bins1ds, feat_vec_h1d)

    
        ###vector de histograma 3d
    
            hist3d(inf, bins3dt, feat_vec_h3d)
    
        ###vector de edges
            edges(inf, feat_vec_edges, 40, 90)
        
            df_h1di.append(feat_vec_h1d)
            df_h3di.append(feat_vec_h3d)
            df_edgesi.append(feat_vec_edges)
        
        ###genero vectores para centro
        
            feat_vec_h1d=list()
            feat_vec_h3d=list()
            feat_vec_edges=list()             
            
        ###vector de histograma 1d
    
            hist1d(cent, bins1ds, feat_vec_h1d)

    
        ###vector de histograma 3d
    
            hist3d(cent, bins3dt, feat_vec_h3d)
    
        ###vector de edges
            edges(cent, feat_vec_edges, 40, 90)
    
            df_h1dc.append(feat_vec_h1d)
            df_h3dc.append(feat_vec_h3d)
            df_edgesc.append(feat_vec_edges)
        
        
        except:
            pass
    
    ###armo data set´s

    df_h1dt=pd.DataFrame(df_h1dt)
    n_cols=df_h1dt.shape[1]
    labels=['df_h1dt'+str(x) for x in list(range(0,n_cols))]
    df_h1dt.columns=labels

    df_h1ds=pd.DataFrame(df_h1ds)
    n_cols=df_h1ds.shape[1]
    labels=['df_h1ds'+str(x) for x in list(range(0,n_cols))]
    df_h1ds.columns=labels

    df_h1di=pd.DataFrame(df_h1di)
    n_cols=df_h1di.shape[1]
    labels=['df_h1di'+str(x) for x in list(range(0,n_cols))]
    df_h1di.columns=labels

    df_h1dc=pd.DataFrame(df_h1dc)
    n_cols=df_h1dc.shape[1]
    labels=['df_h1dc'+str(x) for x in list(range(0,n_cols))]
    df_h1dc.columns=labels

    df_h3dt=pd.DataFrame(df_h3dt)
    n_cols=df_h3dt.shape[1]
    labels=['df_h3dt'+str(x) for x in list(range(0,n_cols))]
    df_h3dt.columns=labels
    
    df_h3ds=pd.DataFrame(df_h3ds)
    n_cols=df_h3ds.shape[1]
    labels=['df_h3ds'+str(x) for x in list(range(0,n_cols))]
    df_h3ds.columns=labels

    df_h3di=pd.DataFrame(df_h3di)
    n_cols=df_h3di.shape[1]
    labels=['df_h3di'+str(x) for x in list(range(0,n_cols))]
    df_h3di.columns=labels

    df_h3dc=pd.DataFrame(df_h3dc)
    n_cols=df_h3dc.shape[1]
    labels=['df_h3dc'+str(x) for x in list(range(0,n_cols))]
    df_h3dc.columns=labels

    df_edgest=pd.DataFrame(df_edgest)
    n_cols=df_edgest.shape[1]
    labels=['df_edgest'+str(x) for x in list(range(0,n_cols))]
    df_edgest.columns=labels

    df_edgess=pd.DataFrame(df_edgess)
    n_cols=df_edgess.shape[1]
    labels=['df_edgess'+str(x) for x in list(range(0,n_cols))]
    df_edgess.columns=labels


    df_edgesi=pd.DataFrame(df_edgesi)
    n_cols=df_edgesi.shape[1]
    labels=['df_edgesi'+str(x) for x in list(range(0,n_cols))]
    df_edgesi.columns=labels

    df_edgesc=pd.DataFrame(df_edgesc)
    n_cols=df_edgesc.shape[1]
    labels=['df_edgesc'+str(x) for x in list(range(0,n_cols))]
    df_edgesc.columns=labels




    ###paso todo a un DF 

    tot=pd.concat([df_h1ds,df_h3ds, df_edgess,df_h1di,df_h3di, df_edgesi, df_h1dc,df_h3dc, df_edgesc,df_h1dt,df_h3dt, df_edgest,], axis=1)

    tot.index=archivo

    tot.to_csv(salida)
    
###función que obtiene las labels para las imágenes

def get_labels(path, path_salida, salida):###toma tres parámetros, el path a la carpeta que contiene las impagenes, el path a la carpeta donde quiere guardarse la salida, y el nombre del archivo de salida
###el path no debe llevar las \\
###path_salida tampoco debe llevar \\\
###salida es solo un nombre indicativo, conviene que refiera al conjunto de imágenes. NO DEBE INCLUIR LA EXTENSIÓN DE LA SALIDA!!!    
###la salida debe realizarse en una carpeta separada, que luego será levantada por otra función
    
    files=os.listdir(path)###genero lista de archivos

    labels=list()

    cont=1

    for i in files:
        labels.append([cont, i, detect_label(path+'\\'+i)])  
        if cont%1000==0:
            archivo=path_salida+'\\'+salida+str(cont)+'.txt'
            with open(archivo, 'w') as f:
                for item in labels:
                    f.write("%s\n" % item)                
            labels=list()
            cont+=1
        elif cont==len(files):
            archivo=path_salida+'\\'+salida+str(cont)+'.txt'
            with open(archivo, 'w') as f:
                for item in labels:
                    f.write("%s\n" % item) 
        else:    
            cont+=1
            
            
###función que construye un dataframe a partir der archivo de labels anterior
def df_labels(path_labels, salida):
###el parámetro path labels es un string, que indica el path a la carpeta que contiene los archivos .txt con las etiquetas antes generadas    
###path_labels debe introducirse sin las \\ finales
###salida es un string que debe indicar el path de salida, el nombre del archivo y la extensión del mismo.
    ###print(salida)###
    files=os.listdir(path_labels)
    labels = list()
    
    for i in files:
        f = open(path_labels+'\\'+i)
    
        for linea in f:
            ###print(linea)
            labels.append(linea)
        f.close()

    labels=' '.join(labels) ###separo los registros correspondientes a cada imagen
    labels=labels.split(']]\n ')
    ###print(labels)
    datasets=pd.DataFrame()

    for i in labels: ###itearo sobre los registros para obtener la info relevante
        columnas=['Archivo']
        scores=[]
    
        try:
            data=i.split(', ')
            ###print(data)
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

    datasets=datasets.transpose()
    datasets=datasets.iloc[:,1:]###elimino la primer columna que es un índice viejo
    datasets=datasets.fillna(0)###reemplazo NA's con 0
    ###guardo el archivo
    datasets.to_csv(salida, index=False)


###de aquí en adelante no fue testeado###
###revisar documentación de lo que sigue###

###función que mergea todos los archivos previos en un dataset final (sobre el que luego se aplicará la selección de atributos y bootstraping)    
def completo_ds(cols, file, file2, salida):###primer parámetro es el .csv con labels, el segundo con los global feat, el tercero el nombre del .csv de salida
###cols es el path + el nombre del archivo con las columnas utilizadas en el modelo entrenado (el dataset que estamos armando debe coincidir en las columnas con el que fue usado para entrenar)
###file es el path + el nombre del .csv con labels
###file2 es el path + el nombre del .csv con global_feat
###salida es el path + el nombre y extensión del archivo de salida
    l_cols=label_list(cols)


    ds_lab=pd.read_csv(file, index_col='Archivo')
    ds_lab_cols=set(ds_lab.columns)###genero set de columnas en dataset nuevo
    cols_mod=set(l_cols)###genero dataset de columnas en el modelo. Están en archivo cols_lab.txt

    crear=cols_mod.difference(ds_lab_cols)###genero set de columnas a crear en nuevos datos
    sacar=ds_lab_cols.difference(cols_mod)
    
    ds_lab=ds_lab.drop(columns=[x for x in sacar])
    
    for x in crear:
        ds_lab[x]=0
        
    ds_glob=pd.read_csv(file2, index_col=0)
    pd.merge(ds_glob, ds_lab.loc[:,l_cols], left_index=True, right_index=True).to_csv(salida)
            
def bootstrap(n_muestra, cant_muestras, df):
    
    boot=list()
    while len(boot)<cant_muestras:
        filas=list(np.random.randint(0,len(df),n_muestra))
        muestra=df.iloc[filas,:].mean(axis=0)
        boot.append(muestra)
        
    return(pd.DataFrame(boot))
    
def bootstrap_train_test(n_muestra, cant_muestras, prop_train, df):
    
    filas_train=random.sample(range(len(df)),round(len(df)*prop_train))
    filas_test=[x for x in range(0, len(df)) if x not in filas_train]
    
    train=bootstrap(n_muestra, cant_muestras, df.iloc[filas_train,:])
    test=bootstrap(n_muestra, cant_muestras, df.iloc[filas_test,:])
    
    return([train, test])
    
    
    