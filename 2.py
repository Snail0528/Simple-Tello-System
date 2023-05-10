import sys
import pygame
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMainWindow
import pymongo
import cv2
import threading
from time import sleep
import mainwindowUI
import login
from PyQt5.QtWidgets import *
from djitellopy import tello
from pygame.locals import *
import numpy as np


class mainwindow(QMainWindow,mainwindowUI.Ui_MainWindow):
    def __init__(self):
        # 界面初始化
        QMainWindow.__init__(self)
        mainwindowUI.Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #设置线程
        self.stop_event_kbc = threading.Event()
        self.stop_event_ot = threading.Event()
        self.stop_event_ft = threading.Event()
        self.stop_event_openframe = threading.Event()
        self.thread_kbc = None
        self.thread_ft = None
        self.thread_ot = None
        self.thread_openframe = None

        #线程槽函数
        def run_kbc(self):
            if self.thread_ot and self.thread_ot.is_alive():
                self.stop_fun_ot()
            if self.thread_ft and self.thread_ft.is_alive():
                self.stop_fun_ft()
            if self.thread_openframe and self.thread_openframe.is_alive():
                self.stop_fun_openframe()
            self.thread_kbc = threading.Thread(target=self.kbc)
            self.stop_event_kbc.clear()
            self.thread_kbc.start()

        def run_ot(self):
            if self.thread_kbc and self.thread_kbc.is_alive():
                self.stop_fun_kbc()
            if self.thread_ft and self.thread_ft.is_alive():
                self.stop_fun_ft()
            if self.thread_openframe and self.thread_openframe.is_alive():
                self.stop_fun_openframe()
            self.thread_ot = threading.Thread(target=self.ot)
            self.stop_event_ot.clear()
            self.thread_ot.start()

        def run_ft(self):
            if self.thread_ot and self.thread_ot.is_alive():
                self.stop_fun_ot()
            if self.thread_kbc and self.thread_kbc.is_alive():
                self.stop_fun_kbc()
            if self.thread_openframe and self.thread_openframe.is_alive():
                self.stop_fun_openframe()
            self.thread_ft = threading.Thread(target=self.ft)
            self.stop_event_ft.clear()
            self.thread_ft.start()

        def run_openframe(self):
            if self.thread_ot and self.thread_ot.is_alive():
                self.stop_fun_ot()
            if self.thread_kbc and self.thread_kbc.is_alive():
                self.stop_fun_kbc()
            if self.thread_ft and self.thread_ft.is_alive():
                self.stop_fun_ft()
            self.thread_openframe = threading.Thread(target=self.openframe)
            self.stop_event_openframe.clear()
            self.thread_openframe.start()
        #结束线程
        def stop_fun_kbc(self):
            self.stop_event_kbc.set()

        def stop_fun_ot(self):
            self.stop_event_ot.set()

        def stop_fun_ft(self):
            self.stop_event_ft.set()

        def stop_fun_openframe(self):
            self.stop_event_openframe.set()

        # 主界面无人机对象
        self.mt = tello.Tello()
        self.mt.connect()
        self.mt.streamon()

        #无人机状态初始化
        self.battery = self.mt.get_battery()
        self.label_battery.setText('{}%'.format(self.battery))

        self.wifi = self.mt.query_wifi_signal_noise_ratio()
        self.label_wifi.setText('{}'.format(self.wifi))

        self.temperature = self.mt.get_temperature()
        self.label_temperature.setText('{}℃'.format(self.temperature))

    #物体跟踪
    def ot(self):
        global startCounter
        startCounter = 0
        while not self.stop_event_ot.is_set():
            self.mt.streamoff()
            self.mt.streamon()
            timer = cv2.getTickCount()
        # 从tello上获取图片
            frame_read = self.mt.get_frame_read()
            myframe = frame_read.frame
            img = cv2.resize(myframe, (self.imgwidth, self.imgheight))

            if cv2.waitKey(1) & 0xff == ord('t'):
            # tracker = cv2.legacy.TrackerMOSSE_create()   #快而不准
                self.tracker = cv2.TrackerCSRT_create()  # 慢而准
            # 截取屏幕获得（x,y,w,h）
                bbox = cv2.selectROI("Tracking", img, False)
                cv2.destroyAllWindows()
            # 使用第一帧和边界框初始化跟踪器
                self.tracker.init(img, bbox)
            succ, bbox = self.tracker.update(img)

            if succ:
                self.drawBox(img, bbox)
                self.tracking(img, bbox)
                display(img)
            else:
                cv2.putText(img, "Lost", (self.imgwidth - 120, 75), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 255), 2)
            ################# FLIGHT

            if startCounter == 0:
            # 起飞
                self.mt.takeoff()
                self.mt.send_rc_control(0, 0, 0, 0)
                sleep(0.5)
                self.mt.send_rc_control(0, 0, 50, 0)
                sleep(2)
                self.mt.send_rc_control(0, 0, 0, 0)
                startCounter = 1

            if dir == 1:
                self.mt.yaw_velocity = -self.speed
            elif dir == 2:
                self.mt.yaw_velocity = self.speed
            elif dir == 3:
                self.mt.up_down_velocity = self.speed
            elif dir == 4:
                self.mt.up_down_velocity = -self.speed
            elif dir1 == 1:
                self.mt.for_back_velocity = self.speed1
            elif dir1 == 2:
                self.mt.for_back_velocity = -self.speed1
            else:
                self.mt.left_right_velocity = 0
                self.mt.for_back_velocity = 0
                self.mt.up_down_velocity = 0
                self.mt.yaw_velocity = 0

            print(dir, dir1)
        # 把飞行的参数传给tello````
            if self.mt.send_rc_control:
                self.mt.send_rc_control(self.mt.left_right_velocity, self.mt.for_back_velocity, self.mt.up_down_velocity, self.mt.yaw_velocity)

            fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
            cv2.putText(img, 'fps:' + str(int(fps)), (self.imgwidth - 120, 40), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 255), 2)

            cv2.imshow("img", img)
            cv2.waitKey(2)
            if cv2.waitKey(1) == ord('q'):
                self.mt.land()
                break
            if cv2.getWindowProperty('img',cv2.WND_PROP_AUTOSIZE)<1:
                break
    def tracking(self,img,bbox):
        global dir,dir1
        dir = 0
        dir1 = 0
        x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
        area = w * h
        cx = int(x + (w / 2))  # CENTER X OF THE OBJECT
        cy = int(y + (h / 2))  # CENTER X OF THE OBJECT

        if (cx < int(self.frameimgwidth / 2) - self.deadZone):
            cv2.putText(img, " GO LEFT ", (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 3)
            cv2.rectangle(img, (0, int(self.frameimgheight / 2 - self.deadZone)),
                          (int(self.frameimgwidth / 2) - self.deadZone, int(self.frameimgheight / 2) + self.deadZone), (0, 0, 255),
                          cv2.FILLED)
            dir = 1
        elif (cx > int(self.frameimgwidth / 2) + self.deadZone):
            cv2.putText(img, " GO RIGHT ", (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 3)
            cv2.rectangle(img, (int(self.frameimgwidth / 2 + self.deadZone), int(self.frameimgheight / 2 - self.deadZone)),
                          (self.frameimgwidth, int(self.frameimgheight / 2) + self.deadZone), (0, 0, 255), cv2.FILLED)
            dir = 2
        elif (cy < int(self.frameimgheight / 2) - self.deadZone):
            cv2.putText(img, " GO UP ", (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 3)
            cv2.rectangle(img, (int(self.frameimgwidth / 2 - self.deadZone), 0),
                          (int(self.frameimgwidth / 2 + self.deadZone), int(self.frameimgheight / 2) - self.deadZone), (0, 0, 255),
                          cv2.FILLED)
            dir = 3
        elif (cy > int(self.frameimgheight / 2) + self.deadZone):
            cv2.putText(img, " GO DOWN ", (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 3)
            cv2.rectangle(img, (int(self.frameimgwidth / 2 - self.deadZone), int(self.frameimgheight / 2) + self.deadZone),
                          (int(self.frameimgwidth / 2 +self.deadZone), self.frameimgheight), (0, 0, 255), cv2.FILLED)
            dir = 4
        elif (area > self.AreaMax):
            cv2.putText(img, " GO BACK ", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 3)
            dir1 = 2
        elif (area < self.AreaMin):
            cv2.putText(img, " GO FORWARD ", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 3)
            dir1 = 1
        else:
            dir = 0
            dir1 = 0

        cv2.line(img, (int(self.frameimgwidth / 2), int(self.frameimgheight / 2)), (cx, cy), (0, 0, 255), 3)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 5)
        # cv2.putText(img, "Points: " + str(len(approx)), (x + w + 20, y + 20), cv2.FONT_HERSHEY_COMPLEX, .7,
        #             (0, 255, 0), 2)
        cv2.putText(img, "Area: " + str(int(area)), (x + w + 20, y + 45), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                    (0, 255, 0), 2)
        print(int(area))
        cv2.putText(img, " " + str(int(x)) + " " + str(int(y)), (x - 20, y - 45), cv2.FONT_HERSHEY_COMPLEX,
                    0.7, (0, 255, 0), 2)

    def display(self,img):
        cv2.line(img, (int(self.frameimgwidth / 2) - self.deadZone, 0), (int(self.frameimgwidth / 2) - self.deadZone, self.frameimgheight),
                 (255, 255, 0),
                 self.linethickness)
        cv2.line(img, (int(self.frameimgwidth / 2) + self.deadZone, 0), (int(self.frameimgwidth / 2) + self.deadZone, self.frameimgheight),
                 (255, 255, 0),
                 self.linethickness)
        cv2.circle(img, (int(self.frameimgwidth / 2), int(self.frameimgheight / 2)), 5, (0, 0, 255), 5)
        cv2.line(img, (0, int(self.frameimgheight / 2) - self.deadZone), (self.frameimgwidth, int(self.frameimgheight / 2) - self.deadZone),
                 (255, 255, 0),
                 self. linethickness)
        cv2.line(img, (0, int(self.frameimgheight / 2) + self.deadZone), (self.frameimgwidth, int(self.frameimgheight / 2) + self.deadZone),
                 (255, 255, 0),
                 self.linethickness)

    def drawBox(self,img,bbox):
        x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
        cv2.rectangle(img, (x, y), ((x + w), (y + h)), (255, 0, 255), 3, 1)
        cv2.putText(img, "Tracking", (self.imgwidth - 150, 75), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)
    #人脸跟踪
    def findFace(self,img):
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(imgGray, 1.2, 8)
        myFaceListC = []
        myFaceListArea = []
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cx = x + w // 2
            cy = y + h // 2
            area = w * h
            cv2.circle(img, (cx, cy), 5, (0, 255, 0), cv2.FILLED)
            myFaceListC.append([cx, cy])
            myFaceListArea.append(area)

        if len(myFaceListArea) != 0:
            i = myFaceListArea.index(max(myFaceListArea))
            return img, [myFaceListC[i], myFaceListArea[i]]
        else:
            return img, [[0, 0], 0]
    def trackFace(self,me,info,w,pid,pError):
        pError = 0
        area = info[1]
        x, y = info[0]
        fb = 0
        error = x - w // 2
        speed = pid[0] * error + pid[1] * (error - pError)
        speed = int(np.clip(speed, -100, 100))
        if area > self.fbRange[1]:
            fb = -20
        elif area < self.fbRange[0] and area != 0:
            fb = 20
        if area > self.fbRange[0] and area < self.fbRange[1]:
            fb = 0
        if x == 0:
            speed = 0
            error = 0
        me.send_rc_control(0, fb, 0, speed)
        return error
    def ft(self):
        global pError,startCounter1
        pError = 0
        startCounter1 = 0
        while not self.stop_event_ft.is_set():
            if startCounter1 == 0:
                self.mt.streamoff()
                self.mt.streamon()
                self.mt.takeoff()
                self.mt.send_rc_control(0, 0, 0, 0)
                sleep(0.5)
                self.mt.send_rc_control(0, 0, 60, 0)
                sleep(2)
                self.mt.send_rc_control(0, 0, 0, 0)
                startCounter1 = 1
            img = self.mt.get_frame_read().frame
            img = cv2.resize(img, (self.ftwidth, self.ftheight))
            img, info = self.findFace(img)
            pError = self.trackFace(self.mt, info, self.ftwidth, self.pid, pError)
            cv2.imshow("image", img)
            cv2.waitKey(1)
            if cv2.waitKey(1) == ord('q'):
                self.mt.land()
                break
            if cv2.getWindowProperty('image',cv2.WND_PROP_AUTOSIZE)<1:
                break
    #键盘控制
    def kbc_init(self):
        pygame.init()
        pygame.display.set_mode((400,400))

    def kbc_getKey(self,keyName):
        ans = False
        for eve in pygame.event.get():pass
        keyInput = pygame.key.get_pressed()
        myKey = getattr(pygame,'K_{}'.format(keyName))
        if keyInput[myKey]:
            ans = True
        pygame.display.update()
        return ans
    def kbc_getKeyboardInput(self):
        lr, fb, ud, yv = 0, 0, 0, 0
        speed = 50
        if self.kbc_getKey("LEFT"):
            yv = -speed
        elif self.kbc_getKey("RIGHT"):
            yv = speed
        if self.kbc_getKey("UP"):
            ud = speed
        elif self.kbc_getKey("DOWN"):
            ud = -speed
        if self.kbc_getKey("w"):
            fb = speed
        elif self.kbc_getKey("s"):
            fb = -speed
        if self.kbc_getKey("a"):
            lr = -speed
        elif self.kbc_getKey("d"):
            lr = speed

        if self.kbc_getKey("q"): self.mt.land()
        if self.kbc_getKey("e"): self.mt.takeoff()
        return [lr, fb, ud, yv]
    def kbc(self):
        while not self.stop_event_kbc.is_set():
            self.kbc_init()
            while True:
                vals=self.kbc_getKeyboardInput()
                self.mt.send_rc_control(vals[0], vals[1], vals[2], vals[3])
                sleep(0.05)
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
    def openframe(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_video)
        self.timer.start(50)

    def update_video(self):
        video_frame = self.mtmain.get_frame_read().frame
        video_frame = cv2.resize(video_frame, (511, 401), interpolation=cv2.INTER_AREA)
        video_frame = cv2.cvtColor(video_frame, cv2.COLOR_BGR2RGB)
            # 将opencv图像转换为Qt图像
        height, width, channel = video_frame.shape
        bytes_per_line = 3 * width
        qt_image = QImage(video_frame.data, width, height, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
        # 将qt图像显示在Qlabel上
        self.label_stream.setPixmap(QPixmap.fromImage(qt_image))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mainwindow()
    window.show()
    sys.exit(app.exec_())