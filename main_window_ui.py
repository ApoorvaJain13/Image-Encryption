# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_Window.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets, QtWidgets, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(465, 417)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        spacerItem = QtWidgets.QSpacerItem(17, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.imageLabel = QtWidgets.QLabel(self.centralwidget)
        self.imageLabel.setObjectName(_fromUtf8("imageLabel"))
        self.verticalLayout_2.addWidget(self.imageLabel)
        spacerItem1 = QtWidgets.QSpacerItem(442, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(442, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(442, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem4 = QtWidgets.QSpacerItem(78, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.labelOption = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.labelOption.setFont(font)
        self.labelOption.setFocusPolicy(QtCore.Qt.NoFocus)
        self.labelOption.setObjectName(_fromUtf8("labelOption"))
        self.horizontalLayout_4.addWidget(self.labelOption)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem6)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem7)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem8)
        self.labelEncrpyt = QtWidgets.QLabel(self.centralwidget)
        self.labelEncrpyt.setObjectName(_fromUtf8("labelEncrpyt"))
        self.horizontalLayout.addWidget(self.labelEncrpyt)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem9)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem10)
        self.buttonEncrypt_2 = QtWidgets.QPushButton(self.centralwidget)
        self.buttonEncrypt_2.setFocusPolicy(QtCore.Qt.TabFocus)
        self.buttonEncrypt_2.setObjectName(_fromUtf8("buttonEncrypt_2"))
        self.horizontalLayout.addWidget(self.buttonEncrypt_2)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem11)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem12)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem13)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem14)
        self.labelDecrypt = QtWidgets.QLabel(self.centralwidget)
        self.labelDecrypt.setObjectName(_fromUtf8("labelDecrypt"))
        self.horizontalLayout_2.addWidget(self.labelDecrypt)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem15)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem16)
        self.buttonDecrypt_2 = QtWidgets.QPushButton(self.centralwidget)
        self.buttonDecrypt_2.setObjectName(_fromUtf8("buttonDecrypt_2"))
        self.horizontalLayout_2.addWidget(self.buttonDecrypt_2)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem17)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem18)
        spacerItem19 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem19)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem20)
        self.labelWatermark = QtWidgets.QLabel(self.centralwidget)
        self.labelWatermark.setObjectName(_fromUtf8("labelWatermark"))
        self.horizontalLayout_3.addWidget(self.labelWatermark)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem21)
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem22)
        self.buttonWatermark = QtWidgets.QPushButton(self.centralwidget)
        self.buttonWatermark.setObjectName(_fromUtf8("buttonWatermark"))
        self.horizontalLayout_3.addWidget(self.buttonWatermark)
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem23)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 465, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFilr = QtWidgets.QMenu(self.menubar)
        self.menuFilr.setObjectName(_fromUtf8("menuFilr"))
        self.menuNetwork = QtWidgets.QMenu(self.menubar)
        self.menuNetwork.setObjectName(_fromUtf8("menuNetwork"))
        MainWindow.setMenuBar(self.menubar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setIconVisibleInMenu(False)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionSend_File = QtWidgets.QAction(MainWindow)
        self.actionSend_File.setObjectName(_fromUtf8("actionSend_File"))
        self.actionReceive_File = QtWidgets.QAction(MainWindow)
        self.actionReceive_File.setObjectName(_fromUtf8("actionReceive_File"))
        self.actionSend_RSA_Public_Key = QtWidgets.QAction(MainWindow)
        self.actionSend_RSA_Public_Key.setObjectName(_fromUtf8("actionSend_RSA_Public_Key"))
        self.menuFilr.addAction(self.actionQuit)
        self.menuNetwork.addAction(self.actionSend_File)
        self.menuNetwork.addSeparator()
        self.menuNetwork.addAction(self.actionReceive_File)
        self.menuNetwork.addSeparator()
        self.menuNetwork.addAction(self.actionSend_RSA_Public_Key)
        self.menubar.addAction(self.menuFilr.menuAction())
        self.menubar.addAction(self.menuNetwork.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Encrypto", None))
        self.imageLabel.setText(_translate("MainWindow", "TextLabel", None))
        self.labelOption.setText(_translate("MainWindow", "Select the Option", None))
        self.labelEncrpyt.setText(_translate("MainWindow", "1. Encrypt Image", None))
        self.buttonEncrypt_2.setText(_translate("MainWindow", "Encrypt", None))
        self.labelDecrypt.setText(_translate("MainWindow", "2. Decrypt Image", None))
        self.buttonDecrypt_2.setText(_translate("MainWindow", "Decrypt", None))
        self.labelWatermark.setText(_translate("MainWindow", " 3. Add Watermark", None))
        self.buttonWatermark.setText(_translate("MainWindow", "Watermark", None))
        self.menuFilr.setTitle(_translate("MainWindow", "File", None))
        self.menuNetwork.setTitle(_translate("MainWindow", "Network", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q", None))
        self.actionSend_File.setText(_translate("MainWindow", "Send File", None))
        self.actionReceive_File.setText(_translate("MainWindow", "Receive File", None))
        self.actionSend_RSA_Public_Key.setText(_translate("MainWindow", "Send RSA Public Key ", None))

