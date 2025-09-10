from cell import Cell


class Field:
    """Игровое поле 9х9"""
    __field = [[Cell() for col in range(9)] for row in range(9)]
    __is_done = False
    # __file_save_name = 'field.save'

    def __init__(self):
        pass

    def get_cell_possible_value(self, r1, c1):
        print('z', r1, c1, self.__field[r1][c1].get_value())
        return self.__field[r1][c1].get_possible_values()

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


    def crossing_out(self, cell_list):
        """Вычеркивание невозможных вариантов по линиям и блокам
         формат cell_list - [{"row":номер строки, "column":номер столбца, "value":значение}, ...] - список словарей"""
        for cell in cell_list:
            # по строке
            print("по строке")
            for col in range(9):
                if not self.__field[cell["row"]][col].get_is_done():
                    self.__field[cell["row"]][col].discard_possible_value(cell["value"])
                    print(cell["row"], col, "-", cell["value"])
            # по столбцу
            print("по столбцу")
            for row in range(9):
                if not self.__field[row][cell["column"]].get_is_done():
                    self.__field[row][cell["column"]].discard_possible_value(cell["value"])
                    print(row, cell["column"], "-", cell["value"])
            # по блоку
            print("по блоку")
            r_start = (cell["row"] // 3) * 3
            c_start = (cell["column"] // 3) * 3
            for r in range(r_start, r_start + 3):
                for c in range(c_start, c_start + 3):
                    if not self.__field[r][c].get_is_done():
                        self.__field[r][c].discard_possible_value(cell["value"])
                        print(r, c, "-", cell["value"])
