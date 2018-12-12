import cv2 as cv
import numpy as np


def erode_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    cv.namedWindow("binary", cv.WINDOW_NORMAL)
    cv.imshow("binary", binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (50, 50))
    dst = cv.erode(binary, kernel)
    cv.namedWindow("erode", cv.WINDOW_NORMAL)
    cv.imshow("erode", dst)


def dilate_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    cv.namedWindow("binary", cv.WINDOW_NORMAL)
    cv.imshow("binary", binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (50, 50))
    dst = cv.dilate(binary, kernel)
    cv.namedWindow("erode", cv.WINDOW_NORMAL)
    cv.imshow("erode", dst)

src = cv.imread("test.png")
kernel = cv.getStructuringElement(cv.MORPH_RECT, (15, 15))
dstn = cv.dilate(src, kernel)
cv.imshow("before", src)
cv.imshow("colorful", dstn)
# dilate_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
