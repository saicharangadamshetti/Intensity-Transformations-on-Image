#!/usr/bin/env python
# coding: utf-8

# In[43]:


import cv2 
import numpy as np 
from IPython.display import display, Image
import warnings
warnings.filterwarnings("ignore")

# Open the image. 
img = cv2.imread('sample.jpg') 
print('Input Image')
display(Image(filename='sample.jpg'))


# In[50]:


# Apply negative transform
negative_transformed = np.array(255-img, dtype = np.uint8) 
cv2.imwrite('negative_transformed.jpg', log_transformed)
print('negative_transformed')
display(Image('negative_transformed.jpg'))


# In[49]:


# Apply log transform. 
c = 255/(np.log(1 + np.max(img))) 
log_transformed = c * np.log(1 + img)  
log_transformed = np.array(log_transformed, dtype = np.uint8) 
cv2.imwrite('log_transformed.jpg', log_transformed) 
print('log_transformed')
display(Image(filename='log_transformed.jpg'))


# In[45]:


#Power-Law (Gamma) Transformation for different gamma values 
for gamma in [0.1, 0.6, 1.2, 1.8]:
    gamma_corrected = np.array(255*(img / 255) ** gamma, dtype = 'uint8') 
    filename='gamma_transformed '+str(gamma)+'.jpg'
    cv2.imwrite(filename, gamma_corrected)
    print(filename)
    display(Image(filename))


# In[48]:


#Piecewise-Linear Transformation 
# Function to map each intensity level to output intensity level. 
def pixelVal(pix, r1, s1, r2, s2): 
    if (0 <= pix and pix <= r1): 
        return (s1 / r1)*pix 
    elif (r1 < pix and pix <= r2): 
        return ((s2 - s1)/(r2 - r1)) * (pix - r1) + s1 
    else: 
        return ((255 - s2)/(255 - r2)) * (pix - r2) + s2 

# Define parameters. 
r1 = 50
s1 = 0
r2 = 120
s2 = 255

# Vectorize the function to apply it to each value in the Numpy array. 
pixelVal_vec = np.vectorize(pixelVal) 

# Apply contrast stretching. 
contrast_stretched = pixelVal_vec(img, r1, s1, r2, s2) 
contrast_stretched_new=np.array(contrast_stretched,dtype = 'uint8') 
cv2.imwrite('contrast_stretched_new.jpg', contrast_stretched_new) 
display(Image('contrast_stretched_new.jpg'))

