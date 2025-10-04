from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QFont, QMouseEvent
from PySide6.QtWidgets import QWidget, QLabel, QGridLayout, QStackedLayout


class CellWidget(QWidget):
    """Кастомный виджет для одной ячейки"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_cellwidget()

    def init_cellwidget(self):
        size = 60
        # фиксированный размер виджета
        self.setFixedSize(size, size)  # ширина, высота

        # Первая страница - grid layout
        self.notes_page = QWidget()
        self.notesLayout = QGridLayout()
        self.notesLayout.setSpacing(3)
        self.notesLayout.setContentsMargins(3, 3, 3, 3)
        self.notesLayout.setRowMinimumHeight(0, size//3)
        self.notesLayout.setRowMinimumHeight(1, size//3)
        self.notesLayout.setRowMinimumHeight(2, size//3)
        self.notesLayout.setColumnMinimumWidth(0, size//3)
        self.notesLayout.setColumnMinimumWidth(1, size//3)
        self.notesLayout.setColumnMinimumWidth(2, size//3)
        # gridLayout.setObjectName(u"cellLayout")


        # список меткок для отображения заметок ячейки
        self.notes_list = [QLabel()] * 9
        note_style = "border: 1px solid gray; border-radius: 4px; padding: 0px; background-color: green;"
        font = QFont()
        font.setPointSize(8)
        for i in range(9):
            self.notes_list[i] = QLabel(str(i + 1))
            self.notes_list[i].setMaximumSize(QSize(16, 16))
            self.notes_list[i].setMinimumSize(QSize(16, 16))
            self.notes_list[i].setFont(font)
            self.notes_list[i].setStyleSheet(note_style)
            self.notesLayout.addWidget(self.notes_list[i], i // 3, i % 3, 1, 1)

        self.notes_page.setLayout(self.notesLayout)

        # Вторая страница - label
        font_label = QFont()
        font_label.setPointSize(20)
        self.value_label = QLabel('')
        self.value_label.setFont(font_label)
        self.value_label.setAlignment(Qt.AlignCenter)
        self.value_label.setStyleSheet("""
            QWidget {
                padding: 0px;
                background-color: blue;
                text-align: center;
            }
        """)

        # Создаем stacked layout
        self.stacked_layout = QStackedLayout()

        # Добавляем страницы в stacked layout
        self.stacked_layout.addWidget(self.notes_page)
        self.stacked_layout.addWidget(self.value_label)

        self.setStyleSheet("border: 1px solid yellow; border-radius: 2px; padding: 0px;")

        # Устанавливаем layout для виджета
        self.setLayout(self.stacked_layout)


    def setNotes(self, notes):
        if self.value_label.text() == '':
            for i in range(9):
                if i+1 in notes:
                    self.notesLayout.itemAt(i).widget().setHidden(False)
                else:
                    self.notesLayout.itemAt(i).widget().setHidden(True)


    def showNotes(self, is_visible):
        if is_visible and self.value_label.text() == '':
            self.stacked_layout.setCurrentIndex(0)
        else:
            self.stacked_layout.setCurrentIndex(1)

    def mousePressEvent(self, event: QMouseEvent):
        """Обрабатывает нажатие мыши"""
        if event.button() == Qt.LeftButton:
            self.setStyleSheet("border: 2px solid red; border-radius: 2px; padding: 0px;")

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