import cv2 as cv
import numpy as np



def template_demo():
    tpl =cv.imread("tar.png")
    target = cv.imread("view.png")
    cv.namedWindow('template image', cv.WINDOW_NORMAL)
    cv.imshow("template image", tpl)
    cv.namedWindow('target image', cv.WINDOW_NORMAL)
    cv.imshow("target image", target)
    methods = [cv.TM_SQDIFF_NORMED, cv.TM_CCORR_NORMED, cv.TM_CCOEFF_NORMED]   #3种模板匹配方法
    th, tw = tpl.shape[:2]
    for md in methods:
        print(md)
        result = cv.matchTemplate(target, tpl, md)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        if md == cv.TM_SQDIFF_NORMED:
            tl = min_loc
        else:
            tl = max_loc
        br = (tl[0]+tw, tl[1]+th)   #br是矩形右下角的点的坐标
        cv.rectangle(target, tl, br, (255, 0, 0), 2)
        cv.namedWindow("match-" + np.str(md), cv.WINDOW_NORMAL)
        cv.imshow("match-" + np.str(md), target)

"""
def template_demo():
    tpl = cv.imread("view.png")
    target = cv.imread("tar.png")
    cv.namedWindow('template_demo', cv.WINDOW_NORMAL)
    cv.imshow("template_demo", tpl)
    cv.namedWindow('target_demo', cv.WINDOW_NORMAL)
    cv.imshow("target_demo", target)
    methods = [cv.TM_SQDIFF_NORMED, cv.TM_CCORR_NORMED, cv.TM_CCOEFF_NORMED]
    th, tw = tpl.shape[:2]
    for md in methods:
        print(md)
        result = cv.matchTemplate(target, tpl, md)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        if md == cv.TM_SQDIFF_NORMED:
            tl = min_loc
        else:
            tl = max_loc
        br = (tl[0]+tw, tl[1]+th)

        cv.rectangle(tpl, tl, br, (255, 0, 0), 2)
        cv.namedWindow("match_"+ np.str(md), cv.WINDOW_NORMAL)
        cv.imshow("match_"+ np.str(md), tpl)
        """

template_demo()
cv.waitKey(0)
cv.destroyAllWindows()