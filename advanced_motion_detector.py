import argparse
import datetime
import imutils
import time
import cv2

framerate = 20.0
videolength = 10

ap = argparse.ArgumentParser()
#ap.add_argument("-v","--video", help = "path to the video file")
ap.add_argument("-a", "--min-area", type = int, default = 200, help= "minimum area size")
args = vars(ap.parse_args())


#firstFrame = None
#camera = cv2.VideoCapture(0)
#time.sleep(0.25)
#avg = None
#count = 0
#sum = 0
#try:

def get_motion():

   firstFrame = None
   camera = cv2.VideoCapture(0)
#time.sleep(0.25)
   avg = None
   count = 0
   sum = 0
   
   instant_time = time.time()
   while (time.time()-instant_time <=10):
	(grabbed,frame) = camera.read()
	#text = "Unoccupied"
	#print "Fetching feed from Camera"
	if not grabbed:
		break

	frame = imutils.resize(frame, width = 480)

	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (21,21),0)	

	if avg is None:
		print "[INFO] Initialising Webcam..."
		print "[INFO] Starting Background Model..."
		avg = gray.copy().astype("float")
		continue

	cv2.accumulateWeighted(gray,avg,0.5)
	frameDelta = cv2.absdiff(gray,cv2.convertScaleAbs(avg))
#	print frameDelta.sum()
#	print frameDelta.shape	
	thresh = cv2.threshold(frameDelta,25,255,cv2.THRESH_BINARY)[1]
	thresh = cv2.dilate(thresh, None, iterations = 2)
	(cnts, _) = cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
	

	if not cnts:
	##list is empty##
		count =0
		#sum =0
		#print frameDelta.sum()
		#print "I HAVE NO IDEA WHAT WE'RE DOING"
	for c in cnts:
		if cv2.contourArea(c) <args["min_area"]:
			continue
			#print "unn"
		#text = "Occupied"
		#print "HUMAN DETECTED AHHHHHHHHHH!!!!" + str(count)
		sum=sum+frameDelta.sum()
		#count = count +1 
		#returned_sum = sum/count
		#print sum/count
		break	
	
	sum = sum+frameDelta.sum()
   value_data = int(sum/60000)	
   print (value_data)
   return value_data
   camera.release()
	
#except (KeyboardInterrupt):
#	camera.release()
#	exit


# cleanup the camera and close any open windows
#camera.release()


