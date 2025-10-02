from PySide6.QtGui import QBrush, QColor
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QTableWidget, QFileDialog

from cell_widget import CellWidget
from delegate import DigitDelegate
from field import Field
from ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    """Главное окно приложения"""
    # __file_save_name = 'saves/field.save'
    # __new_value_list = list() # список новых найденных значений ячеек

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

        self.button_save.setCheckable(True)
        self.button_save.clicked.connect(self.button_save_clicked)

        self.button_download.setCheckable(True)
        self.button_download.clicked.connect(self.button_download_clicked)

        self.button_notes.setCheckable(True)
        self.button_notes.clicked.connect(self.button_notes_clicked)
        self.button_notes.setDisabled(True)

        self.button_single.setCheckable(True)
        self.button_single.clicked.connect(self.button_single_clicked)
        self.button_single.setDisabled(True)

        self.button_naked_pair.setCheckable(True)
        self.button_naked_pair.clicked.connect(self.button_naked_pair_clicked)
        self.button_naked_pair.setDisabled(True)

        self.button_hidden_pair.setCheckable(True)
        self.button_hidden_pair.clicked.connect(self.button_hidden_pair_clicked)
        self.button_hidden_pair.setDisabled(True)

        self.button_naked_triple.setCheckable(True)
        self.button_naked_triple.clicked.connect(self.button_naked_triple_clicked)
        self.button_naked_triple.setDisabled(True)

        self.button_hidden_triple.setCheckable(True)
        self.button_hidden_triple.clicked.connect(self.button_hidden_triple_clicked)
        self.button_hidden_triple.setDisabled(True)

        self.button_a.setCheckable(True)
        self.button_a.clicked.connect(self.button_a_clicked)

        self.button_b.setCheckable(True)
        self.button_b.clicked.connect(self.button_b_clicked)

        self.button_c.setCheckable(True)
        self.button_c.clicked.connect(self.button_c_clicked)
        # ********************************************************************************
        # self.one_cell = CellWidget(10, 20, 11, 16)
        self.one_cell = CellWidget()
        self.gl.addWidget(self.one_cell)

        self.two_cell = CellWidget()
        self.gl.addWidget(self.two_cell)

        # # Устанавливаем виджет как центральный
        # self.setCentralWidget(self.one_cell)

        # Создаем игровое поле
        self.field = Field()

    def save_file_dialog(parent=None):
        """Диалог сохранения файла с выбором места и имени"""
        file_path, _ = QFileDialog.getSaveFileName(
            parent,
            "Сохранить файл",  # Заголовок
            "./saves",  # Начальная директория
            "Файлы сохранений (*.save);;Все файлы (*)"  # Фильтры
        )
        if file_path:
            # Добавляем расширение если его нет
            if not file_path.endswith('.save'):
                file_path += '.save'
            print(f"Выбран файл: {file_path}")
            return file_path
        else:
            print("Сохранение отменено")
            return None


    def open_file_dialog(parent=None):
        """Диалог выбора файла для загрузки сохраненных заданий"""
        # file_name, _ = QFileDialog.getOpenFileName(window, 'Open File', '', 'All Files ()')
        file_path, _ = QFileDialog.getOpenFileName(
            parent,
            "Загрузить файл",  # Заголовок
            "./saves",  # Начальная директория
            "Файлы сохранений (*.save);;Все файлы (*)"  # Фильтры
        )
        if file_path and file_path.endswith('.save'):
            print(f"Выбран файл: {file_path}")
            return file_path
        else:
            print("Загрузка отменена")
            return None

    def on_cell_changed(self, row, column):
        """Обработчик изменения ячейки"""
        # print('changed')
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
        # Активируем/деактивируем кнопки
        self.button_create.setDisabled(True)
        # self.button_save.setDisabled(True)
        self.button_download.setDisabled(True)
        self.button_notes.setDisabled(False)
        self.button_single.setDisabled(False)
        self.button_naked_pair.setDisabled(False)
        self.button_hidden_pair.setDisabled(False)
        self.button_naked_triple.setDisabled(False)
        self.button_naked_triple.setDisabled(False)
        self.button_hidden_triple.setDisabled(False)
        # формируем заметки
        for r in range(self.table.rowCount()):
            for c in range(self.table.columnCount()):
                item = self.table.item(r, c)
                if item is not None and item.text() != '':
                    self.field.crossing_out({"row": r, "column": c, "value": int(item.text())})


    def button_save_clicked(self):
        print("Save!")
        file_path = self.save_file_dialog()
        if file_path:
            # Сохраняем данные в файл
            try:
                with open(file_path, "w") as file:
                    # Перебор всех строк и столбцов
                    for r in range(self.table.rowCount()):
                        for c in range(self.table.columnCount()):
                            item = self.table.item(r, c)
                            if item is not None and item.text() != '':
                                file.write(f"{r}{c}{item.text()}\n")
            except FileNotFoundError:
                print("Невозможно открыть файл")
            except:
                print("Ошибка при работе с файлом")
            finally:
                print("Файл успешно закрыт - ", file.closed)


    def button_download_clicked(self):
        print("Download!")
        file_path = self.open_file_dialog()
        if file_path:
            # очищаем поле и таблицу
            self.field = Field()
            # Перебор всех строк и столбцов и очистка заполненных
            for r in range(self.table.rowCount()):
                for c in range(self.table.columnCount()):
                    item = self.table.item(r, c)
                    if item is not None and item.text() != '':
                        item.setText('')
            # читаем данные из файла и заполняем поле и таблицу
            try:
                with open(file_path) as file:
                    for s in file.readlines():
                        self.field.set_cell_value(int(s[0]), int(s[1]), int(s[2]))
                        self.table.setItem(int(s[0]), int(s[1]), QTableWidgetItem(s[2]))
            except FileNotFoundError:
                print("Невозможно открыть файл")
            except:
                print("Ошибка при работе с файлом")
            finally:
                print("Файл успешно закрыт - ", file.closed)


    def button_notes_clicked(self):
        if self.field.get_cell_is_done(self.table.currentRow(), self.table.currentColumn()):
            print('Cell is DONE!')
        else:
            print(self.table.currentRow(), self.table.currentColumn(), '-',
                  self.field.get_cell_possible_value(self.table.currentRow(), self.table.currentColumn()))

    def button_single_clicked(self):
        print("Единицы!")
        res = self.field.hidden_single()
        if res:
            item = QTableWidgetItem(str(res[2]))
            item.setForeground(QBrush(QColor(0, 0, 255)))
            self.table.setItem(res[0], res[1], item)
            self.field.crossing_out({"row": res[0], "column": res[1], "value": res[2]})
            # self.__new_value_list.append({"row": res[0], "column": res[1], "value": res[2]})
            # self.button_step_clicked()
        else:
            print('нет единиц')

    def button_naked_pair_clicked(self):
        print("Голые двойки!")
        if self.field.naked_pair():
            print('есть двойки')
        else:
            print('нет двоек')

    def button_hidden_pair_clicked(self):
        print("Скрытые двойки!")
        if not self.field.hidden_pair():
            print("больше нет скрытых пар")

    def button_naked_triple_clicked(self):
        print("Голые тройки!")
        if not self.field.naked_triple():
            print("больше нет голых троек")

    def button_hidden_triple_clicked(self):
        print("Скрытые тройки!")


    def button_a_clicked(self):
        print("A")
        self.one_cell.updateNotesList({2, 4, 8 ,9})
        self.one_cell.showNotes(False)


    def button_b_clicked(self):
        print("B")
        self.one_cell.showNotes(True)

    def button_c_clicked(self):
        print("C")
        self.one_cell.updateNotesList({2, 4, 9})
