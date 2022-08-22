# Name: Isaac Lal
# Email: isaac.lal46@myhunter.cuny.edu
# Date: October 14, 2021
# Programming Assignment #21

import matplotlib.pyplot as plt
import numpy as np

img = np.ones((10,10,3))

img[5:,:5,:]= 0

plt.imshow(img)
plt.show()