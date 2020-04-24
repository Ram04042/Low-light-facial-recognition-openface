# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui5.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import os
import sys
import glob
import test
import vid_frame_cap
##import lbp_face_recognition
##import gabor_face_recognition
import numpy as np
import cv2
import os.path
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon




class Ui_MainWindow(object):

    def __init__(self):
        test.load_ram()
        #lbp_face_recognition.train()
        #gabor_face_recognition.train()
        self.path = None
        self.clahedpath = None
        self.match_path = None
        self.videopath = None
        self.count = None
        self.fd1 = None
        self.fd2 = None
        self.fd3 = None
        self.fd4 = None
        self.fd5 = None
        self.fd = None
        self.fdset = {}
       
        
        
    def selectimage_handler(self):
        print("Button pressed")
        self.open_dialog_box()
        
        
    def open_dialog_box(self):
        filename = QFileDialog.getOpenFileName()
        self.path = filename[0]
        print(self.path)
        self.clahedpath = None
        self.match_path = None
        self.setupUi(MainWindow)


    def selectvideofile(self):
        print("select video Button pressed")
        filename1 = QFileDialog.getOpenFileName()
        self.videopath = filename1[0]
        print(self.videopath)
        files = glob.glob('./faces_in_frames/*')
        for f in files:
            os.remove(f)
        self.setupUi(MainWindow)

    def extract_videofaces(self):
        print("Extract Video Faces Clicked")
        self.count=vid_frame_cap.extract_to_folder(self.videopath)
        print(self.count)
        self.setupUI(MainWindow)


    def findfacedetails(self):
        print("Find details Button pressed")
        self.fd = self.clahedpath
        print(self.fd)
        self.setupUi(MainWindow)



        
    def processClick(self):
        print("process clicked")
        img = cv2.imread(self.path)
        img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        img_yuv[:,:,0] = clahe.apply(img_yuv[:,:,0])
        image = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)
        cv2.imwrite('./clahe/clahe.jpeg',image)
        self.clahedpath = './clahe/clahe.jpeg'
        self.setupUi(MainWindow)
        
    def extractfaces_img(self):
        print("extractfaces clicked")
        self.match_path = test.match_pathpack(self.clahedpath)
        print(self.match_path)
        final_path = '5-celebrity-faces-dataset/train/'+self.match_path+'/1.jpeg'
        self.match_path = final_path
        self.setupUi(MainWindow)

    def recognize_faces_in_frames(self):
        imdir = './faces_in_frames'
        outputfolder='./clahed'

        if not os.path.exists(outputfolder): os.mkdir(outputfolder)
        images = [file for file in glob.glob('./faces_in_frames/*.jpg')]
        for index,image in enumerate(images):
            img = cv2.imread(image)
            img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
            clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
            img_yuv[:,:,0] = clahe.apply(img_yuv[:,:,0])
            output = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)
            #ye dono kaam karre hai wiener ya bm3d bhi blur hi karre the tu try karke dekh
            #output = cv2.bilateralFilter(output,9,75,75)
            #output = cv2.medianBlur(output,5)
            path2 = outputfolder + "/image_" +  str(index) + ".jpg"
            match_path = test.match_video(output)
            print(match_path)
            cv2.imwrite(path2,output)
            final_path = '5-celebrity-faces-dataset/train/'+self.match_path+'/1.jpeg'
            self.match_path = final_path

    
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1247, 710)

        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 500))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1227, 690))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(1300, 685))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")


        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_2.setSpacing(10)
        self.gridLayout_2.setObjectName("gridLayout_2")


        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")


        self.left = QtWidgets.QFrame(self.frame)
        self.left.setGeometry(QtCore.QRect(10, 0, 471, 681))
        self.left.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.left.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left.setObjectName("left")


        self.process = QtWidgets.QPushButton(self.left)
        self.process.setGeometry(QtCore.QRect(40, 340, 130, 30))
        self.process.setObjectName("process")


        self.extractfaces = QtWidgets.QPushButton(self.left)
        self.extractfaces.setGeometry(QtCore.QRect(50, 540, 130, 30))
        self.extractfaces.setObjectName("extractfaces")


        self.selectimage = QtWidgets.QPushButton(self.left)
        self.selectimage.setGeometry(QtCore.QRect(260, 0, 120, 30))
        self.selectimage.setObjectName("selectimage")


        self.extractfacesimg = QtWidgets.QLabel(self.left)
        self.extractfacesimg.setGeometry(QtCore.QRect(220, 460, 200, 200))
        self.extractfacesimg.setObjectName("extractfacesimg")
        self.extractfacesimg.setPixmap(QtGui.QPixmap(self.match_path))        
        self.extractfacesimg.setScaledContents(True)


        self.processimg = QtWidgets.QLabel(self.left)
        self.processimg.setGeometry(QtCore.QRect(220, 250, 200, 200))
        self.processimg.setObjectName("processimg")
        self.processimg.setPixmap(QtGui.QPixmap(self.clahedpath))        
        self.processimg.setScaledContents(True)


        self.selectimgimg = QtWidgets.QLabel(self.left)
        self.selectimgimg.setGeometry(QtCore.QRect(220, 40, 200, 200))
        self.selectimgimg.setObjectName("selectimgimg")
        self.selectimgimg.setPixmap(QtGui.QPixmap(self.path))        
        self.selectimgimg.setScaledContents(True)


        self.right = QtWidgets.QFrame(self.frame)
        self.right.setGeometry(QtCore.QRect(480, 0, 781, 331))
        self.right.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.right.setObjectName("right")


        self.selectvideotext = QtWidgets.QLineEdit(self.right)
        self.selectvideotext.setGeometry(QtCore.QRect(120, 10, 230, 30))
        self.selectvideotext.setObjectName("selectvideotext")
        self.selectvideotext.setText(self.videopath)


        self.totalfaces = QtWidgets.QLineEdit(self.right)
        self.totalfaces.setGeometry(QtCore.QRect(470, 10, 250, 30))
        self.totalfaces.setObjectName("totalfaces")
        self.totalfaces.setText(self.count)


        self.extractfaces_2 = QtWidgets.QPushButton(self.right)
        self.extractfaces_2.setGeometry(QtCore.QRect(360, 10, 100, 30))
        self.extractfaces_2.setObjectName("extractfaces_2")


        self.imgdisplay = QtWidgets.QScrollArea(self.right)
        self.imgdisplay.setGeometry(QtCore.QRect(10, 90, 711, 231))
        self.imgdisplay.setWidgetResizable(True)
        self.imgdisplay.setObjectName("imgdisplay")


        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imgdisplay.sizePolicy().hasHeightForWidth())


        self.imgdisplay.setSizePolicy(sizePolicy)
        self.imgdisplay.setMinimumSize(QtCore.QSize(0, 100))
        self.imgdisplay.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.imgdisplay.setWidgetResizable(True)
        self.imgdisplay.setObjectName("imgdisplay")


        self.scrollAreaWidgetContents_10 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_10.setGeometry(QtCore.QRect(0, 0, 709, 10018))
        self.scrollAreaWidgetContents_10.setObjectName("scrollAreaWidgetContents_10")


        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_10)
        self.gridLayout_3.setObjectName("gridLayout_3")


        self.frame_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents_10)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 10000))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")


        self.imgdisplay1 = QtWidgets.QLabel(self.frame_2)
        self.imgdisplay1.setGeometry(QtCore.QRect(10, 10, 200, 200))
        self.imgdisplay1.setObjectName("imgdisplay1")
        
        self.imgdisplay2 = QtWidgets.QLabel(self.frame_2)
        self.imgdisplay2.setGeometry(QtCore.QRect(240, 10, 200, 200))
        self.imgdisplay2.setObjectName("imgdisplay2")
        
        self.imgdisplay3 = QtWidgets.QLabel(self.frame_2)
        self.imgdisplay3.setGeometry(QtCore.QRect(460, 10, 200, 200))
        self.imgdisplay3.setObjectName("imgdisplay3")


        self.gridLayout_3.addWidget(self.frame_2, 0, 0, 1, 1)


        self.imgdisplay.setWidget(self.scrollAreaWidgetContents_10)


        self.extractuniquefaces = QtWidgets.QPushButton(self.right)
        self.extractuniquefaces.setGeometry(QtCore.QRect(290, 50, 130, 30))
        self.extractuniquefaces.setObjectName("extractuniquefaces")


        self.selectvideo = QtWidgets.QPushButton(self.right)
        self.selectvideo.setGeometry(QtCore.QRect(10, 10, 100, 30))
        self.selectvideo.setObjectName("selectvideo")


        self.bottom = QtWidgets.QFrame(self.frame)
        self.bottom.setGeometry(QtCore.QRect(480, 330, 781, 351))
        self.bottom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottom.setObjectName("bottom")


        self.detailimg = QtWidgets.QScrollArea(self.bottom)
        self.detailimg.setGeometry(QtCore.QRect(10, 50, 711, 291))
        self.detailimg.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.detailimg.setWidgetResizable(True)
        self.detailimg.setObjectName("detailimg")


        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 709, 10018))
        self.scrollAreaWidgetContents_2.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")


        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_4.setObjectName("gridLayout_4")


        self.frame_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 10000))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")


        self.fdimg1 = QtWidgets.QLabel(self.frame_3)
        self.fdimg1.setGeometry(QtCore.QRect(20, 20, 200, 200))
        self.fdimg1.setObjectName("fdimg1")
        self.fdimg1.setPixmap(QtGui.QPixmap(self.fd1))        
        self.fdimg1.setScaledContents(True)

        self.fdtxt1 = QtWidgets.QLabel(self.frame_3)
        self.fdtxt1.setGeometry(QtCore.QRect(20, 230, 201, 41))
        self.fdtxt1.setObjectName("fdtxt1")
        self.fdtxt1.setText(self.fd1)
        
        self.fdimg2 = QtWidgets.QLabel(self.frame_3)
        self.fdimg2.setGeometry(QtCore.QRect(240, 20, 200, 200))
        self.fdimg2.setObjectName("fdimg2")
        self.fdimg2.setPixmap(QtGui.QPixmap(self.fd2))        
        self.fdimg2.setScaledContents(True)

        self.fdtxt2 = QtWidgets.QLabel(self.frame_3)
        self.fdtxt2.setGeometry(QtCore.QRect(240, 230, 201, 41))
        self.fdtxt2.setObjectName("fdtxt2")
        self.fdtxt2.setText(self.fd2)
        
        self.fdimg3 = QtWidgets.QLabel(self.frame_3)
        self.fdimg3.setGeometry(QtCore.QRect(460, 20, 200, 200))
        self.fdimg3.setObjectName("fdimg3")
        self.fdimg3.setPixmap(QtGui.QPixmap(self.fd3))        
        self.fdimg3.setScaledContents(True)
                
        self.fdtxt3 = QtWidgets.QLabel(self.frame_3)
        self.fdtxt3.setGeometry(QtCore.QRect(460, 230, 201, 41))
        self.fdtxt3.setObjectName("fdtxt3")
        self.fdtxt3.setText(self.fd3)


        self.gridLayout_4.addWidget(self.frame_3, 0, 1, 1, 1)


        self.detailimg.setWidget(self.scrollAreaWidgetContents_2)


        self.finddetails = QtWidgets.QPushButton(self.bottom)
        self.finddetails.setGeometry(QtCore.QRect(310, 10, 101, 30))
        self.finddetails.setObjectName("finddetails")


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)


        self.scrollArea.setWidget(self.scrollAreaWidgetContents)


        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)


        MainWindow.setCentralWidget(self.centralwidget)


        self.retranslateUi(MainWindow)


        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        
        MainWindow.setWindowTitle(_translate("MainWindow", "Low Light Face Recognition"))
        
        self.process.setText(_translate("MainWindow", "Process"))
        self.process.clicked.connect(self.processClick)
        
        self.extractfaces.setText(_translate("MainWindow", "Extract Faces"))
        self.extractfaces.clicked.connect(self.extractfaces_img)

        self.selectimage.setText(_translate("MainWindow", "Selet Image"))
        self.selectimage.clicked.connect(self.selectimage_handler)
        
        self.extractfaces_2.setText(_translate("MainWindow", "Extract Faces"))
        self.extractfaces_2.clicked.connect(self.extract_videofaces)
        
        self.extractuniquefaces.setText(_translate("MainWindow", "Extract Unique Faces"))
        self.extractuniquefaces.clicked.connect(self.recognize_faces_in_frames)
        
        self.selectvideo.setText(_translate("MainWindow", "Select Video"))
        self.selectvideo.clicked.connect(self.selectvideofile)
        
        self.finddetails.setText(_translate("MainWindow", "Find Details"))
        self.finddetails.clicked.connect(self.findfacedetails)
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
