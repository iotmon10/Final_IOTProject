import time
import mraa
import math

#SENSOR TRIGGER
trig1 = mraa.Gpio(7)
trig1.dir(mraa.DIR_OUT)

trig2 = mraa.Gpio(3)
trig2.dir(mraa.DIR_OUT)


#SENSOR ECHO
echo1 = mraa.Gpio(8)
echo1.dir(mraa.DIR_IN)

echo2 = mraa.Gpio(4)
echo2.dir(mraa.DIR_IN)

ledin = mraa.Gpio(2)
ledin.dir(mraa.DIR_OUT)

ledout = mraa.Gpio(13)
ledout.dir(mraa.DIR_OUT)

signaloff1 = 0
signalon1 = 0
signalon2 = 0
signaloff2 = 0
timepassed1,timepassed2,distance1,distance2 = 0,0,0,0

time.sleep(0.3)

while True:

	trig2.write(1)
	time.sleep(0.00001)
	trig2.write(0)

#	signaloff1 = time.time()

	while (echo1.read()==0 and echo2.read()==0):
		signaloff1 = time.time()
		
	while echo1.read() == 1:
		signalon1 = time.time()

	while echo2.read() == 1:
		signalon2 = time.time()

	timepassed1 = signalon1 - signaloff1
	distance1 = timepassed1*17000

	timepassed2 = signalon2 - signaloff1
	distance2 = timepassed2*17000

	print "distance1:   %s" %distance1
	print "distance2:   %s" %distance2
	time.sleep(0.6)
