# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(326, 278)
        MainWindow.setStyleSheet(u"background-color: rgb(102, 102, 102);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gl_tasks = QGridLayout()
        self.gl_tasks.setObjectName(u"gl_tasks")

        self.verticalLayout.addLayout(self.gl_tasks)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tb_ne_task = QLineEdit(self.centralwidget)
        self.tb_ne_task.setObjectName(u"tb_ne_task")

        self.horizontalLayout.addWidget(self.tb_ne_task)

        self.btn_new_task = QPushButton(self.centralwidget)
        self.btn_new_task.setObjectName(u"btn_new_task")
        font = QFont()
        font.setFamily(u"MRT_Nil 3")
        font.setPointSize(10)
        self.btn_new_task.setFont(font)

        self.horizontalLayout.addWidget(self.btn_new_task)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tb_n_t_d = QTextEdit(self.centralwidget)
        self.tb_n_t_d.setObjectName(u"tb_n_t_d")

        self.verticalLayout.addWidget(self.tb_n_t_d)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(150, 20))
        self.label.setMaximumSize(QSize(150, 20))
        font1 = QFont()
        font1.setFamily(u"MV Boli")
        font1.setPointSize(15)
        self.label.setFont(font1)
        self.label.setContextMenuPolicy(Qt.NoContextMenu)
        self.label.setAutoFillBackground(False)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(150, 20))
        self.label_2.setMaximumSize(QSize(150, 20))
        font2 = QFont()
        font2.setFamily(u"MV Boli")
        font2.setPointSize(15)
        font2.setItalic(False)
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_2)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.date = QLineEdit(self.centralwidget)
        self.date.setObjectName(u"date")

        self.horizontalLayout_2.addWidget(self.date)

        self.time = QLineEdit(self.centralwidget)
        self.time.setObjectName(u"time")

        self.horizontalLayout_2.addWidget(self.time)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(300, 20))
        self.label_3.setMaximumSize(QSize(300, 20))
        font3 = QFont()
        font3.setPointSize(15)
        self.label_3.setFont(font3)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)

        self.i_o_n = QLineEdit(self.centralwidget)
        self.i_o_n.setObjectName(u"i_o_n")

        self.verticalLayout.addWidget(self.i_o_n)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 326, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_new_task.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"insert data", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"insert time", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Important         or          Normal", None))
    # retranslateUi

