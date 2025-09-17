from cell import Cell


class Field:
    """Игровое поле 9х9"""
    __field = [[Cell() for col in range(9)] for row in range(9)]
    __is_done = False
    # __file_save_name = 'field.save'

    def __init__(self):
        pass

    def get_cell_possible_value(self, r, c):
        # print('z', r, c, self.__field[r][c].get_value())
        return self.__field[r][c].get_possible_values()

    def get_cell_is_done(self, r, c):
        return self.__field[r][c].get_is_done()

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
            # print("по строке")
            for col in range(9):
                if not self.__field[cell["row"]][col].get_is_done():
                    self.__field[cell["row"]][col].discard_possible_value(cell["value"])
                    # print(cell["row"], col, "-", cell["value"])
            # по столбцу
            # print("по столбцу")
            for row in range(9):
                if not self.__field[row][cell["column"]].get_is_done():
                    self.__field[row][cell["column"]].discard_possible_value(cell["value"])
                    # print(row, cell["column"], "-", cell["value"])
            # по блоку
            # print("по блоку")
            r_start = (cell["row"] // 3) * 3
            c_start = (cell["column"] // 3) * 3
            for r in range(r_start, r_start + 3):
                for c in range(c_start, c_start + 3):
                    if not self.__field[r][c].get_is_done():
                        self.__field[r][c].discard_possible_value(cell["value"])
                        # print(r, c, "-", cell["value"])


    def one(self) -> tuple:
        """Обнаружение скрытых единиц"""
        start_set = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        # просмотр блоков с 1го по 9й
        for block in range(9):
            # вычисляем стартовые координаты блока
            r_start = block // 3 * 3
            c_start = block % 3 * 3
            # просмотр блока
            result = start_set.copy()
            # print('----------', result)
            # print(start_set)
            for r in range(r_start, r_start + 3):
                for c in range(c_start, c_start + 3):
                    item = self.__field[r][c]
                    if not item.get_is_done():
                        # если в ячейке единственный вариант, то устанавливаем и возвращаем его
                        if item.check():
                            print("check по блоку", r, c, item.get_value())
                            return (r, c, item.get_value())
                        for i in item.get_possible_values():
                            result[i] += 1
            # просмотр блока (второй прогон)
            for key, value in result.items():
                if value == 1:
                    for r in range(r_start, r_start + 3):
                        for c in range(c_start, c_start + 3):
                            item = self.__field[r][c]
                            if not item.get_is_done() and key in item.get_possible_values():
                                item.set_done(key)
                                print('block')
                                return (r, c, key)

        # просмотр строк с 1й по 9ю
        for r in range(9):
            # просмотр строки
            result = start_set.copy()
            for c in range(9):
                item = self.__field[r][c]
                if not item.get_is_done():
                    # если в ячейке единственный вариант, то устанавливаем и возвращаем его
                    if item.check():
                        print("check по строки", r, c, item.get_value())
                        return (r, c, item.get_value())
                    for i in item.get_possible_values():
                        result[i] += 1
            # просмотр строки (второй прогон)
            for key, value in result.items():
                if value == 1:
                    for c in range(9):
                        item = self.__field[r][c]
                        if not item.get_is_done() and key in item.get_possible_values():
                            item.set_done(key)
                            print('row')
                            return (r, c, key)

        # просмотр столобцов с 1го по 9й
        for c in range(9):
            # просмотр столбца
            result = start_set.copy()
            for r in range(9):
                item = self.__field[r][c]
                if not item.get_is_done():
                    # если в ячейке единственный вариант, то устанавливаем и возвращаем его
                    if item.check():
                        print("check по столбца", r, c, item.get_value())
                        return (r, c, item.get_value())
                    for i in item.get_possible_values():
                        result[i] += 1
            # просмотр столбца (второй прогон)
            for key, value in result.items():
                if value == 1:
                    for r in range(9):
                        item = self.__field[r][c]
                        if not item.get_is_done() and key in item.get_possible_values():
                            item.set_done(key)
                            print('column')
                            return (r, c, key)

        # если нет результатов, возвращаем пустой кортеж
        return tuple()