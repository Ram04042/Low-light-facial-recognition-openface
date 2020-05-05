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
import test
import gui

from PyQt5 import QtCore,QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon

from PyQt5.QtCore import pyqtSignal

class MainUIClass(QtWidgets.QMainWindow,gui.Ui_MainWindow):
    def __init__(self,parent=None):
        super(MainUIClass,self).__init__(parent)
        test.load_ram()
        self.setupUi(self)
        self.path = None
        self.clahedpath = None
        self.match_path = None
        self.videopath = None
        self.count = None
        self.movingcord = 20
        self.textmovingcord = 20
        self.videoset = set()

        self.newvideoset = set()
        
        
        self.selectimage.clicked.connect(self.selectimage_handler)
        self.process.clicked.connect(self.processClick)
        self.extractfaces.clicked.connect(self.extractfaces_img)
        self.selectvideo.clicked.connect(self.selectvideofile)
        self.extractfaces_2.clicked.connect(self.extract_videofaces)
        self.processagain.clicked.connect(self.processagainclahe)
        self.extractuniquefaces.clicked.connect(self.extractuniquefaces_video)
        self.finddetails.clicked.connect(self.finddetailsfn)
        
        
        
        
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
        self.progressBar = QtWidgets.QProgressBar(self.right)
        self.progressBar.setGeometry(QtCore.QRect(470, 50, 231, 21))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")

        self.progressBar.show()
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


        self.threadclass = videorecog(files)
        self.threadclass.start()
        self.threadclass.update_videorecog.connect(self.update_videorecog)
        self.threadclass.update_percentage.connect(self.update_percentage)



    def update_videorecog(self,val):
        print(val)
        print("All faces Recognized")
        self.name1 = QtWidgets.QLabel(self.frame_2)
        self.name1.setGeometry(QtCore.QRect(self.textmovingcord, 170, 150, 30))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        self.name1.setFont(font)
        self.name1.setAlignment(QtCore.Qt.AlignCenter)

        self.name1.setObjectName("name1")
        self.name1.setText(val)
        self.name1.show()
        self.textmovingcord += 170
        temp = val.split()
        self.newvideoset.add(str(temp[0]))
        
        
        
        
        
            


    def extract_videofaces(self):
        print("Extract Video Faces Clicked")
        threadclass = ThreadClass(self.videopath)
        threadclass.start()
        threadclass.update_progressbar.connect(self.update_progressbar)
        print(self.count)


    def finddetailsfn(self):
        movcord = 20
        for names in self.newvideoset:
            print(names)
            f = '5-celebrity-faces-dataset/train/'+names+'/1.jpeg'
            self.fdimg1 = QtWidgets.QLabel(self.frame_3)
            self.fdimg1.setGeometry(QtCore.QRect(movcord, 20, 200, 200))
            self.fdimg1.setObjectName("fdimg1")
            self.fdimg1.setPixmap(QtGui.QPixmap(f))
            self.fdimg1.setScaledContents(True)
            self.fdimg1.show()


            self.fdtxt1 = QtWidgets.QLabel(self.frame_3)
            self.fdtxt1.setGeometry(QtCore.QRect(movcord, 230, 201, 30))
            font = QtGui.QFont()
            font.setFamily("MS Shell Dlg 2")
            font.setPointSize(10)
            font.setBold(True)
            self.fdtxt1.setFont(font)
            self.fdtxt1.setAlignment(QtCore.Qt.AlignCenter)
            
            self.fdtxt1.setObjectName("fdtxt1")
            self.fdtxt1.setText(names)
            self.fdtxt1.show()

            movcord += 220
            

            
            


    def update_progressbar(self,val):
        print("back to UI")
        print(val)
        self.count = val
        self.totalfaces.setText(str(int(val))+' faces detected in video')

    def update_percentage(self,percentage):
        self.progressBar.setValue(percentage)

class ThreadClass(QtCore.QThread):
    update_progressbar = pyqtSignal(float)

    def __init__(self,temp, parent=None):
        super(ThreadClass,self).__init__(parent)
        self.temp = temp

    def run(self):
        count = vid_frame_cap.extract_to_folder(self.temp)
        print("thread complete")
        self.update_progressbar.emit(count)



class videorecog(QtCore.QThread):
    update_videorecog = pyqtSignal(str)
    update_percentage = pyqtSignal(int)

    def __init__(self,files, parent=None):
        super(videorecog,self).__init__(parent)
        self.files = files
        self.matchvideoset = set()
        

    def run(self):
        print("video thread complete")
        textmovingcord = 20
        test.load_ram()
        den = len(self.files)
        num = 0
        
        for f in self.files:
            num += 1
            print(f)
            match = test.match_video(f)
            print(match)
            temp = match.split()
            
            print(temp[0]+"will be added in set")
            print(self.matchvideoset)
            self.matchvideoset.add(str(temp[0]))
            print("added in set")
            self.update_videorecog.emit(match)
            self.update_percentage.emit(int((num/den) * 100))
        





            
            






a = QtWidgets.QApplication(sys.argv)
app = MainUIClass()
app.show()
a.exec_()
