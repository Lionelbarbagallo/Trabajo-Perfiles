# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 19:24:57 2019

@author: lione
"""

files=os.listdir()

###genero vectores para ciu_ita

df=list()
for i in files:
    
    img= cv2.imread(i, -1)
    sup = img[0:10, 0:74]
    inf = img[64:74, 0:74]
    cent = img[22:58, 22:58]
    feat_vec=list()

    hist=cv2.calcHist([img], [0, 1, 2], None,	[8, 8,8], [0, 256, 0, 256, 0, 256])
    
    hist=hist.flatten()
    feat_vec.extend(list(hist))
          
            
###histograma del borde superior
            
    hist=cv2.calcHist([sup], [0, 1, 2], None,	[6, 6,6], [0, 256, 0, 256, 0, 256])
    
    hist=hist.flatten()
    feat_vec.extend(list(hist))
            
###histograma del borde inferior
            
    hist=cv2.calcHist([inf], [0, 1, 2], None,	[6, 6,6], [0, 256, 0, 256, 0, 256])
    
    hist=hist.flatten()
    feat_vec.extend(list(hist))
            
###histograma del centro
                
    hist=cv2.calcHist([cent], [0, 1, 2], None,	[6, 6,6], [0, 256, 0, 256, 0, 256])
    
    hist=hist.flatten()
    feat_vec.extend(list(hist))
                        
    feat_vec.append(1)
            
    df.append(feat_vec)

    
###genero vectores para fiorito
    
###levanto los nombres para fiorito
    
files=os.listdir()

for i in files:
    
    img= cv2.imread(i, -1)
    sup = img[0:10, 0:74]
    inf = img[64:74, 0:74]
    cent = img[22:58, 22:58]
    feat_vec=list() 
    
    feat_vec=list()

    hist=cv2.calcHist([img], [0, 1, 2], None,	[8, 8,8], [0, 256, 0, 256, 0, 256])
    
    hist=hist.flatten()
    feat_vec.extend(list(hist))
          
            
###histograma del borde superior
            
    hist=cv2.calcHist([sup], [0, 1, 2], None,	[6, 6,6], [0, 256, 0, 256, 0, 256])
    
    hist=hist.flatten()
    feat_vec.extend(list(hist))
            
###histograma del borde inferior
            
    hist=cv2.calcHist([inf], [0, 1, 2], None,	[6, 6,6], [0, 256, 0, 256, 0, 256])
    
    hist=hist.flatten()
    feat_vec.extend(list(hist))
            
###histograma del centro
                
    hist=cv2.calcHist([cent], [0, 1, 2], None,	[6, 6,6], [0, 256, 0, 256, 0, 256])
    
    hist=hist.flatten()
    feat_vec.extend(list(hist))
                        
                
            
    feat_vec.append(0)
       
    df.append(feat_vec)

    
###armo data set
df=pd.DataFrame(df)
