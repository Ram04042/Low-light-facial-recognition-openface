# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui5.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1250, 750)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 500))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1205, 685))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(1205, 685))
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
        self.process.setGeometry(QtCore.QRect(50, 280, 130, 30))
        self.process.setObjectName("process")
        
        self.extractfaces = QtWidgets.QPushButton(self.left)
        self.extractfaces.setGeometry(QtCore.QRect(50, 520, 130, 30))
        self.extractfaces.setObjectName("extractfaces")
        
        self.selectimage = QtWidgets.QPushButton(self.left)
        self.selectimage.setGeometry(QtCore.QRect(260, 0, 120, 30))
        self.selectimage.setObjectName("selectimage")
        
        self.extractfacesimg = QtWidgets.QLabel(self.left)
        self.extractfacesimg.setGeometry(QtCore.QRect(220, 440, 200, 180))
        self.extractfacesimg.setObjectName("extractfacesimg")
        
        self.processimg = QtWidgets.QLabel(self.left)
        self.processimg.setGeometry(QtCore.QRect(220, 240, 200, 180))
        self.processimg.setObjectName("processimg")
        
        self.selectimgimg = QtWidgets.QLabel(self.left)
        self.selectimgimg.setGeometry(QtCore.QRect(220, 40, 200, 180))
        self.selectimgimg.setObjectName("selectimgimg")


        self.processagain = QtWidgets.QPushButton(self.left)
        self.processagain.setGeometry(QtCore.QRect(50, 360, 131, 31))
        self.processagain.setObjectName("processagain")


        
        self.facename = QtWidgets.QLabel(self.left)
        self.facename.setGeometry(QtCore.QRect(220, 630, 201, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        self.facename.setFont(font)
        self.facename.setAlignment(QtCore.Qt.AlignCenter)
        self.facename.setObjectName("facename")


        
        
        self.right = QtWidgets.QFrame(self.frame)
        self.right.setGeometry(QtCore.QRect(480, 0, 781, 331))
        self.right.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.right.setObjectName("right")
        
        self.selectvideotext = QtWidgets.QLineEdit(self.right)
        self.selectvideotext.setGeometry(QtCore.QRect(120, 10, 230, 30))
        self.selectvideotext.setObjectName("selectvideotext")
        
        self.totalfaces = QtWidgets.QLineEdit(self.right)
        self.totalfaces.setGeometry(QtCore.QRect(470, 10, 250, 30))
        self.totalfaces.setObjectName("totalfaces")
        
        self.extractfaces_2 = QtWidgets.QPushButton(self.right)
        self.extractfaces_2.setGeometry(QtCore.QRect(360, 10, 100, 30))
        self.extractfaces_2.setObjectName("extractfaces_2")
        
        self.imgdisplay = QtWidgets.QScrollArea(self.right)
        self.imgdisplay.setGeometry(QtCore.QRect(10, 90, 711, 250))
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
        self.scrollAreaWidgetContents_10.setGeometry(QtCore.QRect(0, 0, 100000, 231))
        self.scrollAreaWidgetContents_10.setObjectName("scrollAreaWidgetContents_10")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_10)
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.frame_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents_10)
        self.frame_2.setMinimumSize(QtCore.QSize(10000, 0))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")



##        
##        self.name1 = QtWidgets.QLineEdit(self.frame_2)
##        self.name1.setGeometry(QtCore.QRect(20, 170, 150, 25))
##        self.name1.setObjectName("name1")






        
        
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
        self.detailimg.setGeometry(QtCore.QRect(10, 50, 711, 300))
        self.detailimg.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.detailimg.setWidgetResizable(True)
        self.detailimg.setObjectName("detailimg")
        
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0,10018, 709))
        self.scrollAreaWidgetContents_2.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        
        self.frame_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.frame_3.setMinimumSize(QtCore.QSize(10000,0))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        
        
        
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
        self.extractfaces.setText(_translate("MainWindow", "Extract Faces"))
        self.selectimage.setText(_translate("MainWindow", "Selet Image"))
        self.processagain.setText(_translate("MainWindow", "Process Again"))
        
        
        self.extractfaces_2.setText(_translate("MainWindow", "Extract Faces"))
        self.extractuniquefaces.setText(_translate("MainWindow", "Extract Unique Faces"))
        self.selectvideo.setText(_translate("MainWindow", "Select Video"))
        self.finddetails.setText(_translate("MainWindow", "Find Details"))
