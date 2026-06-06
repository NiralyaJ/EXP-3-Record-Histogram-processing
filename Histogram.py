#!/usr/bin/env python
# coding: utf-8

# # Ex. No: 03 
# ## Histogram Equalization Using OpenCV (Grayscale & Color Images)
# 
# **Name :** Niralya J   **Reg. No :** 212224230188   **Slot No :** T2-DIPT-2026
# 

# ### Write a Python program using OpenCV to perform histogram equalization on the given grayscale image **"parrot.jpg"**.
# 
# The program should:
# 
# - Import the required libraries (**OpenCV, NumPy, Matplotlib**).
# - Read the image **"parrot.jpg"** in **grayscale** format.
# - Display the grayscale image and plot its histogram.
# - Perform **histogram equalization** on the grayscale image using `cv2.equalizeHist()` to enhance its contrast.
# - Using Matplotlib, display the following in a **2 × 2 grid layout**:
#   - Original Grayscale Image
#   - Histogram of Original Image
#   - Enhanced (Equalized) Image
#   - Histogram of Enhanced Image
# 

# In[1]:


# Import required libraries


import cv2
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


# Read the image in grayscale format

img = cv2.imread('parrot.jpg', 0)


# In[3]:


# Display the grayscale image.


plt.imshow(img)


# In[4]:


# Plot the histogram of the grayscale image
plt.hist(img.ravel(), bins=256, range=[0,256])
plt.title("Histogram of Grayscale Image")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.show()



# In[5]:


# Perform histogram equalization
equalized = cv2.equalizeHist(img)




# In[6]:


# Display [1] the Original Image (Gray Image) and its Histogram, and [2] the Enhanced Image and its Histogram using a 2×2 layout in Matplotlib.



plt.figure(figsize=(10,8))

# [1] Original Grayscale Image
plt.subplot(2,2,1)
plt.imshow(img, cmap='gray')
plt.title("Original Grayscale Image")
plt.axis('off')

# [1] Histogram of Original Image
plt.subplot(2,2,2)
plt.hist(img.ravel(), bins=256, range=[0,256])
plt.title("Histogram of Original Image")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")

# [2] Enhanced (Equalized) Image
plt.subplot(2,2,3)
plt.imshow(equalized, cmap='gray')
plt.title("Equalized Image")
plt.axis('off')

# [2] Histogram of Enhanced Image
plt.subplot(2,2,4)
plt.hist(equalized.ravel(), bins=256, range=[0,256])
plt.title("Histogram of Equalized Image")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()



# ### Write a Python program using OpenCV to perform color image enhancement through histogram equalization in the HSV color space on the given image **"parrot.jpg"**.
# 
# The program should:
# 
# - Import the required libraries (**OpenCV, NumPy, Matplotlib**).
# - Read the color image **"parrot.jpg"**.
# - Plot the **histogram of the original color image** (use the **B, G, and R** channels).
# - Convert the image from **BGR to HSV** color space.
# - Apply **histogram equalization** to one specific channel to improve brightness and contrast using `cv2.equalizeHist()`.
# - Convert the enhanced HSV image back to **BGR** format.
# - Using Matplotlib, display the following in a **2 × 2 grid layout**:
#   - Original Color Image
#   - Histogram of Original Image (BGR channels)
#   - Enhanced Color Image
#   - Histogram of Enhanced Image (BGR channels)
# 

# In[7]:


# Import required libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt



# In[8]:


# Read the colorgiven parrot.jpg image.
img=cv2.imread('parrot.jpg')




# In[9]:


# Plot the histogram of colour image


colors = ('b', 'g', 'r')

for i, color in enumerate(colors):
    hist = cv2.calcHist([img], [i], None, [256], [0,256])
    plt.plot(hist, color=color)

plt.title("Histogram of Color Image (BGR)")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.show()


# In[10]:


# Convert to HSV.


hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


# In[14]:


# Convert to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Split channels
h, s, v = cv2.split(hsv)


# In[15]:


# Perform histogram equalization


# Apply histogram equalization on V channel
v_eq = cv2.equalizeHist(v)

# Merge channels back
hsv_eq = cv2.merge((h, s, v_eq))



# In[16]:


# Convert back to BGR format


hsv = cv2.cvtColor(img,cv2.COLOR_HSV2BGR)


# In[17]:


# Display


plt.imshow(hsv)



# In[ ]:




