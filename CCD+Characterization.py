
####################################################################################################
import os
import glob
import numpy as np
import astropy.io.fits as fits
import matplotlib.pyplot as plt
####################################################################################################
os.chdir('/Users/bobbystiller/Documents/Modern Observational Techniques/CCD Characterization/Bias')

files = glob.glob('*.fit')

bias = []

for file in files:
    bias.append(fits.getdata(file))
    
bias = np.array(bias)
median_bias = np.median(bias, axis=0)


####################################################################################################
plt.imshow(median_bias, 
           vmin = np.median(median_bias), # black point
           vmax = 1.01*np.median(median_bias), # white point
           cmap = 'cubehelix')
plt.show()

####################################################################################################
def dark_current(array, gain, exposure_time):
    
    array2 = array - median_bias
    counts = np.sum(array2)
    electrons = gain*counts
    pixels = np.square(np.shape(array)[0]) # total pixels
    dark_current = electrons/pixels/exposure_time
    
    return dark_current


# In[385]:
####################################################################################################
os.chdir('/Users/bobbystiller/Documents/Modern Observational Techniques/CCD Characterization/Darks')

files_1s = glob.glob('*1s-*.fit')
files_5s = glob.glob('*5s-*.fit')
files_10s = glob.glob('*10s-*.fit')
files_15s = glob.glob('*15s-*.fit')
files_20s = glob.glob('*20s-*.fit')
files_25s = glob.glob('*25s-*.fit')
files_30s = glob.glob('*30s-*.fit')

darks_1s = []
darks_5s = []
darks_10s = []
darks_15s = []
darks_20s = []
darks_25s = []
darks_30s = []

for f1, f2, f3, f4, f5, f6, f7 in zip(files_1s, files_5s, files_10s, files_15s, files_20s, files_25s, files_30s):
    darks_1s.append(fits.getdata(f1))
    darks_5s.append(fits.getdata(f2))
    darks_10s.append(fits.getdata(f3))
    darks_15s.append(fits.getdata(f4))
    darks_20s.append(fits.getdata(f5))
    darks_25s.append(fits.getdata(f6))
    darks_30s.append(fits.getdata(f7))

darks_1s = np.array(darks_1s)
darks_5s = np.array(darks_5s)
darks_10s = np.array(darks_10s)
darks_15s = np.array(darks_15s)
darks_20s = np.array(darks_20s)
darks_25s = np.array(darks_25s)
darks_30s = np.array(darks_30s)

median_dark_1s = np.median(darks_1s, axis=0)
median_dark_5s = np.median(darks_5s, axis=0)
median_dark_10s = np.median(darks_10s, axis=0)
median_dark_15s = np.median(darks_15s, axis=0)
median_dark_20s = np.median(darks_20s, axis=0)
median_dark_25s = np.median(darks_25s, axis=0)
median_dark_30s = np.median(darks_30s, axis=0)

print(dark_current(median_dark_1s, gain, 1))
print(dark_current(median_dark_5s, gain, 5))
print(dark_current(median_dark_10s, gain, 10))
print(dark_current(median_dark_15s, gain, 15))
print(dark_current(median_dark_20s, gain, 20))
print(dark_current(median_dark_25s, gain, 25))
print(dark_current(median_dark_30s, gain, 25))


# In[384]:

os.chdir('/Users/bobbystiller/Documents/Modern Observational Techniques/CCD Characterization/Reds')

files_1s = glob.glob('*1s-*.fit')
files_3s = glob.glob('*3s-*.fit')
files_5s = glob.glob('*5s-*.fit')
files_7s = glob.glob('*7s-*.fit')
files_9s = glob.glob('*9s-*.fit')

reds_1s = []
reds_3s = []
reds_5s = []
reds_7s = []
reds_9s = []

for f1, f2, f3, f4, f5 in zip(files_1s, files_3s, files_5s, files_7s, files_9s):
    reds_1s.append(fits.getdata(f1))
    reds_3s.append(fits.getdata(f2))
    reds_5s.append(fits.getdata(f3))
    reds_7s.append(fits.getdata(f4))
    reds_9s.append(fits.getdata(f5))

reds_1s = np.array(reds_1s)
reds_3s = np.array(reds_3s)
reds_5s = np.array(reds_5s)
reds_7s = np.array(reds_7s)
reds_9s = np.array(reds_9s)

median_red_1s = np.median(reds_1s, axis=0)
median_red_3s = np.median(reds_3s, axis=0)
median_red_5s = np.median(reds_5s, axis=0)
median_red_7s = np.median(reds_7s, axis=0)
median_red_9s = np.median(reds_9s, axis=0)


# In[387]:

plt.imshow(median_red_1s, 
           vmin = np.median(median_red_1s), # black point
           vmax = 1.01*np.median(median_red_1s), # white point
           cmap = 'cubehelix')
plt.show()

plt.imshow(median_red_3s, 
           vmin = np.median(median_red_3s), # black point
           vmax = 1.01*np.median(median_red_3s), # white point
           cmap = 'cubehelix')
plt.show()

plt.imshow(median_red_5s, 
           vmin = np.median(median_red_5s), # black point
           vmax = 1.01*np.median(median_red_5s), # white point
           cmap = 'cubehelix')
plt.show()

plt.imshow(median_red_7s, 
           vmin = np.median(median_red_7s), # black point
           vmax = 1.01*np.median(median_red_7s), # white point
           cmap = 'cubehelix')
plt.show()

plt.imshow(median_red_9s, 
           vmin = np.median(median_red_9s), # black point
           vmax = 1.01*np.median(median_red_9s), # white point
           cmap = 'cubehelix')
plt.show()


# In[ ]:



