import cv2


def cap_demo():
    # 读取分类器文件
    face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_alt2.xml')
    # 打开摄像头 0为笔记本自带，1为外置摄像头
    capture = cv2.VideoCapture(0)

    while True:
        # 读取摄像头缓存
        ret, frame = capture.read()
        # 彩色转灰度
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # 开始多人脸识别
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        # 画方框
        for (x, y, w, h) in faces:
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 255), 2)
        # 显示图像
        cv2.imshow('frame', frame)
        # 按q退出
        if cv2.waitKey(1) == ord('q'):
            break


cap_demo()