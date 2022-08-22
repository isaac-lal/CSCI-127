# Name: Isaac Lal
# Email: isaac.lal46@myhunter.cuny.edu
# Date: October 13, 2021
# Programming Assignment #20

import numpy as np
import matplotlib.pyplot as plt

#Read in the data to an array, called elevations:
elevations = np.loadtxt('elevationsNYC.txt')

#Take the shape (dimensions) of the elevations
#and add another dimension to hold the 3 color channels:
mapShape = elevations.shape + (3,)

#Create a blank image that's all zeros:
floodMap = np.zeros(mapShape)

for row in range(mapShape[0]):
    for col in range(mapShape[1]):
         if elevations[row,col] <= 0:
           floodMap[row,col,0] = 1.0
           floodMap[row,col,1] = 1.0
         elif elevations[row,col] <= 5:
            floodMap[row,col,0] = 1.0     #Set the red channel to 100%
         elif elevations[row,col] > 5 and elevations[row,col] <= 20:
            floodMap[row,col,0] = 0.5
            floodMap[row,col,1] = 0.5
            floodMap[row,col,2] = 0.5
         else:
            #Above the 6 foot storm surge and didn't flood
            floodMap[row,col,1] = 1.0   #Set the green channel to 100%

#Load the flood map image into matplotlib.pyplot:
#plt.imshow(floodMap)

#Display the plot:
#plt.show()

#Save the image:
plt.imsave('floodMap.png', floodMap)