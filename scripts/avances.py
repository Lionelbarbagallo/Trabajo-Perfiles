# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 10:58:11 2019

@author: lione
"""
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


def est_1d(img, vec):
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
        
def est_3d(img, vec):
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
            
def histdesc_fft(file, vec):

    img = cv2.imread(file, 0)
    

    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)
    magnitude_spectrum = 2*np.log(np.abs(fshift))
    histr = cv2.calcHist([img],[0],None,[256],[0,256])
    
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
    vec.extend(histr.flatten())
    vec.extend([mean, std, p25,p50,p75])
    





vec=list()

h=list(histr)

est_3d(img, v)
h=list(histr.flatten())