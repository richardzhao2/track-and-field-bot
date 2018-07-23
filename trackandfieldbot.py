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

	while(running==True and counter < 50):
		# Keep track of the image currently on the screen
		img1 = np.array(PIL.ImageGrab.grab(bbox=(400,120,1200,500)).convert('RGB'))[:, :, ::-1].copy() 
		# Convert to grayscale to increase speed on locate functions
		img_gray = cv.cvtColor(img1,cv.COLOR_BGR2GRAY)
		template = cv.imread('images/test.png',0)
		w,h = template.shape[::-1]
		
		# Get the current similarity to the template
		res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
		threshold = 0.7

		# Return image locations where the threshold indeed fulfills
		loc = np.where(res >= threshold)
		for pt in zip(*loc[::-1]):
			print(pt)

		cv.imshow('image',img1)
		cv.waitKey(10)
		
		#x, y = cv2.locateCenterOnScreen('images/go.png', grayscale=True, confidence=.8)
		#pyautogui.dragTo(670, 862, .1, button='left')
		#pyautogui.dragTo(800, 812,.1,button='left')
		counter+=1

	cv.destroyAllWindows()

def main():
	print("Track and Field 100m Bot by Richard Zhao")
	print("Programmed specifically for 1920x1080p resolution")
	
	#SELECT BOT MODE
	option = 1

	print("Starting bot...")
	
	runBot()


	print("Stopping bot...")
	sys.exit()


if __name__ == '__main__':
	main()

"""
img_rgb = cv2.imread('images/go.png')
template = cv2.imread('mario_coin.png') # need to replace with whatever screenshot
w, h = template.shape[:-1]

res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)"""