from matplotlib import pyplot as plt
from matplotlib import cm as CM
from matplotlib import mlab as ML
import numpy as np
import cv2
from PIL import Image

img = cv2.imread('left.png',0)
im = Image.open('left.png')
width, height = im.size
print(width,height)

x = np.linspace(0, width, width)
y = np.linspace(0, height, height)
X, Y = np.meshgrid(x, y)											#Generate x,y matrix

n1 = 5
yMean = [50  , 153 , 185 , 300 , 405 ]
xMean = [200 , 190 , 110 , 130 , 180 ]
kMean = [60  , 70  , 70  ,  90 , 70 ]
amplitude = [200 , 255 , 255 , 150 , 255 ]
#amplitude = [0 , 0, 0, 0,0]
P1 = np.zeros((height,width))


for i in range(n1):
	P1 = P1 + amplitude[i]*np.exp( (-(X-xMean[i])**2 -(Y-yMean[i])**2)/(kMean[i]*kMean[i]) )
P1[img>30] = 0
x = X.ravel()
y = Y.ravel()
z = P1.ravel()



gridsize=200
plt.subplot(111)

# if 'bins=None', then color of each hexagon corresponds directly to its count
# 'C' is optional--it maps values to x-y coordinates; if 'C' is None (default) then 
# the result is a pure 2D histogram 

plt.hexbin(x, y, C=z, gridsize=gridsize, cmap=CM.jet, bins=None)
plt.axis([x.min(), x.max(), y.min(), y.max()])


cb = plt.colorbar()
cb.set_label('mean value')

plt.ion()
plt.pause(0.01)
plt.draw()

plt.pause(1)


j=1
while 1:
	if j==1:	
		amplitude = [200 , 255 , 255 , 150 , 255 ]
		
		for i in range(n1):
			P1 = P1 + amplitude[i]*np.exp( (-(X-xMean[i])**2 -(Y-yMean[i])**2)/(kMean[i]*kMean[i]) )
		P1[img>30] = 0
		x = X.ravel()
		y = Y.ravel()
		z = P1.ravel()
		plt.hexbin(x, y, C=z, gridsize=gridsize, cmap=CM.jet, bins=None)
		plt.axis([x.min(), x.max(), y.min(), y.max()])
		plt.pause(0.001)
		plt.draw()
		j=2
	else :
		i=0
		amplitude = [1000 , 200 , 100 , 150 , 1055 ]

		for i in range(n1):
			P1 = P1 + amplitude[i]*np.exp( (-(X-xMean[i])**2 -(Y-yMean[i])**2)/(kMean[i]*kMean[i]) )
		P1[img>30] = 0
		x = X.ravel()
		y = Y.ravel()
		z = P1.ravel()
		plt.hexbin(x, y, C=z, gridsize=gridsize, cmap=CM.jet, bins=None)
		plt.axis([x.min(), x.max(), y.min(), y.max()])
		plt.pause(0.001)
		plt.draw()
		j=1
