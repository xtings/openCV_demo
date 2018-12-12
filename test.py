#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 09:45:29 2018

@author: sxt
"""

import cv2 as cv
import numpy as np


def video_demo():
    # index, video path, size limit, no sound
    capture = cv.VideoCapture(0)
    while (True):
        ret, frame = capture.read()
        cv.flip(frame, 1)
        cv.imshow("video", frame)
        c = cv.waitKey(50)
        if c == 27:
            break


def extract_object_demo():
    capture =cv.VideoCapture("demo.mp4")
    while True:
        ret, frame = capture.read()
        if not ret:
            break
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        lower_hsv = np.array([37, 43, 46])
        upper_hsv = np.array([77, 255, 255])
        mask = cv.inRange(hsv, lower_hsv, upper_hsv)
        dst = cv.bitwise_and(frame, frame, mask=mask)
        cv.imshow("video", frame)
        cv.imshow("mask", dst)
        c = cv.waitKey(40)
        if c == 27:
            break


src = cv.imread("test.png")  # blue, green, red
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
# cv.imshow("input image", src)


cv.waitKey(0)
cv.destroyAllWindows()
