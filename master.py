#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 14:42:47 2021

@author: panshiyun
"""
import cv2  
import numpy
import matplotlib.pyplot as plot

cap = cv2.VideoCapture(0)
print('Hello2')

#while(1):
    # get a frame
   # ret, frame = cap.read()
    # show a frame
   # cv2.imshow("capture", frame)
   # if cv2.waitKey(1) & 0xFF == ord('q'):
#        break


cap.release()
cv2.destroyAllWindows() 

print("Hellow")

