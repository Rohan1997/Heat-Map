# Basic working code for reading data directly into python


import serial

import time
# This port address is for the serial tx/rx pins on the GPIO header
SERIAL_PORT = '/dev/rfcomm0'
# Set this to the rate of communication between PC and HC-05
SERIAL_RATE = 115200


def char_to_float(units, tens, hundreds, thousands):
    number = 1000*thousands + 100*hundreds + 10*tens + units
    return number




def main():
    ser = serial.Serial(SERIAL_PORT, SERIAL_RATE)

    while True:
    	#print(x)
    	#print('\n')

        # using ser.readline() assumes each line contains a single reading
        # sent using Serial.println() on the Arduino
        reading = ser.readline().decode('utf-8')
        # reading becomes a string of the form "0121\n0345\n0004\n0112\n0812\n"
        # reading is a string...do whatever you want from here
        
        #read = char_to_float(reading[3], reading[2], reading[1], reading[0])

        print(reading)
        #time.sleep(5)
        
if __name__ == "__main__":
	main()