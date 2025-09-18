from PySide6.QtGui import QBrush, QColor
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QTableWidget

from delegate import DigitDelegate
from field import Field
from ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    """Главное окно приложения"""
    __file_save_name = 'field.save'
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


        # Создаем игровое поле
        self.field = Field()

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
        self.button_save.setDisabled(True)
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
                    # self.__new_value_list.append({"row": r, "column": c, "value": int(item.text())})
        # print(self.__new_value_list)
        # print("Crossing out!", self.__new_value_list)
        # self.field.crossing_out(self.__new_value_list)
        # self.__new_value_list = list()


    def button_save_clicked(self):
        print("Save!")
        try:
            with open(self.__file_save_name, "w") as file:
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
            with open(self.__file_save_name) as file:
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

    def button_naked_triple_clicked(self):
        print("Голые тройки!")

    def button_hidden_triple_clicked(self):
        print("Скрытые тройки!")