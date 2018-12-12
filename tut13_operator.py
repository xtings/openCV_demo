import cv2 as cv
import numpy as np


def lapalian_demo(image):
    kernel = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]]) # 四邻域与八邻域
    dst = cv.filter2D(image, cv.CV_32F, kernel)

    # dst = cv.Laplacian(image, cv.CV_32F)
    l = cv.convertScaleAbs(dst)
    cv.imshow("lapalcian_demo", l)

def sobel_demo(image):
    # cv.Scharr
    grad_x = cv.Sobel(image, cv.CV_32F, 1, 0)
    grad_y = cv.Sobel(image, cv.CV_32F, 0, 1)
    gradx = cv.convertScaleAbs(grad_x)
    grady = cv.convertScaleAbs(grad_y)
    cv.namedWindow("grad_x", cv.WINDOW_NORMAL)
    cv.imshow("grad_x", gradx)
    cv.namedWindow("grad_y", cv.WINDOW_NORMAL)
    cv.imshow("grad_y", grady)
    gradxy = cv.addWeighted(grad_x, 0.5, grad_y, 0.5, 0)
    cv.namedWindow("gradient", cv.WINDOW_NORMAL)
    cv.imshow("gradient", gradxy)

src = cv.imread("test.png")
lapalian_demo(src)
# sobel_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()