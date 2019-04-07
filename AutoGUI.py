# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 18:57:51 2019

@author: s.lagousis
"""

#Based on code from here 
# https://automatetheboringstuff.com/chapter18/

import pyautogui
width, height = pyautogui.size()

#for i in range(10):
#    pyautogui.moveTo(100, 100, duration=0.25)
#    pyautogui.moveTo(200, 100, duration=0.25)
#    pyautogui.moveTo(200, 200, duration=0.25)
#    pyautogui.moveTo(100, 200, duration=0.25)
    
#for i in range(10):
#    pyautogui.moveRel(100, 0, duration=0.25)
#    pyautogui.moveRel(0, 100, duration=0.25)
#    pyautogui.moveRel(-100, 0, duration=0.25)
#    pyautogui.moveRel(0, -100, duration=0.25)
    
#print(pyautogui.position())

rect = pyautogui.locateOnScreen('microphone.png')
pos = pyautogui.center(rect)
pyautogui.click(pos)
