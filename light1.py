import time
import math
import mraa
import socket
import fcntl
import struct
import pyupm_i2clcd as lcd

IntensitySensor = mraa.Aio(3)

try:
  while(1):

      a= IntensitySensor.read()
      print a
      time.sleep(1)
except KeyboardInterrupt:
  exit


