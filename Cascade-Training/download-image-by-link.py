# Originally written by Harrison@pythonprogramming.net.
# This file grabs images from a URL link, then scales, grayscales, and names them
# The finished files are put in the 'neg' folder

import urllib.request
import cv2
import numpy as np
import os

def store_raw_images():
    neg_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n07942152'   
    neg_image_urls = urllib.request.urlopen(neg_images_link).read().decode()
    pic_num = 254 # Manually adjusted to easily index with preexisting negatives
    
    if not os.path.exists('neg'):
        os.makedirs('neg')
    
    # For each image in the url
    for i in neg_image_urls.split('\n'):
        try:
            print(i)
            urllib.request.urlretrieve(i, "neg/"+str(pic_num)+".jpg")
            img = cv2.imread("neg/"+str(pic_num)+".jpg",cv2.IMREAD_GRAYSCALE)
            # Should be larger than samples / pos pic (so we can place our image on it)
            resized_image = cv2.resize(img, (800, 800)) # Adjusted to 800x800 from 100x100
            cv2.imwrite("neg/img"+str(pic_num)+".jpg",resized_image)
            pic_num += 1
            
        except Exception as e:
            print(str(e))
            
store_raw_images()