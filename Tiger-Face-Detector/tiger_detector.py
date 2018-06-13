# USAGE
# python tiger_detector.py --image tigers/img1.jpg

# Import the necessary packages
import argparse
import cv2
 
# Construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to the input image")
# I've included examples of cascades that I've tested
# Interestingly, lbp5_100_60 works better than lbp6_250_150
ap.add_argument("-c", "--cascade",
	#default="lbp2_200_350.xml",
    #default="lbp1_40_70.xml",
    #default="lbp3_15_30.xml",
    #default="lbp4_50_60.xml",
    default="lbp5_100_60.xml",
    #default="lbp6_250_150.xml",
	help="path to tiger detector LBP cascade")
args = vars(ap.parse_args())

# Load the input image and convert it to grayscale
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Load the tiger detector Haar cascade, then detect tiger faces
# In the input image
detector = cv2.CascadeClassifier(args["cascade"])
rects = detector.detectMultiScale(gray, scaleFactor=1.3,
	minNeighbors=10, minSize=(75, 75))

# Loop over the cat faces and draw a rectangle surrounding each
for (i, (x, y, w, h)) in enumerate(rects):
	cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
	cv2.putText(image, "Tiger #{}".format(i + 1), (x, y - 10),
		cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 2)

# Show the detected cat faces
cv2.imshow("Tiger Faces", image)
cv2.waitKey(0)