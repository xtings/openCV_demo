import cv2 as cv
import numpy as np


def clamp(num):
    if num > 255:
        return 255
    if num < 0:
        return 0
    else:
        return num


def gaussian_noise(image):
    hei, wid, chan = image.shape
    for h in range(hei):
        for w in range(wid):
            b = image[h, w, 0]
            g = image[h, w, 1]
            r = image[h, w, 2]
            ran_num = np.random.normal(0, 20, 3)
            image[h, w, 0] = clamp(b + ran_num[0])
            image[h, w, 1] = clamp(g + ran_num[1])
            image[h, w, 2] = clamp(r + ran_num[2])
    cv.imshow("Gaussian_noise", image)



def blur_demo(image):
    dst = cv.blur(image, (30, 1)) # shuiping, chuizhi

    cv.imshow("blur_dest", dst)


def median_blur_demo(image):
    dst = cv.medianBlur(image, 5)
    cv.imshow("median_blur", dst)


def customer_blur_demo(image):
    # kernel = np.ones([5, 5], np.float32)/25
    # [0, -1, 0], [-1, 5, -1], [0, -1, 0]
    # [1, 1, 1], [1, 1, 1], [1, 1, 1]/9
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32)
    dst = cv.filter2D(image, -1, kernel)

    cv.imshow("customer_blur", dst)


src = cv.imread("view.png")
cv.namedWindow("input image1", cv.WINDOW_AUTOSIZE)
cv.imshow("input image1", src)
# blur_demo(src)
# median_blur_demo(src)
# customer_blur_demo(src)
gaussian_noise(src)
dst = cv.GaussianBlur(src, (5, 5), 0)
cv.imshow("Gaussian blur", dst)
cv.waitKey(0)
cv.destroyAllWindows()
