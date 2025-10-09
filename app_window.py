from PySide6.QtCore import QRect
from PySide6.QtWidgets import QMainWindow, QFileDialog, QWidget, QVBoxLayout

from field import Field
from field_widget import FieldWidget
from ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    """Главное окно приложения"""
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

        self.setWindowTitle("sudoku")

        self.button_create.setCheckable(True)
        self.button_create.clicked.connect(self.button_create_clicked)

        self.button_save.setCheckable(True)
        self.button_save.clicked.connect(self.button_save_clicked)

        self.button_download.setCheckable(True)
        self.button_download.clicked.connect(self.button_download_clicked)


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


        # CheckBox "показать заметки"
        self.notes_box.setCheckable(True)
        self.notes_box.setChecked(False)
        self.notes_box.checkStateChanged.connect(self.notes_box_changed)

        # Игровое поле 9x9
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        # self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 600, 600))
        self.vl = QVBoxLayout(self.verticalLayoutWidget)
        self.vl.setContentsMargins(0, 0, 0, 0)
        # self.vl.setObjectName(u"vl")

        self.field_widget = FieldWidget()
        # self.gl.addWidget(self.field_widget)
        self.vl.addWidget(self.field_widget)
        self.field_widget.signal_cell_changed.connect(self.cell_changed)

        # Создаем игровое поле (логика)
        self.field = Field()



    def cell_changed(self, info: dict):
        """Обработчик изменения ячейки"""
        print("cell_changed", info)
        if info['new_value'] == '':
            self.field.clear_cell(info['row'], info['column'])
        else:
            # если такое значение в ячейке допустимо, присваиваем его
            if self.field.set_cell_value(info['row'], info['column'], int(info['new_value'])):
                self.field_widget.setValue(info['row'], info['column'], info['new_value'])
                self.field.crossing_out({"row": info['row'], "column": info['column'], "value": int(info['new_value'])})
                self.update_notes_in_field()


    def notes_box_changed(self):
        self.field_widget.showNotes(self.notes_box.isChecked())


    def update_notes_in_field(self):
        """обновляет заметки в виджете игрового поля"""
        for r in range(9):
            for c in range(9):
                self.field_widget.setNotes(r, c, self.field.get_cell_possible_value(r, c))


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


    def button_create_clicked(self):
        print("Clicked!")
        # Активируем/деактивируем кнопки
        self.button_create.setDisabled(True)
        # self.button_save.setDisabled(True)
        self.button_download.setDisabled(True)
        self.button_single.setDisabled(False)
        self.button_naked_pair.setDisabled(False)
        self.button_hidden_pair.setDisabled(False)
        self.button_naked_triple.setDisabled(False)
        self.button_naked_triple.setDisabled(False)
        self.button_hidden_triple.setDisabled(False)
        # формируем заметки
        for r in range(9):
            for c in range(9):
                value = self.field_widget.get_cell_value(r, c)
                if value != '':
                    self.field.crossing_out({"row": r, "column": c, "value": int(value)})

        self.update_notes_in_field()
        self.field_widget.set_is_being_solved()



    def button_save_clicked(self):
        print("Save!")
        file_path = self.save_file_dialog()
        if file_path:
            # Сохраняем данные в файл
            try:
                with open(file_path, "w") as file:
                    # Перебор всех строк и столбцов
                    for row in range(9):
                        for column in range(9):
                            value = self.field_widget.get_cell_value(row, column)
                            if value != '':
                                file.write(f"{row}{column}{value}\n")
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
            self.field_widget.clear()
            # читаем данные из файла и заполняем поле и таблицу
            max_lines = 81 # больше строк не читаем!
            try:
                with open(file_path) as file:
                    for s in file.readlines():
                        r, c, v = int(s[0]), int(s[1]), s[2]
                        self.field_widget.setValue(r, c, v)
                        self.field.set_cell_value(r, c, int(v))
                        max_lines -= 1
                        if max_lines <= 0:
                            break
            except FileNotFoundError:
                print("Невозможно открыть файл")
            except:
                print("Ошибка при работе с файлом")
            finally:
                print("Файл успешно закрыт - ", file.closed)


    def button_single_clicked(self):
        print("Единицы!")
        res = self.field.hidden_single()
        if res:
            self.field.crossing_out({"row": res[0], "column": res[1], "value": res[2]})
            self.field_widget.setValue(res[0], res[1], str(res[2]))
            self.update_notes_in_field()
        else:
            print('нет единиц')

    def button_naked_pair_clicked(self):
        print("Голые двойки!")
        if not self.field.naked_pair():
            print('больше нет двоек')
        else:
            self.update_notes_in_field()

    def button_hidden_pair_clicked(self):
        print("Скрытые двойки!")
        if not self.field.hidden_pair():
            print("больше нет скрытых пар")
        else:
            self.update_notes_in_field()

    def button_naked_triple_clicked(self):
        print("Голые тройки!")
        if not self.field.naked_triple():
            print("больше нет голых троек")
        else:
            self.update_notes_in_field()

    def button_hidden_triple_clicked(self):
        print("Скрытые тройки!")


    def button_a_clicked(self):
        print("A")
        self.field_widget.showNotes(True)


    def button_b_clicked(self):
        print("B")
        self.field_widget.showNotes(False)


