# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 20:22:23 2021

@author: Administrator
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('Image/Elephant.jpg', 0)

height, width = image.shape

def resize(image, new_width = 100):
    height, width = image.shape
    new_height = new_width * height / width
    return cv2.resize(image, (int(new_width*2), int(new_height)))

image = resize(image, 200)

ASCII_CHARS = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."," "]

cv2.imshow('Image', image)

cv2.waitKey(0)
cv2.destroyAllWindows()

Long, large = image.shape

f = open('sortie.txt','w')

for i in range(Long):
    for j in range(large):
        print(ASCII_CHARS[int(image[i,j]/256*12)], end='', file=f)
    print("", file=f)