import numpy as np
import serial



def char_to_float(units, tens, hundreds, thousands):
    number = 1000*int(thousands) + 100*int(hundreds) + 10*int(tens) + int(units)
    int(number)
    return number


# This port address is for the serial tx/rx pins on the GPIO header
SERIAL_PORT = '/dev/rfcomm0'
# Set this to the rate of communication between PC and HC-05
SERIAL_RATE = 115200

print('here10')
inputdata = np.zeros(9)
amplitude = np.zeros(9)
ser = serial.Serial(SERIAL_PORT, SERIAL_RATE)

	
while True:
	reading = ser.readline().decode('utf-8')
	print('here7')

	print(reading)

	for j in range(9):
	    read = char_to_float(reading[3+j*4], reading[2+j*4], reading[1+j*4], reading[0+j*4])
	    #read = 1000*reading[0+j*4] + 
	    print(read,' ',j)
	    inputdata[j] = read
	
	print('here8')
	print(inputdata)