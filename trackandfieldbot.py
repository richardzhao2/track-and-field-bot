import numpy as np
import pyautogui
import PIL
import time
import sys
import cv2 as cv

"""
simple clicker bot to play Facebook messenger's 100m track and field
"""

def runBot():
	#just a bunch of constant coordinates
	BUTTON1_COORDINATE = (618, 812, 104, 100)
	BUTTON1_CENTER = (670,862)
	BUTTON2_LOCATION = (800,812)

	counter = 0
	pyautogui.PAUSE = 0.01 # rate at which the cursor oscillates
	
	running = True # game control
	raceStarted = False # if the actual race has started

	while(running==True and counter < 450):
		if (raceStarted == False):
			# Keep track of the image currently on the screen
			img1 = np.array(PIL.ImageGrab.grab(bbox=(462,169,912,972)).convert('RGB'))[:, :, ::-1].copy() 
			# Convert to grayscale to increase speed on locate functions
			template = cv.imread('images/go.png', 1)
			
			# Get the current similarity to the template
			res = cv.matchTemplate(img1,template,cv.TM_CCOEFF_NORMED)
			threshold = 0.85
			
			# Return image locatiosns where the threshold indeed fulfills
			loc = np.where(res >= threshold)
			for pt in zip(*loc[::-1]):
				if len(pt) != 0:
					raceStarted = True
					print("Detected Go")
		
		else:
			pyautogui.dragTo(670, 862, .1, button='left')
			pyautogui.dragTo(800, 812,.1,button='left')
			counter+=1

def main():
	print("Track and Field 100m Bot by Richard Zhao")
	print("Programmed specifically for 1920x1080p resolution")


	print("Starting bot...")
	runBot()


	print("Stopping bot...")
	sys.exit()


if __name__ == '__main__':
	main()

