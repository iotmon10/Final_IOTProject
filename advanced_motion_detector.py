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

def get_motion():

   firstFrame = None
   camera = cv2.VideoCapture(0)
   avg = None
   count = 0
   sum = 0
   
   instant_time = time.time()
   while (time.time()-instant_time <=10):
	(grabbed,frame) = camera.read()
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
	thresh = cv2.threshold(frameDelta,25,255,cv2.THRESH_BINARY)[1]
	thresh = cv2.dilate(thresh, None, iterations = 2)
	(cnts, _) = cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
	

	if not cnts:
	##list is empty##
		count =0
	for c in cnts:
		if cv2.contourArea(c) <args["min_area"]:
			continue
		sum=sum+frameDelta.sum()
		break	
	
	sum = sum+frameDelta.sum()
   value_data = int(sum/20000)	
   print (value_data)
   return value_data
   camera.release()
	



