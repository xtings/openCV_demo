import cv2 as cv
import numpy as np


def subtract_demo(m1, m2):
    dst = cv.subtract(m1, m2)
    cv.imshow("subtract_demo", dst)


def divide_demo(m1, m2):
    dst = cv.divide(m1, m2)
    cv.imshow("divide_demo", dst)


def multiply_demo(m1, m2):
    dst = cv.multiply(m1, m2)
    cv.imshow("multiply_demo", dst)


def others(m1, m2):
    im1, dev1 = cv.meanStdDev(m1)
    im2, dev2 = cv.meanStdDev(m2)
    print("image 1 "+str(im1))
    print("image 2 "+str(im2))
    print("image 1 dev " + str(dev1))
    print("image 2 dev" + str(dev2))


def logic_demo(m1, m2):
    dst = cv.bitwise_not(m1)
    cv.imshow("bitwise_not", dst)


def contrast_brightness_demo(image, c, b):
    h, w, ch = image.shape
    blank = np.zeros([h, w, ch], image.dtype)
    dst = cv.addWeighted(image, c, blank, 1-c, b)
    cv.imshow("con-bri-demo", dst)


src1 = cv.imread("binary.png")
src2 = cv.imread("test.png")
print(src1.shape)
print(src2.shape)
cv.namedWindow("input image1", cv.WINDOW_AUTOSIZE)
cv.imshow("input image1", src1)
cv.imshow("input image2", src2)

# others(src1, src2)
# add_demo(src1, src2)
# subtract_demo(src1, src2)
# divide_demo(src1, src2)
# multiply_demo(src1, src2)
# logic_demo(src1, src2)
contrast_brightness_demo(src2, 1.2, 10)
cv.waitKey(0)
cv.destroyAllWindows()