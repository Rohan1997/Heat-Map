#------------------------------------------------------------------------------------
#  						Electronic Design Lab 2018
#				  Indian Institute of Technology, Bombay
#
#				 Smart-shoes for Physiotherapy Diagnostics
#
#							 	Group D08
#	    	  Suyash Bagad  |  Rohan Pathak  |  Mohak Sahu
#------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------
#
# File name: Final_working_real_time_map.py
#
# Description: Final pressure map plotting with 9 sensors
#
#------------------------------------------------------------------------------------

#
# Import required modules 
#
from matplotlib import pyplot as plt
from matplotlib import cm as CM
from matplotlib import mlab as ML
import numpy as np
import cv2
from PIL import Image
import time
import numpy as np
from matplotlib import animation
import math
from matplotlib import cm
import serial

#
# We are using 'serial' module in python to read serial data coming from Bluetooth module.
# This port address is for the serial tx/rx pins on the GPIO header
#
SERIAL_PORT = '/dev/rfcomm0'
#
# Setting the rate of communication between PC and HC-05
#
SERIAL_RATE = 115200

ser = serial.Serial(SERIAL_PORT, SERIAL_RATE)

img = cv2.imread('left.png',0)
#img = cv2.imread('edl_foot_left.png',0)
size = np.shape(img)


#
# Setting the zero positions of sensors on the image of foot.
#
n1 = 9
xMean = [72 ,120 ,192 ,188 ,107 ,201 ,135 ,199 ,177 ]
yMean = [122 ,75 ,54 ,150 ,188 ,251 ,320 ,366 ,412 ]
kx = [100 ,100 ,60 ,50 ,50 ,70 ,66 ,85 ,70]
ky = [100 ,100 ,60 ,70 ,80 ,70 ,56 ,85 ,60]
#kx = [70 ,70 ,70 ,70 ,70 ,70 ,70 ,70 ,70 ]
#ky = [70 ,70 ,70 ,70 ,70 ,70 ,70 ,70 ,70 ]

#
# Setting the amplitudes of gaussian functions for the first iteration.
#
amplitude = [400 ,400 ,800 ,1000 ,950 ,500 ,749 ,700 ,899 ]

height = size[0]
width = size[1]
print(width,height)

x = np.linspace(0, width, width)
y = np.linspace(0, height, height)
#
# Generate x,y matrix
#
X, Y = np.meshgrid(x, y)											

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

def main():
	#
	# tempx multiplies xth gaussian with xth amplitude
	#
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

	#
	# First set up the figure, the axis, and the plot element we want to animate
	# We have used gaussian interpolation technique because of the following reasons:
	# 1) If the maps will be used for statistical data analysis, then it is required to
	#    have clean and smoothly varying data rather than noisy and discontinuous data. Hence
	#    there is a need for spatial filtering of the pressure map after measurement. The widely
	#    accepted representation of the distributions is Gaussian. And also the simplest and fast
	#    filtering could be done by using Gaussian filtering.
	#
	# 2) Considering the biomedical point of view, the foot shape is convex. So we need a curve
	#	 which goes to 0 as we go away from the point. But curves like a parabola, 4 degree curve etc 
	#	 make a cup which doesn't meet the required specifications. Hence we need to use exponential function.
	#	 So the best and standard way of doing it is using Gaussian Interpolation.
	#
	#
	# 	 All references are cited in final report.
	#
	fig = plt.figure()
	image = plt.imshow(final, cmap=cm.jet, interpolation='gaussian')
	
	#
	# Initialization function: plot the background of each frame
	#
	def init():
	    image.set_data(final)
	    return image

	#
	# Animation function.  This is repeatedly called at with time-period of 100 ms.
	#
	def animate(i, size, xMean, yMean, kx, ky):
		#
		# The data received is in the below format for the 9 sensors.
		# data = [100 ,400 ,800 ,1000 ,950 ,500 ,749 ,700 ,899 ]
	    # data = data
	    #
	    data = receive()
	    pressureMap = update(data)
	    image.set_array(pressureMap)
	    return [image]

	anim = animation.FuncAnimation(fig, animate, init_func=init, fargs=[size, xMean, yMean, kx, ky], interval=100)
	cb = fig.colorbar(image)
	cb.set_label('Pressure in kPascal/1.5')
	plt.show()

def update(data):
	newMap = np.zeros(size)
	temp0 = data[0]*P0
	temp1 = data[1]*P1
	temp2 = data[2]*P2
	temp3 = data[3]*P3
	temp4 = data[4]*P4
	temp5 = data[5]*P5
	temp6 = data[6]*P6
	temp7 = data[7]*P7
	temp8 = data[8]*P8

	newMap = temp0 + temp1 + temp2 + temp3 + temp4 + temp5 + temp6 + temp7 + temp8
	newMap[img>30] = 0
	return newMap

#
# The receive() function reads serial data and stores it in a string 
# The string of data from bluetooth module is sent only when indicated
# by the host computer by sending '.' to the module.
#
def receive():

	ser.write('.')

	time.sleep(0.001)

	reading = ser.readline().decode('utf-8')

	inputdata = np.zeros(9)

	for i in range(9):
		inputdata[i] = int(reading[i*4:i*4+4])
	print(inputdata)
	
	input2 = inputdata
	input2[inputdata<20] = 20
	pressureValues = np.zeros(9)

	for j in range(9):
		pressureValues[j] = sensorvalues(input2[j])

	print(pressureValues/1500)
	return pressureValues/1500
	##return inputdata

#
# The following function converts the sensor reading to the actual pressure value using the
# characteristic pressure-resistance curve obtained from calibration.
#
def sensorvalues(data):
	s = 10000*(1024.0/data - 1)
	y = -0.0779*(math.log10(s))*(math.log10(s)) - 0.6972*(math.log10(s)) + 8.4693
	pressure = 10**y
	return pressure

#
# Main funtion
# 
if __name__ == '__main__':
	main()