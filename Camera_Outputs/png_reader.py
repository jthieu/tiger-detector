# This file processes the images as they come through serial_stream.c
# and generates copies of unique camera captures
# Make sure to uncomment this in serial_stream.c in order to use it


import png
import cv2
import time
import shutil
import sys

pic = open("output.png","rb") # Open output.png to look at

if (sys.argv[1] != ''): # If there's an input img_cnt, index the photo as such
    img_name = "IMG_"+sys.argv[1]+".png"
else:                   # If there's no img_cnt, index the photo as 1
    img_name = "IMG_"+str(1)+".png"
# If a later version output.png is not the same as pic,
# then copy it and label it with img_name
if (open("output.png","rb").read() != pic):
    shutil.copy("output.png",img_name)
    pic = open("output.png","rb")