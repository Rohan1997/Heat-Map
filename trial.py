from matplotlib import pyplot as PLT
from matplotlib import cm as CM
from matplotlib import mlab as ML
import numpy as NP
import cv2

n = 1e5
x = y = NP.linspace(-5, 5, 100)										#Generate 100 equidistant values bet -5 to 5
X, Y = NP.meshgrid(x, y)											#Generate x,y matrix



Z1 = ML.bivariate_normal(X, Y, 1, 2, 0, 0)
#bivariate_normal(X, Y, sigmax=1.0, sigmay=1.0, mux=0.0, muy=0.0, sigmaxy=0.00

Z2 = ML.bivariate_normal(X, Y, 4, 1, 1, 1)
ZD = Z2 - Z1
x = X.ravel()
y = Y.ravel()
z = ZD.ravel()
gridsize=30
PLT.subplot(111)

# if 'bins=None', then color of each hexagon corresponds directly to its count
# 'C' is optional--it maps values to x-y coordinates; if 'C' is None (default) then 
# the result is a pure 2D histogram 

PLT.hexbin(x, y, C=z, gridsize=gridsize, cmap=CM.jet, bins=None)
PLT.axis([x.min(), x.max(), y.min(), y.max()])


cb = PLT.colorbar()
cb.set_label('mean value')

PLT.show()
