# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 885)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtCore.Qt.QLayout::SizeConstraint::SetDefaultConstraint)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.scan_btn = QtWidgets.QPushButton(self.centralwidget)
        self.scan_btn.setMinimumSize(QtCore.QSize(80, 40))
        self.scan_btn.setMaximumSize(QtCore.QSize(80, 40))
        self.scan_btn.setObjectName("scan_btn")
        self.horizontalLayout_2.addWidget(self.scan_btn)
        self.update_btn = QtWidgets.QPushButton(self.centralwidget)
        self.update_btn.setMinimumSize(QtCore.QSize(80, 40))
        self.update_btn.setMaximumSize(QtCore.QSize(80, 40))
        self.update_btn.setObjectName("update_btn")
        self.horizontalLayout_2.addWidget(self.update_btn)
        self.Btn = QtWidgets.QPushButton(self.centralwidget)
        self.Btn.setMinimumSize(QtCore.QSize(80, 40))
        self.Btn.setMaximumSize(QtCore.QSize(80, 40))
        self.Btn.setObjectName("Btn")
        self.horizontalLayout_2.addWidget(self.Btn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 33))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.menu.addAction(self.action)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Clamav Interface"))
        self.scan_btn.setText(_translate("MainWindow", "Scan"))
        self.update_btn.setText(_translate("MainWindow", "Update"))
        self.Btn.setText(_translate("MainWindow", "Unknown"))
        self.menu.setTitle(_translate("MainWindow", "帮助"))
        self.action.setText(_translate("MainWindow", "关于"))
