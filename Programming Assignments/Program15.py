# Name: Isaac Lal
# Email: isaac.lal46@myhunter.cuny.edu
# Date: October 5, 2021
# Programming Assignment #15

import matplotlib.pyplot as plt
import numpy as np

image = input("Enter name of the input file: ")
output = input("Enter name of the outfile file: ")

img = plt.imread(image)

img2 = img.copy()
img2[:,:,2] = 0

plt.imsave(output,img2)