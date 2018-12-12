import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def bi_demo(image):
    dst = cv.bilateralFilter(image, 0, 100, 15)
    cv.imshow("bi_demo", dst)


def shift_demo(image):
    dst = cv.pyrMeanShiftFiltering(image, 10, 50)
    cv.imwrite("ccc.jpeg", dst)
    cv.imshow("shift_demo", dst)


def plot_demo(image):
    plt.hist(image.ravel(), 256, [0, 256])
    plt.show()


def image_hist(image):
    color = ["b", "g", "r"]
    for i in range(len(color)):
        hist = cv.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(hist, color[i])
        plt.xlim([0, 256])
    plt.show()


def equalHist_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    dst = cv.equalizeHist(gray)
    cv.imshow("equalHist_demo", dst)


def clahe_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    clahe = cv.createCLAHE()
    dst = clahe.apply(gray)
    cv.imshow("clahe_demo", dst)


def create_rgb_hist(image):
    hei, wid, chan = image.shape
    rgbHist = np.zeros([16*16*16, 1], np.float32)
    bsize = 256/16
    for h in range(hei):
        for w in range(wid):
            b = image[h, w, 0]
            g = image[h, w, 1]
            r = image[h, w, 2]
            index = np.int(b/bsize)*16*16 + np.int(g/bsize)*16 + np.int(r/bsize)
            rgbHist[np.int(index), 0] += 1
    return rgbHist


def hist_compare(image1, image2):
    hist1 = create_rgb_hist(image1)
    hist2 = create_rgb_hist(image2)
    match1 = cv.compareHist(hist1, hist2, cv.HISTCMP_BHATTACHARYYA)
    match2 = cv.compareHist(hist1, hist2, cv.HISTCMP_CORREL)
    match3 = cv.compareHist(hist1, hist2, cv.HISTCMP_CHISQR)
    print(match1, match2, match3)

def hist2d_demo(image):
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    hist = cv.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
    plt.imshow(hist, interpolation="nearest")
    plt.title("hist2d_demo")
    plt.show()

def back_projection_demo():
    sample = cv.imread("view.png")
    target = cv.imread("target.png")
    sample_hsv = cv.cvtColor(sample, cv.COLOR_BGR2HSV)
    target_hsv = cv.cvtColor(target, cv.COLOR_BGR2HSV)
    cv.namedWindow("sample", cv.WINDOW_NORMAL)
    cv.imshow("sample", sample)
    cv.namedWindow("target", cv.WINDOW_NORMAL)
    cv.imshow("target", target)

    roiHist = cv.calcHist([target_hsv], [0, 1], None, [10, 10], [0, 180, 0, 256])
    cv.normalize(roiHist, roiHist, 0, 255, cv.NORM_MINMAX)
    dst = cv.calcBackProject([sample_hsv], [0, 1], roiHist, [0, 180, 0, 256], 1)
    cv.namedWindow("back_projection_demo", cv.WINDOW_NORMAL)

    cv.imshow("back_projection_demo", dst)


src = cv.imread("view.png")
cv.namedWindow("input image1", cv.WINDOW_AUTOSIZE)
cv.imshow("input image1", src)
# bi_demo(src)
# shift_demo(src)
# plot_demo(src)
# image_hist(src)
# clahe_demo(src)
# equalHist_demo(src)
hist2d_demo(src)
# back_projection_demo()
cv.waitKey(0)
cv.destroyAllWindows()