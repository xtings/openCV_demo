import cv2 as cv


def pyramid_demo(image):
    level = 3
    temp = image.copy()
    pyramid_image = []
    for i in range(level):
        dst = cv.pyrDown(temp)
        pyramid_image.append(dst)
        cv.imshow("pyramid_demo_"+str(i), dst)
        temp = dst.copy()
    return pyramid_image

def lapalian_demo(image): # 报错了？？？？
    pyramid_images = pyramid_demo(image)
    level = len(pyramid_images)
    for i in range(level-1, -1, -1):
        if i-1 < 0:
            expand = cv.pyrUp(pyramid_images[i], dstsize=image.shape[:2])
            lpls = cv.subtract(image, expand)
            cv.imshow("lapalian_demo_"+str(i), lpls)
        else:
            expand = cv.pyrUp(pyramid_images[i], dstsize=pyramid_images[i-1].shape[:2])
            lpls = cv.subtract(pyramid_images[i-1], expand)
            cv.imshow("lapalian_demo_" + str(i), lpls)

src = cv.imread("view.png")
# pyramid_demo(src)
lapalian_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()

