import psutil
import sys
import time
import os
import sys
import glob
import numpy as np
import cv2
import os.path

import vid_frame_cap
#import test
import gui

from PyQt5 import QtCore,QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon

from PyQt5.QtCore import pyqtSignal

class MainUIClass(QtWidgets.QMainWindow,gui.Ui_MainWindow):
    def __init__(self,parent=None):
        super(MainUIClass,self).__init__(parent)
        #test.load_ram()
        self.setupUi(self)
        self.path = None
        self.clahedpath = None
        self.match_path = None
        self.videopath = None
        self.count = None
        self.movingcord = 20
        
        self.selectimage.clicked.connect(self.selectimage_handler)
        self.process.clicked.connect(self.processClick)
        self.extractfaces.clicked.connect(self.extractfaces_img)
        self.selectvideo.clicked.connect(self.selectvideofile)
        self.extractfaces_2.clicked.connect(self.extract_videofaces)
        self.processagain.clicked.connect(self.processagainclahe)
        self.extractuniquefaces.clicked.connect(self.extractuniquefaces_video)
        
        
        
        #self.threadclass = ThreadClass(self.videopath)
        #self.threadclass.start()
        #self.threadclass.update_progressbar.connect(self.update_progressbar)

    def selectimage_handler(self):
        print("Button pressed")
        self.open_dialog_box()
        

    def open_dialog_box(self):
        filename = QFileDialog.getOpenFileName()
        self.path = filename[0]
        print(self.path)
        self.clahedpath = None
        self.match_path = None
        self.selectimgimg.setPixmap(QtGui.QPixmap(self.path))
        self.selectimgimg.setScaledContents(True)

        #resetting old image's process and extract
        self.processimg.setPixmap(QtGui.QPixmap(self.clahedpath))
        self.processimg.setScaledContents(True)
        self.extractfacesimg.setPixmap(QtGui.QPixmap(self.match_path))        
        self.extractfacesimg.setScaledContents(True)
        self.facename.setText(self.match_path)
        
        
        

        
        

    def processClick(self):
        print("process clicked")
        print("got path")
        print(self.path)
        img = cv2.imread(self.path)
        img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        img_yuv[:,:,0] = clahe.apply(img_yuv[:,:,0])
        image = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)
        cv2.imwrite('./clahe/clahe.jpeg',image)
        self.clahedpath = './clahe/clahe.jpeg'
        self.processimg.setPixmap(QtGui.QPixmap(self.clahedpath))
        self.processimg.setScaledContents(True)


    def processagainclahe(self):
        print("Process Again Button pressed")
        img = cv2.imread(self.clahedpath)
        img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        img_yuv[:,:,0] = clahe.apply(img_yuv[:,:,0])
        image = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)
        cv2.imwrite('./clahe/clahe.jpeg',image)
        self.clahedpath = './clahe/clahe.jpeg'
        self.processimg.setPixmap(QtGui.QPixmap(self.clahedpath))
        self.processimg.setScaledContents(True)

    def extractfaces_img(self):
        print("extractfaces clicked")
        self.match_path = test.match_pathpack(self.clahedpath)
        print(self.match_path)
        self.facename.setText(self.match_path)
        tempo = self.match_path.split()
        final_path = '5-celebrity-faces-dataset/train/'+tempo[0]+'/1.jpeg'
        name = tempo[0]
        self.match_path = final_path
        self.extractfacesimg.setPixmap(QtGui.QPixmap(self.match_path))        
        self.extractfacesimg.setScaledContents(True)
        

    def selectvideofile(self):
        print("select video Button pressed")
        filename1 = QFileDialog.getOpenFileName()
        self.videopath = filename1[0]
        print(self.videopath)
        files = glob.glob('./faces_in_frames/*')
        for f in files:
            os.remove(f)
        self.selectvideotext.setText(os.path.basename(self.videopath))


    def extractuniquefaces_video(self):
        #for i in range(20):
        print("Inside Extract Unique")
        path = './faces_in_frames/'
        files = []
        # r=root, d=directories, f = files
        for r, d, f in os.walk(path):
            for file in f:
                if '.jpg' in file:
                    files.append(os.path.join(r, file))

        for f in files:
            print(f)
            self.imgdisplay5 = QtWidgets.QLabel(self.frame_2)
            self.imgdisplay5.setGeometry(QtCore.QRect(self.movingcord, 10, 150, 150))
            self.imgdisplay5.setObjectName("imgdisplay5")
            self.imgdisplay5.setText("Working")
            self.imgdisplay5.show()
            self.movingcord += 170
            self.imgdisplay5.setPixmap(QtGui.QPixmap(f))
            self.imgdisplay5.setScaledContents(True)
            



        
        
        #I use the label to display an image.
        
        
            


    def extract_videofaces(self):
        print("Extract Video Faces Clicked")
        threadclass = ThreadClass(self.videopath)
        threadclass.start()
        threadclass.update_progressbar.connect(self.update_progressbar)
        print(self.count)


    def update_progressbar(self,val):
        print("back to UI")
        print(val)
        self.count = val
        self.totalfaces.setText(str(int(val))+' faces detected in video')


class ThreadClass(QtCore.QThread):
    update_progressbar = pyqtSignal(float)

    def __init__(self,temp, parent=None):
        super(ThreadClass,self).__init__(parent)
        self.temp = temp

    def run(self):
        count = vid_frame_cap.extract_to_folder(self.temp)
        print("thread complete")
        self.update_progressbar.emit(count)


a = QtWidgets.QApplication(sys.argv)
app = MainUIClass()
app.show()
a.exec_()
