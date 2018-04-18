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
    	reading = ser.readline().decode('utf-8')
        # reading becomes a string of the form "0121\n0345\n0004\n0112\n0812\n"
        # reading is a string...do whatever you want from here
        print(reading)

        for i in range(9):
            read = char_to_float(reading[3+i*4], reading[2+i*4], reading[1+i*4], reading[0+i*4])

            print(read, " ",i)
            inputdata[i] = read
            #count = (count + 1)%9


    
        P1 = np.zeros((height,width))
        amplitude = inputdata
        
        for i in range(n1):
            P1 = P1 + amplitude[i]*np.exp( (-(X-xMean[i])**2)/(kx[i]*kx[i]) -((Y-yMean[i])**2)/(ky[i]*ky[i]) )
        
        P1[img>30] = 0
        
        x = X.ravel()
        y = Y.ravel()
        z = P1.ravel()

        plt.hexbin(x, y, C=z, gridsize=gridsize, cmap=CM.jet, bins=None)
        plt.axis([x.min(), x.max(), y.min(), y.max()])
        plt.pause(0.01)
        plt.draw()

        plt.pause(1)
        time.sleep(3)

   
if __name__ == "__main__":
	
    count = 0
    inputdata = np.zeros(9)


    img = cv2.imread('left.png',0)
    im = Image.open('left.png')
    width, height = im.size
    print(width,height)

    x = np.linspace(0, width, width)
    y = np.linspace(0, height, height)
    X, Y = np.meshgrid(x, y)                                            #Generate x,y matrix

    n1 = 9
    xMean = [72 ,120 ,192 ,188 ,107 ,201 ,135 ,199 ,177 ]
    yMean = [122 ,75 ,54 ,150 ,188 ,251 ,320 ,366 ,412 ]
    kx = [60 ,70 ,70 ,90 ,70 ,70 ,46 ,45 ,90]
    ky = [60 ,70 ,70 ,90 ,70 ,70 ,46 ,45 ,90]
    
    kMean = [60 ,70 ,70 ,90 ,70 ,70 ,46 ,45 ,90]
    amplitude = [200 ,900 ,800 ,150 ,850 ,742 ,249 ,245 ,900 ]
    P1 = np.zeros((height,width))

    for i in range(n1):
        P1 = P1 + amplitude[i]*np.exp( (-(X-xMean[i])**2)/(kx[i]*kx[i]) -((Y-yMean[i])**2)/(ky[i]*ky[i]) )
            
    P1[img>30] = 0
    
    x = X.ravel()
    y = Y.ravel()
    z = P1.ravel()

    gridsize=200
    plt.subplot(111)

    plt.hexbin(x, y, C=z, gridsize=gridsize, cmap=CM.jet, bins=None)
    plt.axis([x.min(), x.max(), y.min(), y.max()])


    cb = plt.colorbar()
    cb.set_label('mean value')

    plt.ion()
    plt.pause(0.01)

    plt.draw()

    main()