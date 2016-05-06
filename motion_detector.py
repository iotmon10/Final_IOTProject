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


#grab camera
#camera = cv2.VideoCapture(0)

#fourcc = cv2.cv.CV_FOURCC(*'XVID')
#out = cv2.VideoWriter('myvideo.avi', fourcc,framerate,(640,480))

#for i in range (int(videolength*framerate)):
#	if (camera.isOpened()):
#		ret, frame = camera.read()
#		if ret ==True:
#			out.write(frame)
#		else:
#			continue

#camera.release()
#out.release()

#videointake = cv2.VideoCapture(args["video"])

firstFrame = None
camera = cv2.VideoCapture(0)
time.sleep(0.25)
avg = None

try:
   while True:
	(grabbed,frame) = camera.read()
	#text = "Unoccupied"
	#print "Fetching feed from Camera"
	if not grabbed:
		break

	frame = imutils.resize(frame, width = 480)

	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (21,21),0)

#	if firstFrame is None:
#		firstFrame = gray
#		continue	

	if avg is None:
		print "[INFO] Starting Backgrond Model..."
		avg = gray.copy().astype("float")
		continue

	cv2.accumulateWeighted(gray,avg,0.5)
	frameDelta = cv2.absdiff(gray,cv2.convertScaleAbs(avg))
	

	#frameDelta = cv2.absdiff(firstFrame, gray)
	#thresh = cv2.threshold(frameDelta,25,255,cv2.THRESH_BINARY)[1]

	thresh = cv2.dilate(thresh, None, iterations = 2)
	(cnts, _) = cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)

	for c in cnts:
		if cv2.contourArea(c) <args["min_area"]:
			continue

#		(x,y,w,h) = cv2.boundingRect(c)
#		cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255, 0),2)
		#text = "Occupied"
		print "HUMAN DETECTED AHHHHHHHHHH!!!!"
		break	

#	cv2.putText(frame, "Room Status: {}".format(text), (10, 20),
#		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
#	cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
#		(10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

	# show the frame and record if the user presses a key
#	cv2.imshow("Security Feed", frame)
#	cv2.imshow("Thresh", thresh)
#	cv2.imshow("Frame Delta", frameDelta)
#	key = cv2.waitKey(1) & 0xFF

	# if the `q` key is pressed, break from the lop
#	if key == ord("q"):
#		break
except (KeyboardInterrupt):
	camera.release()
	exit


# cleanup the camera and close any open windows
#camera.release()

