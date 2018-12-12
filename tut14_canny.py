import cv2 as cv
import numpy as np

def canny_demo(image):
    blur = cv.GaussianBlur(image, (3, 3), 0)
    gray = cv. cvtColor(blur, cv.COLOR_BGR2GRAY)
    grad_x = cv.Sobel(gray, cv.CV_16SC1, 1, 0)
    grad_y = cv.Sobel(gray, cv.CV_16SC1, 0, 1)
    edge = cv.Canny(grad_x, grad_y, 50, 150)
    dst = cv.bitwise_and(image, image, mask=edge)
    cv.imshow("edge", dst)

def line_detection(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    edges = cv.Canny(gray, 50, 150, apertureSize=3)
    cv.imshow("gray", edges)
    lines = cv.HoughLines(edges, 1, np.pi/180, 200)
    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * a)
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * a)
        cv.line(image, (x1, y1), (x2, y2), (255, 0 ,0), 2)
    cv.namedWindow("lines", cv.WINDOW_NORMAL)
    cv.imshow("lines", image)


def line_detection_possible_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    edges = cv.Canny(gray, 50, 150, apertureSize=3)
    lines = cv.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength= 50, maxLineGap= 10)
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
    cv.namedWindow("line_possible", cv.WINDOW_NORMAL)
    cv.imshow("line_possible", image)





src = cv.imread("line.jpg")
# line_detection(src)
line_detection_possible_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
