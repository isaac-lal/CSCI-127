# Name: Isaac Lal
# Email: isaac.lal46@myhunter.cuny.edu
# Date: October 8, 2021
# Programming Assignment #18

import numpy as np
import matplotlib.pyplot as plt

img = np.zeros((30, 30, 3))

img[range(6),:,0] = 1
img[range(6),:,2] = 1

img[:,range(6),0] = 1
img[:,range(6),2] = 1

for row in range(15, 21):
    img[row,:,0] = 1
    img[row,:,2] = 1

for row in range(18):
    for col in range(25, 30):
        img[row,col,0] = 1
        img[row,col,2] = 1

plt.imsave("logo.png", img)