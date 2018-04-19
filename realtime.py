from matplotlib import pyplot as plt
from matplotlib import cm as CM
from matplotlib import mlab as ML
import numpy as np
import cv2
from PIL import Image
import time
import numpy as np
import matplotlib.pyplot as plt
import serial

def char_to_float(units, tens, hundreds, thousands):
    number = 1000*int(thousands) + 100*int(hundreds) + 10*int(tens) + int(units)
    return number

# This port address is for the serial tx/rx pins on the GPIO header
SERIAL_PORT = '/dev/rfcomm0'
# Set this to the rate of communication between PC and HC-05
SERIAL_RATE = 115200


inputdata = np.zeros(9)

img = cv2.imread('left.png',0)
im = Image.open('left.png')
width, height = im.size
print(width,height)

x = np.linspace(0, width, width)
y = np.linspace(0, height, height)
X, Y = np.meshgrid(x, y)											#Generate x,y matrix

n1 = 9
xMean = [72 ,120 ,192 ,188 ,107 ,201 ,135 ,199 ,177 ]
yMean = [122 ,75 ,54 ,150 ,188 ,251 ,320 ,366 ,412 ]
kx = [100 ,100 ,60 ,50 ,50 ,70 ,66 ,85 ,70]
ky = [100 ,100 ,60 ,70 ,80 ,70 ,56 ,85 ,60]
#kx = [70 ,70 ,70 ,70 ,70 ,70 ,70 ,70 ,70 ]
#ky = [70 ,70 ,70 ,70 ,70 ,70 ,70 ,70 ,70 ]

#amplitude = [1000 ,1000 ,1000 ,1000 ,1000 ,1000 ,1000 ,1000 ,1000 , ]

amplitude = [400 ,400 ,800 ,1000 ,950 ,500 ,749 ,700 ,899 ]

P0 = np.zeros((height,width))
P1 = np.zeros((height,width))
P2 = np.zeros((height,width))
P3 = np.zeros((height,width))
P4 = np.zeros((height,width))
P5 = np.zeros((height,width))
P6 = np.zeros((height,width))
P7 = np.zeros((height,width))
P8 = np.zeros((height,width))

P0 = np.exp( (-(X-xMean[0])**2)/(kx[0]*kx[0]) -((Y-yMean[0])**2)/(ky[0]*ky[0]) )
P1 = np.exp( (-(X-xMean[1])**2)/(kx[1]*kx[1]) -((Y-yMean[1])**2)/(ky[1]*ky[1]) )
P2 = np.exp( (-(X-xMean[2])**2)/(kx[2]*kx[2]) -((Y-yMean[2])**2)/(ky[2]*ky[2]) )
P3 = np.exp( (-(X-xMean[3])**2)/(kx[3]*kx[3]) -((Y-yMean[3])**2)/(ky[3]*ky[3]) )
P4 = np.exp( (-(X-xMean[4])**2)/(kx[4]*kx[4]) -((Y-yMean[4])**2)/(ky[4]*ky[4]) )
P5 = np.exp( (-(X-xMean[5])**2)/(kx[5]*kx[5]) -((Y-yMean[5])**2)/(ky[5]*ky[5]) )
P6 = np.exp( (-(X-xMean[6])**2)/(kx[6]*kx[6]) -((Y-yMean[6])**2)/(ky[6]*ky[6]) )
P7 = np.exp( (-(X-xMean[7])**2)/(kx[7]*kx[7]) -((Y-yMean[7])**2)/(ky[7]*ky[7]) )
P8 = np.exp( (-(X-xMean[8])**2)/(kx[8]*kx[8]) -((Y-yMean[8])**2)/(ky[8]*ky[8]) )

temp0 = amplitude[0]*P0
temp1 = amplitude[1]*P1
temp2 = amplitude[2]*P2
temp3 = amplitude[3]*P3
temp4 = amplitude[4]*P4
temp5 = amplitude[5]*P5
temp6 = amplitude[6]*P6
temp7 = amplitude[7]*P7
temp8 = amplitude[8]*P8

final = temp0 + temp1 + temp2 + temp3 + temp4 + temp5 + temp6 + temp7 + temp8

final[img>30] = 0
x = X.ravel()
y = Y.ravel()
z = final.ravel()

gridsize=300
plt.subplot(111)

plt.hexbin(x, y, C=z, gridsize=gridsize, cmap=CM.jet, bins=None)
plt.axis([x.min(), x.max(), y.min(), y.max()])

cb = plt.colorbar()
cb.set_label('Pressure')
plt.pause(0.05)
plt.draw()

ser = serial.Serial(SERIAL_PORT, SERIAL_RATE)


while True:
	print('here6')
	reading = ser.readline().decode('utf-8')
	
	print('here7')
	print(reading)
	print('here8')
	
	for j in range(9):
	    read = char_to_float(reading[3+j*4], reading[2+j*4], reading[1+j*4], reading[0+j*4])

	    print(read, " ",j)
	    inputdata[j] = read

	print('here9')
	amplitude = inputdata
	print(amplitude)
	
	temp0 = amplitude[0]*P0
	temp1 = amplitude[1]*P1
	temp2 = amplitude[2]*P2
	temp3 = amplitude[3]*P3
	temp4 = amplitude[4]*P4
	temp5 = amplitude[5]*P5
	temp6 = amplitude[6]*P6
	temp7 = amplitude[7]*P7
	temp8 = amplitude[8]*P8

	final = temp0 + temp1 + temp2 + temp3 + temp4 + temp5 + temp6 + temp7 + temp8

	final[img>30] = 0

	x = X.ravel()
	y = Y.ravel()
	z = final.ravel()

	plt.hexbin(x, y, C=z, gridsize=gridsize, cmap=CM.jet, bins=None)
	plt.axis([x.min(), x.max(), y.min(), y.max()])
	plt.pause(0.01)
	plt.draw()

	plt.pause(1)
	#time.sleep(2)