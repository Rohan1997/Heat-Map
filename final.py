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
yMean = [50  , 153 , 185 , 300 , 405 ];
xMean = [200 , 190 , 110 , 130 , 180 ];
kMean = [60  , 70  , 70  ,  90 , 70 ];
amplitude = [200 , 255 , 255 , 150 , 255 ];

P1 = np.zeros((height,width))


i=0
P1 = + amplitude[i]*np.exp( (-(X-xMean[i])**2 -(Y-yMean[i])**2)/(kMean[i]*kMean[i]) )
i=1
P2 = + amplitude[i]*np.exp( (-(X-xMean[i])**2 -(Y-yMean[i])**2)/(kMean[i]*kMean[i]) )
i=2
P3 = + amplitude[i]*np.exp( (-(X-xMean[i])**2 -(Y-yMean[i])**2)/(kMean[i]*kMean[i]) )
i=3
P4 = + amplitude[i]*np.exp( (-(X-xMean[i])**2 -(Y-yMean[i])**2)/(kMean[i]*kMean[i]) )
i=4
P5 = + amplitude[i]*np.exp( (-(X-xMean[i])**2 -(Y-yMean[i])**2)/(kMean[i]*kMean[i]) )

P = P1+P2+P3+P4+P5

P[img>30] = 0

#for i in range(n1):
#	P1 = P1 + amplitude[i]*np.exp( (-(X-xMean[i])**2 -(Y-yMean[i])**2)/(kMean[i]*kMean[i]) )

x = X.ravel()
y = Y.ravel()

z1 = P1.ravel()
z2 = P2.ravel()
z3 = P3.ravel()
z4 = P4.ravel()
z5 = P5.ravel()
z = P.ravel()



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

plt.pause(2)


j=1
while 1:
	if j==1:	
		amplitude[1] = 1000
		i=0
		P1 = + amplitude[i]*np.exp( (-(X-xMean[i])**2 -(Y-yMean[i])**2)/(kMean[i]*kMean[i]) )
		i=1
		P2 = + amplitude[i]*np.exp( (-(X-xMean[i])**2 -(Y-yMean[i])**2)/(kMean[i]*kMean[i]) )
		i=2
		P3 = + amplitude[i]*np.exp( (-(X-xMean[i])**2 -(Y-yMean[i])**2)/(kMean[i]*kMean[i]) )
		i=3
		P4 = + amplitude[i]*np.exp( (-(X-xMean[i])**2 -(Y-yMean[i])**2)/(kMean[i]*kMean[i]) )
		i=4
		P5 = + amplitude[i]*np.exp( (-(X-xMean[i])**2 -(Y-yMean[i])**2)/(kMean[i]*kMean[i]) )

		P = P1+P2+P3+P4+P5

		P[img>30] = 0
		x = X.ravel()
		y = Y.ravel()
		z = P.ravel()
		plt.hexbin(x, y, C=z, gridsize=gridsize, cmap=CM.jet, bins=None)
		plt.axis([x.min(), x.max(), y.min(), y.max()])
		plt.pause(0.001)
		plt.draw()
		j=2
	else :
		i=0
		amplitude[1] = 200
		P1 = + amplitude[i]*np.exp( (-(X-xMean[i])**2 -(Y-yMean[i])**2)/(kMean[i]*kMean[i]) )
		i=1
		P2 = + amplitude[i]*np.exp( (-(X-xMean[i])**2 -(Y-yMean[i])**2)/(kMean[i]*kMean[i]) )
		i=2
		P3 = + amplitude[i]*np.exp( (-(X-xMean[i])**2 -(Y-yMean[i])**2)/(kMean[i]*kMean[i]) )
		i=3
		P4 = + amplitude[i]*np.exp( (-(X-xMean[i])**2 -(Y-yMean[i])**2)/(kMean[i]*kMean[i]) )
		i=4
		P5 = + amplitude[i]*np.exp( (-(X-xMean[i])**2 -(Y-yMean[i])**2)/(kMean[i]*kMean[i]) )

		P = P1+P2+P3+P4+P5

		P[img>30] = 0
		x = X.ravel()
		y = Y.ravel()
		z = P.ravel()
		plt.hexbin(x, y, C=z, gridsize=gridsize, cmap=CM.jet, bins=None)
		plt.axis([x.min(), x.max(), y.min(), y.max()])
		plt.pause(0.001)
		plt.draw()
		j=1
