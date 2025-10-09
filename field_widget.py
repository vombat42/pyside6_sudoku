from PySide6.QtCore import Qt, Signal, QRect
from PySide6.QtGui import QFont, QKeyEvent, QPainter, QPen
from PySide6.QtWidgets import QWidget, QGridLayout, QFrame, QLabel

from cell_widget import CellWidget


class FieldWidget(QWidget):
    """Кастомный виджет для одной ячейки"""
    # Сигнал изменения ячейки
    signal_cell_changed = Signal(dict)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_fieldwidget()

    def init_fieldwidget(self):
        """Конструктор"""
        self.color_lines = Qt.black
        self.color_lines = Qt.white
        self.size = 600
        # фиксированный размер виджета
        self.setFixedSize(self.size, self.size)  # ширина, высота

        # Список для хранения ссылок на виджеты ячеек
        self.cell_widgets = list()

        self.fieldLayout = QGridLayout()
        # self.fieldLayout.setSpacing(0)
        # self.fieldLayout.setContentsMargins(0,0,0,0)

        k = 0
        m = 0
        for i in range(81):

            widget = CellWidget()
            widget.mousePressEvent = lambda event, idx=i: self.on_cell_clicked(event, idx)
            if i == 27 or i == 54:
                space = QLabel()
                space.setFixedSize(10, 10)
                space.setText('*')
                # self.fieldLayout.addWidget(space, i // 9 + k, i % 9 + m, 1, 1)
                self.fieldLayout.addWidget(space)
                k += 1
            # if i == 3 or i == 6:
            if i % 3 == 0 and i != 0:
                space = QLabel()
                space.setFixedSize(10, 10)
                space.setText('+')
                # self.fieldLayout.addWidget(space, i // 9 + k, i % 9 + m, 1, 1)
                self.fieldLayout.addWidget(space)
                m += 1
            self.fieldLayout.addWidget(widget, i // 9 + k, i % 9 + m, 1, 1)
            self.cell_widgets.append(widget)

        # Устанавливаем layout для виджета
        self.setLayout(self.fieldLayout)

        # Текущая активная ячейка
        self.active_cell_index = None

        # Признак - идет процесс создания задачи или уже идет ее решение?
        self.is_being_solved = False

        # Включаем отслеживание клавиш для всего виджета
        self.setFocusPolicy(Qt.StrongFocus)


    def paintEvent(self, event):
        """Линии"""
        painter = QPainter(self)
        # толстые линии
        painter.setPen(QPen(self.color_lines, 4))
        s = self.size // 3
        # Горизонтальные линии
        painter.drawLine(0, 0, self.size, 0)
        # painter.drawLine(0, s, self.size, s)
        # painter.drawLine(0, s * 2, self.size, s * 2)
        painter.drawLine(0, self.size, self.size, self.size)
        # Вертикальные линии
        painter.drawLine(0, 0, 0, self.size)
        # painter.drawLine(s, 0, s, self.size)
        # painter.drawLine(s * 2, 0, s * 2, self.size)
        painter.drawLine(self.size, 0, self.size, self.size)

        # # тонкие линии
        # painter.setPen(QPen(self.color_lines, 1))
        # s = self.size // 9
        # # Горизонтальные линии
        # painter.drawLine(0, s, self.size, s)
        # painter.drawLine(0, s * 2, self.size, s * 2)
        # painter.drawLine(0, s * 4, self.size, s * 4)
        # painter.drawLine(0, s * 5, self.size, s * 5)
        # painter.drawLine(0, s * 7, self.size, s * 7)
        # painter.drawLine(0, s * 8, self.size, s * 8)
        # # Вертикальные линии
        # painter.drawLine(s , 0, s, self.size)
        # painter.drawLine(s * 2, 0, s * 2, self.size)
        # painter.drawLine(s * 4, 0, s * 4, self.size)
        # painter.drawLine(s * 5, 0, s * 5, self.size)
        # painter.drawLine(s * 7, 0, s * 7, self.size)
        # painter.drawLine(s * 8, 0, s * 8, self.size)


    def get_cell_value(self, row, column):
        return self.cell_widgets[row * 9 + column].getValue()

    def set_is_being_solved(self):
        self.is_being_solved = True

    def get_is_being_solved(self) -> bool:
        return self.is_being_solved

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
        if key == Qt.Key_Escape:
            self.set_active_cell(None)

        if key in (Qt.Key_Delete, Qt.Key_Backspace):
            # очистка ячейки возможна, если идет процесс задания условия задачи
            if not self.is_being_solved or self.cell_widgets[self.active_cell_index].getValue() == '':
                # передаем сигнал об очистке ячейки - словарь с ключами (row, column, new_value)
                self.signal_cell_changed.emit({'row': self.active_cell_index // 9,
                                               'column': self.active_cell_index % 9,
                                               'new_value': ''})
                self.cell_widgets[self.active_cell_index].clear()
        # elif key in (Qt.Key_1, Qt.Key_2, Qt.Key_3, Qt.Key_4, Qt.Key_5, Qt.Key_6, Qt.Key_7, Qt.Key_8, Qt.Key_9) :
        elif text in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
            # изменение ячейки возможно, если идет процесс задания условия задачи, или если ячейка еще не заполнена
            if not self.is_being_solved or self.cell_widgets[self.active_cell_index].getValue() == '':
                # передаем сигнал об изменении ячейки  - словарь с ключами (row, column, new_value)
                self.signal_cell_changed.emit({'row': self.active_cell_index // 9,
                                               'column': self.active_cell_index % 9,
                                               'new_value': text})
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
        if index != None and (index > 80 or index < 0):
            return
        if self.active_cell_index != None:
            self.cell_widgets[self.active_cell_index].setActive(False)
        # при index == None - нет активных ячеек
        if index != None:
            self.cell_widgets[index].setActive(True)
        self.active_cell_index = index


    def setValue(self, row, column, value):
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