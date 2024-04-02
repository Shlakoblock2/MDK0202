# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'flag.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(300, 400)
        MainWindow.setMinimumSize(QSize(300, 400))
        MainWindow.setMaximumSize(QSize(300, 400))
        MainWindow.setSizeIncrement(QSize(400, 500))
        MainWindow.setTabletTracking(False)
        MainWindow.setFocusPolicy(Qt.NoFocus)
        MainWindow.setStyleSheet(u"background-color: rgb(85, 85, 127);\n"
"font: 16pt \"Segoe UI\";")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.colors = QVBoxLayout()
        self.colors.setObjectName(u"colors")
        self.radioButton_5 = QRadioButton(self.centralwidget)
        self.radioButton_5.setObjectName(u"radioButton_5")
        self.radioButton_5.setAutoExclusive(False)

        self.colors.addWidget(self.radioButton_5)

        self.radioButton_8 = QRadioButton(self.centralwidget)
        self.radioButton_8.setObjectName(u"radioButton_8")
        self.radioButton_8.setAutoExclusive(False)

        self.colors.addWidget(self.radioButton_8)

        self.radioButton_4 = QRadioButton(self.centralwidget)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setAutoExclusive(False)

        self.colors.addWidget(self.radioButton_4)

        self.radioButton_7 = QRadioButton(self.centralwidget)
        self.radioButton_7.setObjectName(u"radioButton_7")
        self.radioButton_7.setAutoExclusive(False)

        self.colors.addWidget(self.radioButton_7)

        self.radioButton = QRadioButton(self.centralwidget)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setAutoExclusive(False)

        self.colors.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setAutoExclusive(False)

        self.colors.addWidget(self.radioButton_2)


        self.gridLayout.addLayout(self.colors, 0, 0, 1, 1)

        self.draw = QPushButton(self.centralwidget)
        self.draw.setObjectName(u"draw")

        self.gridLayout.addWidget(self.draw, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setStyleSheet(u"font: 8pt \"Segoe UI\";")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.radioButton_5.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0435\u043b\u044b\u0439 ", None))
        self.radioButton_8.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0438\u043d\u0438\u0439", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0440\u0430\u0441\u043d\u044b\u0439", None))
        self.radioButton_7.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0440\u0430\u043d\u0436\u0435\u0432\u044b\u0439", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0435\u043b\u0435\u043d\u044b\u0439", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0435\u0440\u043d\u044b\u0439", None))
        self.draw.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0440\u0438\u0441\u043e\u0432\u0430\u0442\u044c", None))
    # retranslateUi

