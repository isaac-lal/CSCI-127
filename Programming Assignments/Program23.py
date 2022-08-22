# Name: Isaac Lal
# Email: isaac.lal46@myhunter.cuny.edu
# Date: October 18, 2021
# Programming Assignment #23

import matplotlib.pyplot as plt
import numpy as np

file1 = input("Enter first image file name: ")
file2 = input("Enter first image file name: ")

img1 = plt.imread(file1)
img2 = plt.imread(file2)

t = float(input("Enter threshold of white pixels: "))

countSnow1 = 0 #Number of pixels in image 1 that are almost white
countSnow2 = 0 #Number of pixels in image 2 that are almost white

for i in range(img1.shape[0]):
     for j in range(img1.shape[1]):
          #Check if red, green, and blue are > t:
          if (img1[i,j,0] > t) and (img1[i,j,1] > t) and (img1[i,j,2] > t):
               countSnow1 = countSnow1 + 1

for i in range(img2.shape[0]):
     for j in range(img2.shape[1]):
          #Check if red, green, and blue are > t:
          if (img2[i,j,0] > t) and (img2[i,j,1] > t) and (img2[i,j,2] > t):
               countSnow2 = countSnow2 + 1

print("Snow count of first image:", countSnow1)
print("Snow count of second image:", countSnow2)
print("Difference between first and second image:", max(countSnow1,countSnow2) - min(countSnow1,countSnow2))
