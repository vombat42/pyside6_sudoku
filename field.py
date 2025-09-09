from cell import Cell


class Field:
    """Игровое поле 9х9"""
    __field = [[Cell() for col in range(9)] for row in range(9)]
    __is_done = False
    # __file_save_name = 'field.save'

    def __init__(self):
        pass

    def clear_cell(self, row, column):
        self.__field[row][column].set_done(None)

    def set_cell_value(self, row, column, value: int) -> bool:
        """Установка значения в ячейку, если некорректно - возвращаем False"""
        self.__field[row][column].set_done(None) #предварительно очищаем ячеку, если вдруг значение некорректно
        # проверка по строке
        for c in range(9):
            if self.__field[row][c].get_value() == value:
                return False
        # проверка по столбцу
        for r in range(9):
            if self.__field[r][column].get_value() == value:
                return False
        # проверка по блоку
        r_start = (row // 3) * 3
        c_start = (column // 3) * 3
        for r in range(r_start, r_start + 3):
            for c in range(c_start, c_start + 3):
                if self.__field[r][c].get_value() == value:
                    return False
        self.__field[row][column].set_done(value) #значение корректно - записывем в ячейку
        return True


    # def save_field(self):
    #     try:
    #         with open(self.__file_save_name, "w") as file:
    #             for r in range(9):
    #                 for c in range(9):
    #                     if self.__field[r][c].get_value() != None:
    #                         file.write(f"{r}{c}{self.__field[r][c].get_value()}\n")
    #     except FileNotFoundError:
    #          print("Невозможно открыть файл")
    #     except:
    #         print("Ошибка при работе с файлом")
    #     finally:
    #         print(file.closed)