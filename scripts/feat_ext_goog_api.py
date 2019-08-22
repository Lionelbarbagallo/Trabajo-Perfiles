# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 14:36:17 2019

@author: lione
"""
from google.cloud import vision
from google.cloud.vision import types
from PIL import Image, ImageDraw
import os
import io
from goog_api import detect_label, detect_obj ###en carpeta trabajo perfiles

###seteo la variable global con la KEY de la API de Google
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = str('C:\\Users\\lione\\Imagenes-5cc20b0b7936.json')


###Levanto labels para Perfiles de Ciudadanía Italiana

files=os.listdir('C:\\Users\\lione\\Dropbox\\Perfiles_Ciudadania_Italiana_Caba')###genero lista de archivos

labels=list()

cont=1

for i in files:
    labels.append([cont, i, detect_label('C:\\Users\\lione\\Dropbox\\Perfiles_Ciudadania_Italiana_Caba\\'+i)])  
    if cont%1000==0:
        archivo='C:\\Users\\lione\\Dropbox\\Trabajo_perfiles\\caba_lab'+str(cont)+'.txt'
        with open(archivo, 'w') as f:
            for item in labels:
                f.write("%s\n" % item)                
        labels=list()
        cont+=1
    elif cont==len(files):
        archivo='C:\\Users\\lione\\Dropbox\\Trabajo_perfiles\\caba_lab'+str(cont)+'.txt'
        with open(archivo, 'w') as f:
            for item in labels:
                f.write("%s\n" % item) 
    else:    
        cont+=1
        
###Levanto labels para Perfiles de Merca Libre Villa Fiorito

files=os.listdir('C:\\Users\\lione\\Dropbox\\Perfiles_Merca_Libre_Villa_Fiorito')###genero lista de archivos

labels=list()

cont=1

for i in files:
    labels.append([cont, i, detect_label('C:\\Users\\lione\\Dropbox\\Perfiles_Merca_Libre_Villa_Fiorito\\'+i)])  
    if cont%1000==0:
        archivo='C:\\Users\\lione\\Dropbox\\Trabajo_perfiles\\fiorito_lab'+str(cont)+'.txt'
        with open(archivo, 'w') as f:
            for item in labels:
                f.write("%s\n" % item)                
        labels=list()
        cont+=1
    elif cont==len(files):
        archivo='C:\\Users\\lione\\Dropbox\\Trabajo_perfiles\\fiorito_lab'+str(cont)+'.txt'
        with open(archivo, 'w') as f:
            for item in labels:
                f.write("%s\n" % item)
    else:    
        cont+=1
        
        
###Levanto objetos para Perfiles de Ciudadanía Italiana

files=os.listdir('C:\\Users\\lione\\Dropbox\\Perfiles_Ciudadania_Italiana_Caba')###genero lista de archivos

labels=list()


cont=1

for i in files:
    labels.append([cont, i, detect_obj('C:\\Users\\lione\\Dropbox\\Perfiles_Ciudadania_Italiana_Caba\\'+i)])  
    if cont%1000==0:
        archivo='C:\\Users\\lione\\Dropbox\\Trabajo_perfiles\\caba_obj'+str(cont)+'.txt'
        with open(archivo, 'w') as f:
            for item in labels:
                f.write("%s\n" % item)                
        labels=list()
        cont+=1
    elif cont==len(files):
        archivo='C:\\Users\\lione\\Dropbox\\Trabajo_perfiles\\caba_obj'+str(cont)+'.txt'
        with open(archivo, 'w') as f:
            for item in labels:
                f.write("%s\n" % item) 
    else:    
        cont+=1
        
###Levanto objetos para Perfiles de Villa Fiorito

files=os.listdir('C:\\Users\\lione\\Dropbox\\Perfiles_Merca_Libre_Villa_Fiorito')###genero lista de archivos

labels=list()


cont=1

for i in files:
    labels.append([cont, i, detect_obj('C:\\Users\\lione\\Dropbox\\Perfiles_Merca_Libre_Villa_Fiorito\\'+i)])  
    if cont%1000==0:
        archivo='C:\\Users\\lione\\Dropbox\\Trabajo_perfiles\\fiorito_obj'+str(cont)+'.txt'
        with open(archivo, 'w') as f:
            for item in labels:
                f.write("%s\n" % item)                
        labels=list()
        cont+=1
    elif cont==len(files):
        archivo='C:\\Users\\lione\\Dropbox\\Trabajo_perfiles\\fiorito_obj'+str(cont)+'.txt'
        with open(archivo, 'w') as f:
            for item in labels:
                f.write("%s\n" % item) 
    else:    
        cont+=1