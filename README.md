# tiger-detector

### Included Folders:
- Cam_Project_1.1.zip
- Tiger-Face-Detector
- Cascade-Training

### Software Needed:
- CCS
- Homebrew
- Arduino
- Python
	-PIP
	-OpenCV

# DOWNLOADING FILES AND SCRIPTS

## CCS

Code Composer Studio is the main service that EE 107 (Fall 17-18) uses to program its boards.

If you haven't already downloaded and prepared it, here's the link:

http://www.ti.com/tool/CCSTUDIO

In Code Composer studio, you can import the relevant project file (named Cam_Project_1.1).

First, decompress the Cam_Project_1.1.zip and put it wherever you'd like.
Under the Project tab at the top, you'll see Import CCS Projects.
Navigate to whatever folder you downloaded this project into, and then you should be able to select the entire Cam_Project_1.1 file and import it into your CCS program.



## Homebrew

Homebrew is a service that allows MacOS users to download software from open source files online

To start, open up your terminal and make sure that you're in the source

I.e. your terminal's left side looks something like this:
DN51u4ou:~ jamesthieu23$

Just paste this into your terminal:
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"



## Python

Mac OS High Sierra should come with Python 2.7 out of the box
However, a lot of the code that I'm using is done via Python3 so we'll have to use that.
Download Python 3 with the following line in terminal:
brew install python3

Running a Python 3 script instead of a Python 2 script requires that you type "python3" instead of "python".
Ex.

python3 test_file.py
vs
python test_file.py



## PIP

PIP is a package manager for Python, meaning that it can download and manage different modules that you'll import into your Python files to use.

We'll need it for downloading OpenCV

PIP is fairly easy to install, just paste the following into terminal:
sudo easy_install pip



## OpenCV

OpenCV is an open source software that allows for many camera vision and machine learning functions.
It's extremely powerful, and this project only begins to scratch the surface of its potential.

There are MANY ways for you to install OpenCV, as can be found online
However, the most simple way I found was just to write the following into terminal:
pip install opencv-python

To use OpenCV in your python file, just type at the top of the file:
import cv2

From there, you'll have access to pretty much all the OpenCV functions
Make sure to check the OpenCV website for syntax and a manual!
https://docs.opencv.org/3.3.0/d1/dfb/intro.html



# RUNNING CAMERA SCRIPTS

## Downloading CCS Camera Script

For the CCS script to download onto the MSP430, there are a few steps that you should be fairly familiar with by this point as an EE 107 student.
First, make sure that your debugging module is plugged into your computer and that it connects to the MSP430 board such that the power status LED is on.
All you need to do to download the script is press Debug. (The symbol conveniently looks like a little green bug). At this point, it should go through a few messages that you can press OK through - it'll then begin downloading the project into the board.

When it looks like it's finished, check the console - if it says that there's a hardware breakpoint, press the green arrow to progress past that.
When you see the console say "LED Initialized", then you can press the STOP. 
At this point, it's safe to turn off CCS as the code is safely on the board.



## Running Motion Detection Script

For this part, you will need the MSP board with the code downloaded, the UART cable, and the debugger/power assembly.
Connect the board, UART, and debugger together and connect them to the computer.
Navigate to the Camera_Outputs folder.
Here, you'll find all the files relevant to getting the camera to take and download photos via UART.

To run the program, cd into the Camera_Outputs folder such that your terminal looks like: `DN0a2265b1:Camera_Outputs [YOUR_NAME_HERE]$`

Type: `gcc -o serial_stream serial_stream.c`

This file compiles your serial_stream.c, which manages your image outputs.

Find your board's serial number with the following:
1. Type the following in terminal:
system_profiler SPUSBDataType | grep "Serial Number" -B5
2. Look for USB UART
3. Copy the number after Serial Number
4. Type the following into terminal: `./serial_stream -t /dev/cu.usbserial-YOURSERIALNO`

You'll see the following:
`USB = 3`
`serial port open good`
`Synced`

At this point, if it takes a while to run, move around in front of the camera
You should see:
`IMG_1.png`
`Dumped`

You're good to go! Just move around in front of the camera to get more outputs like so:
Start of frame
`IMG_2.bmp`
`IMG_2.png`
`Dumped`

If the terminal stops on `Synced`, try pulling the power cable out and putting it back, then move around in front of it

At this point, you should be able to see your .bin and .png outputs being output into the Camera_Outputs file.
Adjust the camera as desired to get images focused at different ranges.

When you want to stop receiving images and disconnect the board and UART, press CTRL + C. This will end the program.

Feel free to look over the images - note, however, that most of them are corrupted.



# RUNNING OBJECT RECOGNITION SCRIPTS

## Training Object Detection

If you just want to work with the pre-trained files, feel free to ignore this section.

In this section, I drew heavily from the below two tutorials:
https://www.learnopencv.com/training-better-haar-lbp-cascade-eye-detector-opencv/
https://pythonprogramming.net/haar-cascade-object-detection-python-opencv-tutorial/

Look at the following for much more comprehensive documentation:
https://docs.opencv.org/3.3.0/dc/d88/tutorial_traincascade.html

For this part, you'll be working principally in the Cascade-Training folder. Here, you can train new cascade.xml files to detect whatever you'd like! (dogs, potatoes, etc.)

To train a motion detection machine learning software, you first have to decide on positive and negative images to train on.
Positive images are those that include your desired object. They should all be cropped into a uniform aspect ratio & size and only show what it is that you're looking for.
Negative images are those that do not include your desired object. They can be of any size and aspect ratio, but larger sizes take significantly longer to process.

I've already gone ahead and generated ~1600 800x800 negative images, so unless you want extreme precision, that set of negatives should be fine.



## There are two ways to generate positive images:
1. Superimposing a single positive on multiple negatives to generate images
2. Manually generate a set of unique positives

The first method is much faster, but requires significantly more training for accuracy on par with the second method.

### First Method:
0. CD into the Cascade-Training folder
1. In terminal:
	find ./negative_images -iname "*.jpg" > negatives.txt
This updates the negatives.txt file just in case you added some.
2. Add your cropped photo into the Cascade-Training folder
3. In terminal: `opencv_createsamples -img X.jpg -bg negatives.txt -info info/info.lst -pngoutput info -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num N`
This creates N number of positives where X.jpg is superimposed on the image. 
Make sure that N is less than the number of negatives - otherwise, the file won't generate positives past that.
4. In terminal: `opencv_createsamples -info info/info.lst -num N -w W -h H -vec positives.vec`
This creates a file positives.vec that is a vector file of all the positives to base the training cascade file off of.
N is the number of positives that you want to use to generate the positives.vec file.
W is the width of each sample - you can adjust this and the positive will be shifted to that width.
H is the height of each sample - you can adjust this and the positive will be shifted to that height.
W and H should be fairly small, as larger sizes lead to exponentially longer training times.

### Second Method:
0. Find N number of positive images.
1. Crop them so that they only show what you want to detect. They should all have the same dimensions.
2. Put these positive images into a folder "positives"
3. In terminal: `find ./negative_images -iname "*.jpg" > negatives.txt`
This updates the negatives.txt file just in case you added some.
4. In terminal:	`find ./positive_images -iname "*.jpg" > positives.txt`
This updates the positives.txt file to reflect your images.
5. In terminal:
	`perl bin/createsamples.pl positives.txt negatives.txt samples N "opencv_createsamples -bgcolor 0 -bgthresh 0 -maxxangle 1.1 -maxyangle 1.1 maxzangle 0.5 -maxidev 40 -w W -h H" `
This creates a file samples.vec that is a vector file of all the positives to base the training cascade file off of.
The samples will be dumped into the folder "samples".
6. In terminal:
	`python ./tools/mergevec.py -v samples/ -o samples.vec`
This creates a file samples.vec that is a vector file of all the positives to base the training cascade file off of.



## For training scripts, there are two methods:
1. Local Binary Patterns (LBP) Cascade
2. HAAR Cascade

### LBP:
The first method is significantly faster, but requires more training for decent accuracy than the second method.
For reference, training 12 stages with 250 positives and 150 negatives took ~2 hours using LBP.
In terminal:
	opencv_traincascade -data lbp -vec YOURVEC.vec -bg negatives.txt -numStages X -minHitRate 0.999 -maxFalseAlarmRate 0.5 -numPos P -numNeg N -w W -h H -mode ALL -precalcValBufSize 4096 -precalcIdxBufSize 4096 -featureType LBP

X is the number of stages through which to train. 10-20 is a good rule of thumb, but more stages require exponentially more time.
P is the number of positives on which to train. Again, more positives requires significantly more computation time.
N is the number of negatives on which to train. Similar computation issues as with positives.
W & H should match the W & H that you listed earlier for your .vec files.

If your computer hangs after this, try adjusted the BufSize variables down to 1024 or below.

### HAAR:
The second is much slower, but much more accurate.
Note: This method requires EXTREME computational power on higher input values. My MacBook Pro 2015 15" with 16 GB RAM almost crashed running it. As such, I have yet to successfully train using HAAR for significant input values, but it is said to sometimes require entire days to train.
In terminal:
	opencv_traincascade -data haar -vec YOURVEC.vec -bg negatives.txt -numStages X -minHitRate 0.999 -maxFalseAlarmRate 0.5 -numPos P -numNeg N -w W -h H -mode ALL -precalcValBufSize 4096 -precalcIdxBufSize 4096

X is the number of stages through which to train. 10-20 is a good rule of thumb, but more stages require exponentially more time.
P is the number of positives on which to train. Again, more positives requires significantly more computation time.
N is the number of negatives on which to train. Similar computation issues as with positives.
W & H should match the W & H that you listed earlier for your .vec files.

If your computer hangs after this, try adjusted the BufSize variables down to 1024 or below.



After doing these, you'll see a bunch of .xml files in either the haar or lbp folder, depending on which method you used.
The most important of these is the cascade.xml file.
Duplicate the cascade file and move the duplicate over to Tiger-Face-Detector.

The convention I use for naming these is METHOD_TRIAL_NUMPOS_NUMNEG for both folders and .xml files ported to Tiger-Face-Detector.


I drew heavily on certain resources for the following section:
https://www.pyimagesearch.com/2016/06/20/detecting-cats-in-images-with-opencv/

Running Object Detection

If you decided to train using a new cascade file, go into tiger_detector.py and change the cascade file loaded in lines 12-13.
`ap.add_argument("-c", "--cascade", default="YOURCASCADE.xml",`
Go ahead and also change some of the naming within the .py file to reflect whatever it is you're detecting.

To detect tigers, as we trained on, use the following in terminal: `python tiger_detector.py --image tigers/img1.jpg`
You can switch images between 1 and 5, or add as many as you'd like!

To detect your custom object, do as follows:
1. Create a new folder for your test images
2. Change the cascade file as above
3. In terminal: `python YOUR_DETECTOR.py --image FOLDER/img1.jpg`

In either case, you should see a popup with your test image and a red box telling you where your detected object is!
If it works, congrats!
Otherwise, you should look into building a new cascade.xml with increased input values.