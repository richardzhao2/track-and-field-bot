import numpy
import pyautogui
import PIL

"""
simple clicker bot to play Facebook messenger's 100m track and field
"""

img1 = PIL.ImageGrab.grab(bbox=(0,0,100,100))
print(img1)


pyautogui.moveTo(0, 50)