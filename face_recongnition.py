import cv2
import sys
import time

def num_of_people():
	faces ={}
	# Get user supplied values
	video_capture = cv2.VideoCapture(0)
	#imagePath = sys.argv[1]
	cascPath = "default_face.xml"

	# Create the haar cascade
	faceCascade = cv2.CascadeClassifier(cascPath)

	# Read the image
	ret, frame = video_capture.read()
	#image = cv2.imread(imagePath)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# Detect faces in the image
	faces = faceCascade.detectMultiScale(
    		gray,
    		scaleFactor=1.1,
    		minNeighbors=6,
    		minSize=(30, 30),
    		flags = cv2.cv.CV_HAAR_SCALE_IMAGE
	)
	print "Found {0} faces!".format(len(faces))
	
# Draw a rectangle around the faces
#for (x, y, w, h) in faces:
#    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

#cv2.imshow("Faces found", image)
	video_capture.release()
	cv2.waitKey(0)
	return len(faces)
#while True:
#	num_of_people()
#	time.sleep(0.1)
