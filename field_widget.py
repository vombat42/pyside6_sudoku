from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QKeyEvent
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

        # Список для хранения ссылок на виджеты ячеек
        self.cell_widgets = list()

        self.fieldLayout = QGridLayout()

        for i in range(81):
            widget = CellWidget()
            widget.mousePressEvent = lambda event, idx=i: self.on_cell_clicked(event, idx)
            self.fieldLayout.addWidget(widget, i // 9, i % 9, 1, 1)
            self.cell_widgets.append(widget)

        # Устанавливаем layout для виджета
        self.setLayout(self.fieldLayout)

        # Текущая активная ячейка
        self.active_cell_index = None

        # Включаем отслеживание клавиш для всего виджета
        self.setFocusPolicy(Qt.StrongFocus)


    def get_cell_value(self, row, column):
        return self.cell_widgets[row * 9 + column].getValue()


    def on_cell_clicked(self, event, cell_index):
        """Обработчик клика по ячейке"""
        self.set_active_cell(cell_index)
        self.setFocus()  # Устанавливаем фокус на виджет


    def keyPressEvent(self, event: QKeyEvent):
        """Обработчик нажатия клавиш для виджета"""
        if self.active_cell_index is None:
            return
        key = event.key()
        text = event.text()
        # Обрабатываем разные типы клавиш
        if key in (Qt.Key_Delete, Qt.Key_Backspace) :
            self.cell_widgets[self.active_cell_index].clear()
        # elif key in (Qt.Key_1, Qt.Key_2, Qt.Key_3, Qt.Key_4, Qt.Key_5, Qt.Key_6, Qt.Key_7, Qt.Key_8, Qt.Key_9) :
        elif text in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
            self.cell_widgets[self.active_cell_index].setValue(text)
        elif key == Qt.Key_Up:
            self.set_active_cell(self.active_cell_index - 9)
        elif key == Qt.Key_Down:
            self.set_active_cell(self.active_cell_index + 9)
        elif key == Qt.Key_Left:
            if self.active_cell_index % 9 != 0:
                self.set_active_cell(self.active_cell_index - 1)
        elif key == Qt.Key_Right:
            if self.active_cell_index % 9 != 8:
                self.set_active_cell(self.active_cell_index + 1)


    def set_active_cell(self, index: int):
        if index > 80 or index < 0:
            return
        self.active_cell_index = index
        # Сбрасываем стиль всех Label
        for i, cell in enumerate(self.cell_widgets):
            if i == index:
                cell.setActive(True)
            else:
                cell.setActive(False)


    def setItem(self, row, column, value):
        """Установка значения в ячейку"""
        self.cell_widgets[row * 9 + column].setValue(value)


    def clear(self):
        for item in self.cell_widgets:
            item.clear()


    def showNotes(self, is_visible):
        for item in self.cell_widgets:
            item.showNotes(is_visible)

    def setNotes(self, row, column, notes_list):
        self.cell_widgets[row * 9 + column].setNotes(notes_list)