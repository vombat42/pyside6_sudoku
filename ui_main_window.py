# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QLayout,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1011, 819)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.button_create = QPushButton(self.centralwidget)
        self.button_create.setObjectName(u"button_create")
        self.button_create.setGeometry(QRect(10, 700, 180, 60))
        self.button_hidden_pair = QPushButton(self.centralwidget)
        self.button_hidden_pair.setObjectName(u"button_hidden_pair")
        self.button_hidden_pair.setGeometry(QRect(800, 150, 180, 60))
        self.button_download = QPushButton(self.centralwidget)
        self.button_download.setObjectName(u"button_download")
        self.button_download.setGeometry(QRect(390, 700, 180, 60))
        self.button_save = QPushButton(self.centralwidget)
        self.button_save.setObjectName(u"button_save")
        self.button_save.setGeometry(QRect(200, 700, 180, 60))
        self.button_single = QPushButton(self.centralwidget)
        self.button_single.setObjectName(u"button_single")
        self.button_single.setGeometry(QRect(800, 10, 180, 60))
        self.button_naked_pair = QPushButton(self.centralwidget)
        self.button_naked_pair.setObjectName(u"button_naked_pair")
        self.button_naked_pair.setGeometry(QRect(800, 80, 180, 60))
        self.button_naked_triple = QPushButton(self.centralwidget)
        self.button_naked_triple.setObjectName(u"button_naked_triple")
        self.button_naked_triple.setGeometry(QRect(800, 220, 180, 60))
        self.button_hidden_triple = QPushButton(self.centralwidget)
        self.button_hidden_triple.setObjectName(u"button_hidden_triple")
        self.button_hidden_triple.setGeometry(QRect(800, 290, 180, 60))
        self.gridLayoutWidget_3 = QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(10, 10, 771, 681))
        self.gl = QGridLayout(self.gridLayoutWidget_3)
        self.gl.setSpacing(0)
        self.gl.setObjectName(u"gl")
        self.gl.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gl.setContentsMargins(0, 0, 0, 0)
        self.button_a = QPushButton(self.centralwidget)
        self.button_a.setObjectName(u"button_a")
        self.button_a.setGeometry(QRect(800, 450, 71, 60))
        self.button_b = QPushButton(self.centralwidget)
        self.button_b.setObjectName(u"button_b")
        self.button_b.setGeometry(QRect(800, 520, 71, 60))
        self.notes_box = QCheckBox(self.centralwidget)
        self.notes_box.setObjectName(u"notes_box")
        self.notes_box.setGeometry(QRect(800, 370, 171, 23))
        self.notes_box.setTristate(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1011, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.button_create.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        self.button_hidden_pair.setText(QCoreApplication.translate("MainWindow", u"\"\u0421\u043a\u0440\u044b\u0442\u044b\u0435 \u043f\u0430\u0440\u044b\"", None))
        self.button_download.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c", None))
        self.button_save.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.button_single.setText(QCoreApplication.translate("MainWindow", u"\"\u041e\u0434\u0438\u043d\u043e\u0447\u043a\u0438\"", None))
        self.button_naked_pair.setText(QCoreApplication.translate("MainWindow", u"\"\u0413\u043e\u043b\u044b\u0435 \u043f\u0430\u0440\u044b\"", None))
        self.button_naked_triple.setText(QCoreApplication.translate("MainWindow", u"\"\u0413\u043e\u043b\u044b\u0435 \u0442\u0440\u043e\u0439\u043a\u0438\"", None))
        self.button_hidden_triple.setText(QCoreApplication.translate("MainWindow", u"\"\u0421\u043a\u0440\u044b\u0442\u044b\u0435 \u0442\u0440\u043e\u0439\u043a\u0438\"", None))
        self.button_a.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.button_b.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.notes_box.setText(QCoreApplication.translate("MainWindow", u"\u043f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0437\u0430\u043c\u0435\u0442\u043a\u0438", None))
    # retranslateUi

