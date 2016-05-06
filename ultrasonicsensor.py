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

count1 = 0
count2 = 0

#signaloff1 = 0
#signalon1 = 0
#signalon2 = 0
#signaloff2 = 0
#timepassed1,timepassed2,distance1,distance2 = 0,0,0,0

global firstTrigger 
global lastTrigger
lastTrigger = 0
firstTrigger = 1
time.sleep(0.3)

def get_entry():
	
	#trig1.write(1)
	#time.sleep(0.00001)
	#trig1.write(0)

	while echo1.read() == 0:
		signaloff1 = time.time()
		trig1.write(1)
         	time.sleep(0.00001)
        	trig1.write(0)		
	while echo1.read() == 1:
		signalon1 = time.time()

	timepassed1 = signalon1- signaloff1
	distance1 = timepassed1*17000
	print "this is distance1 :      %s" %distance1	
	if distance1 <= 43:
		return 1
	else:
		return 0

def get_exit():

        trig2.write(1)
        time.sleep(0.00001)
        trig2.write(0)

        while echo2.read() == 0:
                signaloff2 = time.time()
		trig2.write(1)
        	time.sleep(0.00001)
       		trig2.write(0)        

	while echo2.read() == 1:
                signalon2 = time.time()
        timepassed2 = signalon2- signaloff2
        distance2 = timepassed2*17000
	print "this is distance2 :     %s" %distance2
	
        if distance2 <=	43:
                return 2
        else:
                return 0


while True:

	outside = get_entry()	##returns 1 or 0
	inside = get_exit()	##returns 2 or 0
	
	if((inside==2 or outside==1) and (not (inside==2 and outside==1))):

		if (inside ==2):
			lastTrigger = inside
			print "Last trigger = %s " %lastTrigger
		else:
			lastTrigger = outside
			print "here Last trigger = %s " %lastTrigger
	else:
		lastTrigger = 0	
	time.sleep(0.6)
	
	if (lastTrigger != 0):
		if (firstTrigger != lastTrigger):
		
			print "GOING OUT!" 

		elif (firstTrigger == lastTrigger): 
			print "COMING IN!"		


	"""
	if(outside ==1 and inside == 0 and last_triggeredinside == 0):
		print "ENTRY"
		last_triggeredoutside = 1
		last_triggeredinside = 0
		time.sleep(0.6)

	if(outside ==0 and inside ==1 and last_triggeredoutside ==1):
		print "person still entering"
		last_triggeredoutside =0
		time.sleep(0.6)

	if(outside ==0 and inside == 1 and last_triggeredoutside == 0):
		print "EXIT"
		last_triggeredinside = 1
		last_triggeredoutside = 0
		time.sleep(0.6)

	if (outside ==1 and inside == 0 and last_triggeredinside == 1):
		print "person still exiting"
		last_triggeredinside = 0
		time.sleep(0.6)

#	if(outside ==1 and inside ==1):
#		print "ignore this condition"
#		last_triggeredinside,last_triggeredoutside = 0,0
#		time.sleep(0.6)
	
	else:
	#if(outside ==0 and inside ==0):
		print "no motion at all"
		#last_triggeredinside,last_triggeredoutside = 0,0
		time.sleep(0.6)
	
	if (get_entry()):
		ledin.write(1)
		ledout.write(0)
		print "ENTRY"
		time.sleep(0.6)
	
	if (get_exit()):
		ledin.write(0)
		ledout.write(1)
		print "EXIT"
		time.sleep(0.6)

	else:
		ledin.write(0)
		ledout.write(0)
		time.sleep(0.6)		
	"""



