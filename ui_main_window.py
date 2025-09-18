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
from PySide6.QtWidgets import (QApplication, QHeaderView, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(802, 676)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.table = QTableWidget(self.centralwidget)
        if (self.table.columnCount() < 9):
            self.table.setColumnCount(9)
        if (self.table.rowCount() < 9):
            self.table.setRowCount(9)
        self.table.setObjectName(u"table")
        self.table.setGeometry(QRect(20, 10, 540, 540))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table.sizePolicy().hasHeightForWidth())
        self.table.setSizePolicy(sizePolicy)
        self.table.setMinimumSize(QSize(540, 540))
        self.table.setMaximumSize(QSize(540, 540))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.table.setFont(font)
        self.table.setAutoFillBackground(False)
        self.table.setStyleSheet(u"background: lightblue;\n"
"color: green;")
        self.table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.table.setCornerButtonEnabled(False)
        self.table.setRowCount(9)
        self.table.setColumnCount(9)
        self.table.horizontalHeader().setVisible(False)
        self.table.horizontalHeader().setMinimumSectionSize(60)
        self.table.horizontalHeader().setDefaultSectionSize(60)
        self.table.verticalHeader().setVisible(False)
        self.table.verticalHeader().setMinimumSectionSize(60)
        self.table.verticalHeader().setDefaultSectionSize(60)
        self.button_create = QPushButton(self.centralwidget)
        self.button_create.setObjectName(u"button_create")
        self.button_create.setGeometry(QRect(20, 560, 180, 60))
        self.button_hidden_pair = QPushButton(self.centralwidget)
        self.button_hidden_pair.setObjectName(u"button_hidden_pair")
        self.button_hidden_pair.setGeometry(QRect(590, 150, 180, 60))
        self.button_download = QPushButton(self.centralwidget)
        self.button_download.setObjectName(u"button_download")
        self.button_download.setGeometry(QRect(400, 560, 180, 60))
        self.button_save = QPushButton(self.centralwidget)
        self.button_save.setObjectName(u"button_save")
        self.button_save.setGeometry(QRect(210, 560, 180, 60))
        self.button_notes = QPushButton(self.centralwidget)
        self.button_notes.setObjectName(u"button_notes")
        self.button_notes.setGeometry(QRect(590, 560, 180, 60))
        self.button_single = QPushButton(self.centralwidget)
        self.button_single.setObjectName(u"button_single")
        self.button_single.setGeometry(QRect(590, 10, 180, 60))
        self.button_naked_pair = QPushButton(self.centralwidget)
        self.button_naked_pair.setObjectName(u"button_naked_pair")
        self.button_naked_pair.setGeometry(QRect(590, 80, 180, 60))
        self.button_naked_triple = QPushButton(self.centralwidget)
        self.button_naked_triple.setObjectName(u"button_naked_triple")
        self.button_naked_triple.setGeometry(QRect(590, 220, 180, 60))
        self.button_hidden_triple = QPushButton(self.centralwidget)
        self.button_hidden_triple.setObjectName(u"button_hidden_triple")
        self.button_hidden_triple.setGeometry(QRect(590, 290, 180, 60))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 802, 22))
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
        self.button_notes.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043c\u0435\u0442\u043a\u0438 \u044f\u0447\u0435\u0439\u043a\u0438", None))
        self.button_single.setText(QCoreApplication.translate("MainWindow", u"\"\u041e\u0434\u0438\u043d\u043e\u0447\u043a\u0438\"", None))
        self.button_naked_pair.setText(QCoreApplication.translate("MainWindow", u"\"\u0413\u043e\u043b\u044b\u0435 \u043f\u0430\u0440\u044b\"", None))
        self.button_naked_triple.setText(QCoreApplication.translate("MainWindow", u"\"\u0413\u043e\u043b\u044b\u0435 \u0442\u0440\u043e\u0439\u043a\u0438\"", None))
        self.button_hidden_triple.setText(QCoreApplication.translate("MainWindow", u"\"\u0421\u043a\u0440\u044b\u0442\u044b\u0435 \u0442\u0440\u043e\u0439\u043a\u0438\"", None))
    # retranslateUi

