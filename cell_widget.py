from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QWidget, QLabel, QGridLayout, QStackedLayout


class CellWidget(QWidget):
    """Кастомный виджет для одной ячейки"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_cellwidget()

    def init_cellwidget(self):
        size = 60
        size_notes = 16
        margin = 3
        self.stylesheet_active = "border: 1px solid yellow; border-radius: 2px; padding: 0px; background-color: blue;"
        self.stylesheet_notactive = "border: none; border-radius: 2px; padding: 0px; background-color: #6A5ACD; color: #E6E6FA"
        self.note_style = "border: none; border-radius: 5px; padding: 0px; color: black; background-color: #483D8B; color: #E6E6FA"
        # self.value_style = "border: none; border-radius: 2px; padding: 0px; background-color: #6A5ACD; color: #E6E6FA"
        # фиксированный размер виджета
        self.setFixedSize(size, size)  # ширина, высота
        self.setContentsMargins(0,0,0,0)

        # Первая страница - grid layout
        self.notes_page = QWidget()
        self.notesLayout = QGridLayout()
        self.notesLayout.setSpacing(margin)
        self.notesLayout.setContentsMargins(margin, margin, margin, margin)
        self.notesLayout.setRowMinimumHeight(0, size//3)
        self.notesLayout.setRowMinimumHeight(1, size//3)
        self.notesLayout.setRowMinimumHeight(2, size//3)
        self.notesLayout.setColumnMinimumWidth(0, size//3)
        self.notesLayout.setColumnMinimumWidth(1, size//3)
        self.notesLayout.setColumnMinimumWidth(2, size//3)
        # gridLayout.setObjectName(u"cellLayout")

        # список меткок для отображения заметок ячейки
        self.notes_list = [QLabel()] * 9
        font = QFont()
        font.setPointSize(8)
        font.setBold(True)
        for i in range(9):
            self.notes_list[i] = QLabel(str(i + 1))
            self.notes_list[i].setMaximumSize(QSize(size_notes, size_notes))
            self.notes_list[i].setMinimumSize(QSize(size_notes, size_notes))
            self.notes_list[i].setFont(font)
            self.notes_list[i].setAlignment(Qt.AlignCenter)
            self.notes_list[i].setStyleSheet(self.note_style)
            self.notesLayout.addWidget(self.notes_list[i], i // 3, i % 3, 1, 1)

        self.notes_page.setLayout(self.notesLayout)

        # Вторая страница - label
        font_label = QFont()
        font_label.setPointSize(20)
        font_label.setBold(True)
        self.value_label = QLabel('')
        # self.value_label.setStyleSheet(self.value_style)
        self.value_label.setFixedSize(size, size)
        self.value_label.setContentsMargins(0,0,0,0)
        self.value_label.setFont(font_label)
        self.value_label.setAlignment(Qt.AlignCenter)

        # Создаем stacked layout
        self.stacked_layout = QStackedLayout()

        # Добавляем страницы в stacked layout
        self.stacked_layout.addWidget(self.notes_page)
        self.stacked_layout.addWidget(self.value_label)
        self.stacked_layout.setCurrentIndex(1) # заметки скрыты

        self.setStyleSheet(self.stylesheet_notactive)

        # Устанавливаем layout для виджета
        self.setLayout(self.stacked_layout)


    def getValue(self):
        return self.value_label.text()


    def setNotes(self, notes):
        if self.value_label.text() == '':
            for i in range(9):
                if i+1 in notes:
                    self.notesLayout.itemAt(i).widget().setHidden(False)
                else:
                    self.notesLayout.itemAt(i).widget().setHidden(True)


    def setActive(self, param):
        if param:
            self.setStyleSheet(self.stylesheet_active)
        else:
            self.setStyleSheet(self.stylesheet_notactive)


    def showNotes(self, is_visible):
        if is_visible and self.value_label.text() == '':
            self.stacked_layout.setCurrentIndex(0)
        else:
            self.stacked_layout.setCurrentIndex(1)


    def setValue(self, value):
        self.value_label.setText(value)
        self.stacked_layout.setCurrentIndex(1)


    def clear(self):
        """значение в None, все заметки восстанавливаюся"""
        self.value_label.setText('')
        for i in range(9):
            self.notesLayout.itemAt(i).widget().setHidden(False)


    def myupdate(self):
        self.repaint()