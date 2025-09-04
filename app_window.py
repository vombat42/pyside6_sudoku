from PySide6 import QtCore
from PySide6.QtCore import QSize
from PySide6.QtGui import QBrush, QColor
from PySide6.QtWidgets import QMainWindow, QPushButton, QTableWidgetItem, QTableWidget

from delegate import DigitDelegate
from ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    """ Главное окно приложения """
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

        self.setWindowTitle("sudoku")

        # Устанавливаем кастомный делегат для всех ячеек
        self.table.setItemDelegate(DigitDelegate(self.table))

        # Подключаем сигнал завершения редактирования
        self.table.cellChanged.connect(self.on_cell_changed)

        # item = QTableWidgetItem(self.table.item(8, 8))
        # item.setTextAlignment(QtCore.Qt.AlignCenter)

        self.button_create.setCheckable(True)
        self.button_create.clicked.connect(self.button_create_clicked)

        self.button_step.setCheckable(True)
        self.button_step.clicked.connect(self.button_step_clicked)

    def on_cell_changed(self, row, column):
        """Обработчик изменения ячейки"""
        item = self.table.item(row, column)
        if item and item.text():
            print(f"Ячейка [{row},{column}]: {item.text()}")


    def button_create_clicked(self):
        print("Clicked!")
        # Запрещаем редактирование всех ячеек
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.button_create.setDisabled(True)

    def button_step_clicked(self):
        print("Step!")
        self.button_create.setEnabled(True)
        item = QTableWidgetItem("2")
        item.setForeground(QBrush(QColor("blue")))
        self.table.setItem(0, 5, item)

        item2 = self.table(0, 7)
        item2.setForeground(QBrush(QColor("blue")))