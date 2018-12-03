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


def get_image_infor(image):
    print(type(image))
    # gao kuan shendu
    print(image.shape)
    print(image.size)
    print(image.dtype)
    pixel_data = np.array(image)
    print(pixel_data)


def access_pixels(image):
    print(image.shape)
    hei = image.shape[0]
    wid = image.shape[1]
    cha = image.shape[2]
    print(wid, hei, cha)
    for r in range(hei):
        for c in range(wid):
            for ch in range(cha):
                pv = image[r, c, ch]
                image[r, c, ch] = 255 - pv
    cv.imshow("pixel_demo", image)


def create_image():
    """
    img = np.zeros([400, 400, 3], np.uint8)
    img[:, :, 2] = np.ones([400, 400])*255
    cv.imshow("new image",img)

    img = np.zeros([400, 400, 1], np.uint8)
    img[:, :, 0] = np.ones([400, 400]) * 127
    cv.imshow("new image", img)
    """

    mt = np.ones([3,3], np.uint8)
    mt.fill(122.388)
    print(mt)


def inverse(image):
    dst = cv.bitwise_not(image)
    cv.imshow("inverse demo", dst)


def color_space_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imshow("gray image", gray)
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    cv.imshow("HSV image", hsv)
    his = cv.cvtColor(image, cv.COLOR_BGR2HLS)
    cv.imshow("HLS image", his)
    ycrcb = cv.cvtColor(image, cv.COLOR_BGR2YCrCb)
    cv.imshow("Ycrcb image", ycrcb)
    yuv = cv.cvtColor(image, cv.COLOR_BGR2YUV)
    cv.imshow("YUV image", yuv)


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





# flag = -1解码得到的方式，0单通道黑白，1彩色
src = cv.imread("test.png")  # blue, green, red
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
"""
b, g, r = cv.split(src)
cv.imshow("blue", b)
cv.imshow("green", g)
cv.imshow("red", r)
src[:,:,2] = 0

src = cv.merge([r, g, b])
cv.imshow("changed src", src)
t1 = cv.getTickCount()
"""
# access_pixels(src)
# create_image()
# inverse(src)
# color_space_demo(src)
extract_object_demo()
# t2 = cv.getTickCount()
# time = (t2 - t1) / cv.getTickFrequency()
# print("time period "+str(time * 1000))
# gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
# cv.imwrite("result.png", gray)
# video_demo()
cv.waitKey(0)
cv.destroyAllWindows()
