from PySide6.QtGui import QBrush, QColor
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QTableWidget

from delegate import DigitDelegate
from field import Field
from ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    """Главное окно приложения"""
    __file_save_name = 'field.save'
    __new_value_list = list() # список новых найденных значений ячеек

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
        self.button_step.setDisabled(True)

        self.button_show_notes.setCheckable(True)
        self.button_show_notes.clicked.connect(self.button_show_notes_clicked)
        self.button_show_notes.setDisabled(True)

        self.button_save.setCheckable(True)
        self.button_save.clicked.connect(self.button_save_clicked)

        self.button_download.setCheckable(True)
        self.button_download.clicked.connect(self.button_download_clicked)


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
        # Активируем/деактивируем кнопки
        self.button_create.setDisabled(True)
        self.button_save.setDisabled(True)
        self.button_download.setDisabled(True)
        self.button_step.setDisabled(False)
        self.button_show_notes.setDisabled(False)
        # формируем список __new_value_list
        for r in range(self.table.rowCount()):
            for c in range(self.table.columnCount()):
                item = self.table.item(r, c)
                if item is not None and item.text() != '':
                    self.__new_value_list.append({"row": r, "column": c, "value": int(item.text())})
        print(self.__new_value_list)


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

    def button_step_clicked(self):
        print("Crossing out!")
        self.field.crossing_out(self.__new_value_list)
        self.__new_value_list = list()


    def button_show_notes_clicked(self):
        print(self.table.currentRow(), self.table.currentColumn(), '-', self.field.get_cell_possible_value(self.table.currentRow(), self.table.currentColumn()))