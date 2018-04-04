
# coding: utf-8

# In[29]:


#Write a function to find moving average in an array over a window:
#Test it over [3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150] and window of 3.

import numpy as np
from numpy import convolve

#define the function to calculate the average
def calculatemovingaverage (values, window):
    weights = np.repeat(1.0, window)/window
    #use the convolve function of python 
    sma= np.convolve(values, weights, 'valid')
    return sma
 
#User input for the array(number of elements and the actual numbers)
arr = []
elem = int(input("Number of elements in the array:"))
for i in range(0, elem):
    arr.append(int(input("Enter one by one number to be present in array :")))
k = input("Enter the window period ")

MA = calculatemovingaverage(arr,int(k))
print (MA)

