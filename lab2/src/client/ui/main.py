# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(442, 612)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(200, 223, 210, 255), stop:1 rgba(186, 207, 195, 255));\n"
"font: 14pt;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.onoff = QPushButton(self.centralwidget)
        self.onoff.setObjectName(u"onoff")
        self.onoff.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout.addWidget(self.onoff)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.list = QListWidget(self.centralwidget)
        self.list.setObjectName(u"list")

        self.verticalLayout.addWidget(self.list)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.rand = QPushButton(self.centralwidget)
        self.rand.setObjectName(u"rand")

        self.horizontalLayout_2.addWidget(self.rand)

        self.play = QPushButton(self.centralwidget)
        self.play.setObjectName(u"play")

        self.horizontalLayout_2.addWidget(self.play)

        self.stop = QPushButton(self.centralwidget)
        self.stop.setObjectName(u"stop")

        self.horizontalLayout_2.addWidget(self.stop)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.onoff.setText(QCoreApplication.translate("MainWindow", u"on", None))
        self.rand.setText(QCoreApplication.translate("MainWindow", u"Rand", None))
        self.play.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.stop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
    # retranslateUi

