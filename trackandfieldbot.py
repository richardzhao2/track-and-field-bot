import numpy
import pyautogui
import PIL

"""
simple clicker bot to play Facebook messenger's 100m track and field
"""

img1 = PIL.ImageGrab.grab(bbox=(0,0,100,100))
print(img1)

counter = 0
pyautogui.PAUSE = 0.05

while(counter < 50):
	pyautogui.click(x=100, y=200)
	pyautogui.click(x=150, y=200)
	counter += 1
	print(counter)