# -*- coding: utf-8 -*-
"""ML PRJ1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iY55U8LfVlxGBxyMQoVsSsqnj_FehYcH
"""

#P3

#implementation of simpsons 1/3 rd rule
# x 8.20 8.30 8.40 8.50 9 
# y 24.2 35 41.3 42.8 39.4 
# s=h/3[(v0+ v4 )+4(v1 + v3 )+2 v2 (7) 
# =1/3*1/6[(24.2+39.4)+4(35+42.8)+2(41.3)] 
# =25.4
# The image given is taken and single point is created.
# This is compared with the data
# The matched data finds the equation
# Equation sperates the point
# points are matched with the given input
# KMP Algorithm is used to compare
# The matched segment is selected 
#valuate logx dx within limit 4 to 5.2.

#First we will divide interval into six equal 
#parts as number of interval should be even.

#x    :  4     4.2   4.4   4.6   4.8  5.0  5.2
#logx :  1.38  1.43  1.48  1.52  1.56 1.60 1.64

#Now we can calculate approximate value of integral
#using above formula:
 #    = h/3[( 1.38 + 1.64) + 4 * (1.43 + 1.52 + 
          #            1.60 ) +2 *(1.48 + 1.56)]
  #   = 1.84
#Hence the approximation of above integral is 
#1.827 using Simpson's 1/3 rule.  


# Python code for simpson's 1 / 3 rule
import math
 
# Function to calculate f(x)
def func( x ):
    return math.log(x)
 
# Function for approximate integral
def simpsons_( ll, ul, n ):
 
    # Calculating the value of h
    h = ( ul - ll )/n
 
    # List for storing value of x and f(x)
    x = list()
    fx = list()
     
    # Calculating values of x and f(x)
    i = 0
    while i<= n:
        x.append(ll + i * h)
        fx.append(func(x[i]))
        i += 1
 
    # Calculating result
    res = 0
    i = 0
    while i<= n:
        if i == 0 or i == n:
            res+= fx[i]
        elif i % 2 != 0:
            res+= 4 * fx[i]
        else:
            res+= 2 * fx[i]
        i+= 1
    res = res * (h / 3)
    return res
     
# Driver code
lower_limit = 4   # Lower limit
upper_limit = 5.2 # Upper limit
n = 6 # Number of interval
print("%.6f"% simpsons_(lower_limit, upper_limit, n))

#P2.1
#Python program for KMP Algorithm
def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)

# create lps[] that will hold the longest prefix suffix
# values for pattern
    lps = [0]*M
    j = 0 # index for pat[]

    # Preprocess the pattern (calculate lps[] array)
    computeLPSArray(pat, M, lps)

    i = 0 # index for txt[]
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1

        if j == M:
            print("Found pattern at index " + str(i-j))
            j = lps[j-1]

        # mismatch after j matches
        elif i < N and pat[j] != txt[i]:
            # Do not match lps[0..lps[j-1]] characters,
            # they will match anyway
            if j != 0:
                j = lps[j-1]
            else:
                i += 1

def computeLPSArray(pat, M, lps):
    len = 0 # length of the previous longest prefix suffix

    lps[0] # lps[0] is always 0
    i = 1

    # the loop calculates lps[i] for i = 1 to M-1
    while i < M:
        if pat[i]== pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is similar
            # to search step.
            if len != 0:
                len = lps[len-1]

                # Also, note that we do not increment i here
            else:
                lps[i] = 0
                i += 1

txt = "AAACAAAB"
pat = "AB"
KMPSearch(pat, txt)

# This code is contributed by Bhavya Jain

# Here this program is changed to get the output
# an array containing the difference of the pixels 2 2 ,1 3,4 5,5 4 x y respectively
# the matching string is for example : 1 3,4 5

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
#filepath = r'C:\Users\HP\Documents\Me.jpg'
#image = Image.open(r"C:\Users\HP\Documents\lenna.png")
#image.show()
#img = cv.imread(r'C:\Users\HP\Documents\me.jpg',0)
img = cv.imread(r'D:\college\college docs\ml proj\images\plot1.png',0)
#n,m = img.shape 
edges = cv.Canny(img,400,400)
n,m = edges.shape
#plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.subplot(121),plt.imshow(edges,cmap = 'gray')
image_grey = edges
for row in range(n):
    for col in range(m):     
        if((image_grey[row,col]) > 0):
            print('here is greater than 0')
            print(image_grey[row,col])

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
#filepath = r'C:\Users\HP\Documents\Me.jpg'
#image = Image.open(r"C:\Users\HP\Documents\lenna.png")
#image.show()
#img = cv.imread(r'D:\college\college docs\ml proj\images\d5.jpg',0)
img = cv.imread(r'D:\college\college docs\ml proj\images\plot1.png',0)
n,m = img.shape 
edges = cv.Canny(img,400,400)
#plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.subplot(121),plt.imshow(edges,cmap = 'gray')

#P2 identification of the image segments
#The identification of numbers in image is made first part
#Then identification of face image is made.

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
#filepath = r'C:\Users\HP\Documents\Me.jpg'
#image = Image.open(r"C:\Users\HP\Documents\lenna.png")
#image.show()
img = cv.imread(r'D:\college\college docs\ml proj\images\d5.jpg',0)
edges = cv.Canny(img,100,200)
#plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.subplot(121),plt.imshow(edges,cmap = 'gray')

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
#filepath = r'C:\Users\HP\Documents\Me.jpg'
#image = Image.open(r"C:\Users\HP\Documents\lenna.png")
#image.show()
img = cv.imread(r'D:\college\college docs\ml proj\images\d5.jpg',0)
img = cv.imread(r'D:\college\college docs\ml proj\images\plot1.png',0)
edges = cv.Canny(img,100,200)
#plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.subplot(121),plt.imshow(edges,cmap = 'gray')

###################

#P5
import numpy as np
from scipy import integrate

from rtree import index

idx = index.Index()

left,bottom,right,top = (0.0,0.0,1.0,1.0)

idx.insert(0,(left,bottom,right,top))
# here the values that can be determined can be,left,bottom,right,top

left,bottom,right,top = (0.33,0.23,0.35,0.25)

idx.insert(1,(left,bottom,right,top))

list(idx.nearest((0.31,0.22,0.34,0.24)))

#Rtree also supports inserting any object you can pickle into the index (called a clustered index in libspatialindex parlance). The following inserts the picklable object 42 into the index with the given id:

idx.insert(1, (left, bottom, right, top), obj=45)

[n.object for n in idx.intersection((left, bottom, right, top), objects=True)]
[None, None, 42]

idx.insert(1, (left, bottom, right, top), obj=45)

[n.object for n in idx.intersection((left, bottom, right, top), objects=True)]

idx.insert(0,(left,bottom,right,top),obj=47)

[n.object for n in idx.intersection((left, bottom, right, top), objects=True)]

