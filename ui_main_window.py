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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHeaderView, QLabel, QLayout, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1572, 877)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.table = QTableWidget(self.centralwidget)
        if (self.table.columnCount() < 9):
            self.table.setColumnCount(9)
        if (self.table.rowCount() < 9):
            self.table.setRowCount(9)
        self.table.setObjectName(u"table")
        self.table.setGeometry(QRect(790, 10, 540, 540))
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
        self.button_create.setGeometry(QRect(0, 770, 180, 60))
        self.button_hidden_pair = QPushButton(self.centralwidget)
        self.button_hidden_pair.setObjectName(u"button_hidden_pair")
        self.button_hidden_pair.setGeometry(QRect(1190, 710, 180, 60))
        self.button_download = QPushButton(self.centralwidget)
        self.button_download.setObjectName(u"button_download")
        self.button_download.setGeometry(QRect(380, 770, 180, 60))
        self.button_save = QPushButton(self.centralwidget)
        self.button_save.setObjectName(u"button_save")
        self.button_save.setGeometry(QRect(190, 770, 180, 60))
        self.button_notes = QPushButton(self.centralwidget)
        self.button_notes.setObjectName(u"button_notes")
        self.button_notes.setGeometry(QRect(570, 770, 180, 60))
        self.button_single = QPushButton(self.centralwidget)
        self.button_single.setObjectName(u"button_single")
        self.button_single.setGeometry(QRect(1190, 570, 180, 60))
        self.button_naked_pair = QPushButton(self.centralwidget)
        self.button_naked_pair.setObjectName(u"button_naked_pair")
        self.button_naked_pair.setGeometry(QRect(1190, 640, 180, 60))
        self.button_naked_triple = QPushButton(self.centralwidget)
        self.button_naked_triple.setObjectName(u"button_naked_triple")
        self.button_naked_triple.setGeometry(QRect(990, 560, 180, 60))
        self.button_hidden_triple = QPushButton(self.centralwidget)
        self.button_hidden_triple.setObjectName(u"button_hidden_triple")
        self.button_hidden_triple.setGeometry(QRect(990, 630, 180, 60))
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(790, 560, 191, 181))
        self.field_layout = QGridLayout(self.gridLayoutWidget)
        self.field_layout.setObjectName(u"field_layout")
        self.field_layout.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(50, 50))
        self.label_5.setFrameShape(QFrame.Box)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.field_layout.addWidget(self.label_5, 2, 0, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(50, 50))
        self.label_2.setFrameShape(QFrame.Box)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.field_layout.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(50, 50))
        self.label_3.setFrameShape(QFrame.Box)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.field_layout.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(50, 50))
        self.label_7.setFrameShape(QFrame.Box)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.field_layout.addWidget(self.label_7, 0, 2, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(50, 50))
        self.label_8.setFrameShape(QFrame.Box)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.field_layout.addWidget(self.label_8, 1, 2, 1, 1)

        self.label_10 = QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(50, 50))
        self.label_10.setFrameShape(QFrame.Box)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.field_layout.addWidget(self.label_10, 0, 1, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(15, 15))
        font1 = QFont()
        font1.setPointSize(8)
        self.label.setFont(font1)
        self.label.setFrameShape(QFrame.Box)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(15, 15))
        self.label_6.setFont(font1)
        self.label_6.setFrameShape(QFrame.Box)

        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)

        self.label_9 = QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(15, 15))
        self.label_9.setFont(font1)
        self.label_9.setFrameShape(QFrame.Box)

        self.gridLayout.addWidget(self.label_9, 1, 1, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(15, 15))
        self.label_4.setFont(font1)
        self.label_4.setFrameShape(QFrame.Box)

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.label_11 = QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(15, 15))
        self.label_11.setFont(font1)
        self.label_11.setFrameShape(QFrame.Box)

        self.gridLayout.addWidget(self.label_11, 1, 2, 1, 1)


        self.field_layout.addLayout(self.gridLayout, 1, 1, 1, 1)

        self.gridLayoutWidget_3 = QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(10, 0, 771, 681))
        self.gl = QGridLayout(self.gridLayoutWidget_3)
        self.gl.setSpacing(0)
        self.gl.setObjectName(u"gl")
        self.gl.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gl.setContentsMargins(0, 0, 0, 0)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(790, 760, 59, 59))
        self.gridLayout_2 = QGridLayout(self.layoutWidget)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.layoutWidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(15, 15))
        self.label_12.setFont(font1)
        self.label_12.setFrameShape(QFrame.Box)

        self.gridLayout_2.addWidget(self.label_12, 0, 0, 1, 1)

        self.label_13 = QLabel(self.layoutWidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(15, 15))
        self.label_13.setFont(font1)
        self.label_13.setFrameShape(QFrame.Box)

        self.gridLayout_2.addWidget(self.label_13, 2, 0, 1, 1)

        self.label_14 = QLabel(self.layoutWidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(15, 15))
        self.label_14.setFont(font1)
        self.label_14.setFrameShape(QFrame.Box)

        self.gridLayout_2.addWidget(self.label_14, 1, 1, 1, 1)

        self.label_15 = QLabel(self.layoutWidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(15, 15))
        self.label_15.setFont(font1)
        self.label_15.setFrameShape(QFrame.Box)

        self.gridLayout_2.addWidget(self.label_15, 1, 0, 1, 1)

        self.label_16 = QLabel(self.layoutWidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(15, 15))
        self.label_16.setFont(font1)
        self.label_16.setFrameShape(QFrame.Box)

        self.gridLayout_2.addWidget(self.label_16, 1, 2, 1, 1)

        self.button_a = QPushButton(self.centralwidget)
        self.button_a.setObjectName(u"button_a")
        self.button_a.setGeometry(QRect(500, 700, 71, 60))
        self.button_b = QPushButton(self.centralwidget)
        self.button_b.setObjectName(u"button_b")
        self.button_b.setGeometry(QRect(590, 700, 71, 60))
        self.button_c = QPushButton(self.centralwidget)
        self.button_c.setObjectName(u"button_c")
        self.button_c.setGeometry(QRect(680, 700, 71, 60))
        self.notes_box = QCheckBox(self.centralwidget)
        self.notes_box.setObjectName(u"notes_box")
        self.notes_box.setGeometry(QRect(30, 720, 171, 23))
        self.notes_box.setTristate(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1572, 22))
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
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.button_a.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.button_b.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.button_c.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.notes_box.setText(QCoreApplication.translate("MainWindow", u"\u043f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0437\u0430\u043c\u0435\u0442\u043a\u0438", None))
    # retranslateUi

