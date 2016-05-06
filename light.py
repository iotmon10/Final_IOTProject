#!/usr/bin/env python
import time
import math
import mraa
import socket
import fcntl
import struct
import pyupm_i2clcd as lcd

Ledin = 3
IntensitySensor = mraa.Aio(3)
op = mraa.Gpio(Ledin)
#IntensitySensor.dir(mraa.DIR_IN)
op.dir(mraa.DIR_OUT)
threshold1=120
threshold2 = 122

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

try:
  while(1):

      a= IntensitySensor.read()
      print a
      #print(IntensitySensor.read())
  #    R= 10*(1023-IntensitySensor.read())/IntensitySensor.read()
   #   print(R)
      if(IntensitySensor.read() > threshold1 and IntensitySensor.read()< threshold2+1) :
      #  print(IntensitySensor.read())  
        myLcd.clear()
        myLcd.setCursor(0,0)
        myLcd.write("Study/Medium Bright arena!")
        op.write(1)
      
      #print(c)
      elif(IntensitySensor.read() > threshold2):
       # print(IntensitySensor.read())  
        myLcd.clear()
        myLcd.setCursor(0,0)
        myLcd.write("Bright arena")
        op.write(1)
      #c += 0
      #print(c)

      elif(IntensitySensor.read() < threshold1):
       # print(IntensitySensor.read())  
        myLcd.clear()
        myLcd.setCursor(0,0)
        myLcd.write("Dull arena")
        op.write(0)
      #time.sleep(1.0)  
except KeyboardInterrupt:
  exit


