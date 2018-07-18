import numpy
import pyautogui
import PIL
import time
import sys

"""
simple clicker bot to play Facebook messenger's 100m track and field
"""

img1 = PIL.ImageGrab.grab(bbox=(0,0,100,100))

BUTTON1_COORDINATE = (618, 812, 104, 100)
BUTTON1_CENTER = (670,862)
BUTTON2_LOCATION = (800,812)

counter = 0
pyautogui.PAUSE = 0.01
running = True
raceStarted = False

print("starting bot...")
time.sleep(3)
while(running==True and counter < 400):
	pyautogui.dragTo(670, 862, .1, button='left')
	pyautogui.dragTo(800, 812,.1,button='left')
	counter+=1

print("bot closing...")
sys.exit()
