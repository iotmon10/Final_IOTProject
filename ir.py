#!/usr/bin/env python
import time
import math
import mraa
import socket
import fcntl
import struct
import pyupm_i2clcd as lcd

PIRSensorin1,PIRSensorin2 = 7,8
inp1,inp2 = mraa.Gpio(PIRSensorin1),mraa.Gpio(PIRSensorin2)
inp1.dir(mraa.DIR_IN)
inp2.dir(mraa.DIR_IN)
c1,c2=0,0
 
def get_ip_address(ifname):
       
	s = socket.socket(socket.AD_INET, socket.SOCK_DGRAM)
	return socket.inet_ntoa(fcntl.ioctl(
		s.fileno(),
		0x8915, # SIOCGIFADDR
		struc.pack('256s', ifname[:15])
	)[20:24])

#initialize Jhd1313ml at 0x3E (LCD_ADDRESS AND 0x62 (RGB_ADDRESS))
myLcd = lcd.Jhd1313m1(0, 0x3E, 0x62)
#clear 
myLcd.clear()
#purple
myLcd.setColor(255,0,255)
#initialize cursor
myLcd.setCursor(0,0)

a=inp1.read()
b=inp2.read()
count = 0
try:
  while(1):
    if(inp1.read()):
	count =count +1
	print (count)
	#time.sleep(1)
    else:
	print ("not detecting anything")
	#time.sleep(1)
      #while(b==0):
#	pass
 #     myLcd.clear()
  #    myLcd.setCursor(0,0)
   #   myLcd.write("Entry!")
    #  c1 +=1
     # print("count_in:"+str(c1))
      #time.sleep(1.0)
      
    #elif(b):
     
     #while(a==0):
#	pass
 #    myLcd.clear()
  #   myLcd.setCursor(0,0)
   #  myLcd.write("Exit")
    # c2 += 1
     ##print("count_out:" +str(c2))
     #time.sleep(1.0)
 
    #time.sleep(2.0)
    
except KeyboardInterrupt:
  exit


