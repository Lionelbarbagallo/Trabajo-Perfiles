# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 21:27:14 2019

@author: lione
"""
import matplotlib.pyplot as plt

def variance_of_laplacian(image):
    img = cv2.imread(image, -1)
	# compute the Laplacian of the image and then return the focus
	# measure, which is simply the variance of the Laplacian
    return cv2.Laplacian(img, 2,3).var()

files=os.listdir()

vector=list()

for i in files:

    ls=list()
    histdesc_fft(i,ls)
    vector.append(ls)
    

desc=pd.DataFrame(vector)


# An "interface" to matplotlib.axes.Axes.hist() method
n, bins, patches = plt.hist(x=vector, bins='auto', color='#0504aa',
                            alpha=0.7, rwidth=0.85)
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('My Very Own Histogram')
plt.text(23, 45, r'$\mu=15, b=3$')
maxfreq = n.max()
# Set a clean upper y-axis limit.
plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)

bins = 'auto'

plt.hist([vector[0:2035], vector[2035:]], bins, label=['x', 'y'])
plt.legend(loc='upper right')
plt.show()

sum(vector[2035:])/2035
    