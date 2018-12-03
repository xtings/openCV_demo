import cv2 as cv
import numpy as np

src = cv.imread("test.png")
print(src.shape)
cv.namedWindow("input image1", cv.WINDOW_AUTOSIZE)
cv.imshow("input image1", src)


face = src[50:250, 100:300]

gray = cv.cvtColor(face, cv.COLOR_BGR2GRAY)
backface = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
src[50:250, 100:300] = backface
cv.imshow("face", src)
cv.waitKey(0)
cv.destroyAllWindows()