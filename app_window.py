from PySide6.QtGui import QBrush, QColor
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QTableWidget

from delegate import DigitDelegate
from field import Field
from ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    """Главное окно приложения"""
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

        self.setWindowTitle("sudoku")

        # Устанавливаем кастомный делегат для всех ячеек
        self.table.setItemDelegate(DigitDelegate(self.table))

        # Подключаем сигнал завершения редактирования
        self.table.cellChanged.connect(self.on_cell_changed)

        self.button_create.setCheckable(True)
        self.button_create.clicked.connect(self.button_create_clicked)

        self.button_step.setCheckable(True)
        self.button_step.clicked.connect(self.button_step_clicked)

        # Создаем игровое поле
        self.field = Field()

    def on_cell_changed(self, row, column):
        """Обработчик изменения ячейки"""
        print('changed')
        item = self.table.item(row, column)
        if item and item.text() == '':
            self.field.clear_cell(row, column)
        if item and item.text():
            print(f"Ячейка [{row},{column}]: {item.text()}")
            if not self.field.set_cell_value(row, column, int(item.text())):
                item.setText('')


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
        item.setTextAlignment(4)
        self.table.setItem(0, 5, item)

