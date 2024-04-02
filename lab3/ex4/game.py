# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'game.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(320, 258)
        MainWindow.setStyleSheet(u"background-color: rgb(85, 85, 127);\n"
"font: 16pt \"Segoe UI\";")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setEnabled(True)
        self.game = QWidget()
        self.game.setObjectName(u"game")
        self.verticalLayout = QVBoxLayout(self.game)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.CurrentAmount = QLabel(self.game)
        self.CurrentAmount.setObjectName(u"CurrentAmount")
        self.CurrentAmount.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.CurrentAmount)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.b1 = QPushButton(self.game)
        self.b1.setObjectName(u"b1")

        self.horizontalLayout.addWidget(self.b1)

        self.b2 = QPushButton(self.game)
        self.b2.setObjectName(u"b2")

        self.horizontalLayout.addWidget(self.b2)

        self.b3 = QPushButton(self.game)
        self.b3.setObjectName(u"b3")

        self.horizontalLayout.addWidget(self.b3)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.stackedWidget.addWidget(self.game)
        self.setup = QWidget()
        self.setup.setObjectName(u"setup")
        self.verticalLayout_2 = QVBoxLayout(self.setup)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.StartAmount = QLineEdit(self.setup)
        self.StartAmount.setObjectName(u"StartAmount")
        self.StartAmount.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.StartAmount)

        self.Start = QPushButton(self.setup)
        self.Start.setObjectName(u"Start")

        self.verticalLayout_2.addWidget(self.Start)

        self.stackedWidget.addWidget(self.setup)

        self.verticalLayout_3.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.CurrentAmount.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043c\u043d\u0435\u0439: 0", None))
        self.b1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.b2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.b3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.StartAmount.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043a\u0430\u043c\u043d\u0435\u0439", None))
        self.Start.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u0442\u044c", None))
    # retranslateUi

