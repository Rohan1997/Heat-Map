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
# File name: README.txt 
#
# Description: Self-explanatory.
#
#------------------------------------------------------------------------------------

#-----------------  Procedure to connect to Bluetooth module ------------------------

Note: We have worked and tested the entire process on Windows 10 as well as Ubuntu 16.04.
However, the description is made only for 'non-trivial' ubuntu. 

1) Go to bluetooth settings

2) Add a new device 'DD08'

3) Pin: 0321

4) Status would be shown as 'Connected and Paired'

5) Create a serial port 'rfcomm0'

Example:

>> sudo hcitool scan
   Scanning...
   98:D3:31:20:AE:3D	DD08
   68:D2:11:50:AI:2E	DELL-Desktop
>> sudo killall rfcomm0
>> sudo rfcomm connect /dev/rfcomm0 98:D3:31:20:AE:3D 1 &

   1:6472
>> Connected rfcomm0 to 98:D3:31:20:AE:3D through channel 1
   Press Ctrl+C to hang up
