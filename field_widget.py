from PySide6.QtGui import QFont
from PySide6.QtWidgets import QWidget, QGridLayout

from cell_widget import CellWidget


class FieldWidget(QWidget):
    """Кастомный виджет для одной ячейки"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_fieldwidget()

    def init_fieldwidget(self):
        """Конструктор"""
        # фиксированный размер виджета
        self.setFixedSize(600, 600)  # ширина, высота

        # Словарь для хранения ссылок на виджеты ячеек
        self.cell_widgets = {}

        self.fieldLayout = QGridLayout()

        for i in range(81):
            widget = CellWidget()
            self.fieldLayout.addWidget(widget, i // 9, i % 9, 1, 1)
            self.cell_widgets[(i // 9, i % 9)] = widget

        # Устанавливаем layout для виджета
        self.setLayout(self.fieldLayout)


    def setItem(self, row, column, value):
        """Установка значения в ячейку"""
        self.cell_widgets[(row,column)].setValue(value)


    def clear(self):
        for key, item in self.cell_widgets.items():
            item.clear()


    def showNotes(self, is_visible):
        for key, item in self.cell_widgets.items():
            item.showNotes(is_visible)

    def setNotes(self, row, column, notes_list):
        self.cell_widgets[(row, column)].setNotes(notes_list)