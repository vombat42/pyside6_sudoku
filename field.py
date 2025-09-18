from cell import Cell


class Field:
    """Игровое поле 9х9"""
    __field = [[Cell() for col in range(9)] for row in range(9)]
    __is_done = False


    def __init__(self):
        pass

    @staticmethod
    def block_coordinates(block: int):
        """вычисляем стартовые координаты блока (row, column)"""
        return block // 3 * 3, block % 3 * 3


    def get_cell_possible_value(self, r, c):
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


    def crossing_out(self, cell):
        """Вычеркивание невозможных вариантов по линиям и блокам
         формат cell - {"row":номер строки, "column":номер столбца, "value":значение}"""
        # по строке
        for col in range(9):
            if not self.__field[cell["row"]][col].get_is_done():
                self.__field[cell["row"]][col].discard_possible_value(cell["value"])
        # по столбцу
        for row in range(9):
            if not self.__field[row][cell["column"]].get_is_done():
                self.__field[row][cell["column"]].discard_possible_value(cell["value"])
        # по блоку
        r_start = (cell["row"] // 3) * 3
        c_start = (cell["column"] // 3) * 3
        for r in range(r_start, r_start + 3):
            for c in range(c_start, c_start + 3):
                if not self.__field[r][c].get_is_done():
                    self.__field[r][c].discard_possible_value(cell["value"])


    def hidden_single(self) -> tuple:
        """Метод 'Скрытая одиночка'"""
        start_set = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        # просмотр блоков с 1го по 9й
        for block in range(9):
            # стартовые координаты блока
            r_start, c_start = Field.block_coordinates(block)
            # просмотр блока
            result = start_set.copy()
            for r in range(r_start, r_start + 3):
                for c in range(c_start, c_start + 3):
                    item = self.__field[r][c]
                    if not item.get_is_done():
                        # если в ячейке единственный вариант, то устанавливаем и возвращаем его
                        if item.check():
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
                            return (r, c, key)

        # если нет результатов, возвращаем пустой кортеж
        return tuple()


    def naked_pair(self) -> bool:
        """Метод 'Голая пара'"""
        flag = False
        # просмотр блоков с 1го по 9й
        for block in range(9):
            # стартовые координаты блока
            r_start, c_start = Field.block_coordinates(block)
            # просмотр блока, ищем ячейки, в которых два возможных значения
            result = list()
            for r in range(r_start, r_start + 3):
                for c in range(c_start, c_start + 3):
                    item = self.__field[r][c]
                    if not item.get_is_done() and len(item.get_possible_values()) == 2:
                        result.append((r, c, item.get_possible_values()))
            # просмотр "двоек"
            print(block, "result", result)
            if len(result) > 1:
                i = 0
                for x in result[:-1]:
                    i += 1
                    for y in result[i:]:
                        if x[2] == y[2]:
                            print('two finded in block! -', x[0], x[1], '<->', y[0], y[1], ':', x[2])
                            # вычеркиваем из других ячеек блока эту "двойку" и выходим из функции, возвращаем True
                            for r in range(r_start, r_start + 3):
                                for c in range(c_start, c_start + 3):
                                    item = self.__field[r][c]
                                    if not item.get_is_done() and item.get_possible_values() != x[2]:
                                        item.discard_set_possible_value(x[2])

        # просмотр строк с 1й по 9ю
        for r in range(9):
            # просмотр строки, ищем ячейки, в которых два возможных значения
            result = list()
            for c in range(9):
                item = self.__field[r][c]
                if not item.get_is_done() and len(item.get_possible_values()) == 2:
                    result.append((r, c, item.get_possible_values()))
            # просмотр "двоек"
            print('row =', r, ", result =", result)
            if len(result) > 1:
                i = 0
                for x in result[:-1]:
                    i += 1
                    for y in result[i:]:
                        if x[2] == y[2]:
                            print('two finded in column! -', x[0], x[1], '<->', y[0], y[1], ':', x[2])
                            # вычеркиваем из других ячеек строки эту "двойку" и выходим из функции, возвращаем True
                            for c in range(9):
                                item = self.__field[r][c]
                                if not item.get_is_done() and item.get_possible_values() != x[2]:
                                    item.discard_set_possible_value(x[2])

        # просмотр столбцов с 1го по 9й
        for c in range(9):
            # просмотр столбца, ищем ячейки, в которых два возможных значения
            result = list()
            for r in range(9):
                item = self.__field[r][c]
                if not item.get_is_done() and len(item.get_possible_values()) == 2:
                    result.append((r, c, item.get_possible_values()))
            # просмотр "двоек"
            print('column =', c, ", result =", result)
            if len(result) > 1:
                i = 0
                for x in result[:-1]:
                    i += 1
                    for y in result[i:]:
                        if x[2] == y[2]:
                            print('two finded in column! -', x[0], x[1], '<->', y[0], y[1], ':', x[2])
                            # вычеркиваем из других ячеек столбца эту "двойку"
                            for r in range(9):
                                item = self.__field[r][c]
                                if not item.get_is_done() and item.get_possible_values() != x[2]:
                                    item.discard_set_possible_value(x[2])
        return flag

    def naked_triple(self) -> bool:
        """Метод 'Голая тройка'"""
        flag = False
        # просмотр блоков с 1го по 9й
        for block in range(9):
            # стартовые координаты блока
            r_start, c_start = Field.block_coordinates(block)
            # просмотр блока, ищем ячейки, в которых два возможных значения
            result = list()
            for r in range(r_start, r_start + 3):
                for c in range(c_start, c_start + 3):
                    item = self.__field[r][c]
                    if not item.get_is_done() and len(item.get_possible_values()) == 2:
                        result.append((r, c, item.get_possible_values()))
            # просмотр "двоек"
            print(block, "result", result)
            if len(result) > 1:
                i = 0
                for x in result[:-1]:
                    i += 1
                    for y in result[i:]:
                        if x[2] == y[2]:
                            print('two finded in block! -', x[0], x[1], '<->', y[0], y[1], ':', x[2])
                            # вычеркиваем из других ячеек блока эту "двойку" и выходим из функции, возвращаем True
                            for r in range(r_start, r_start + 3):
                                for c in range(c_start, c_start + 3):
                                    item = self.__field[r][c]
                                    if not item.get_is_done() and item.get_possible_values() != x[2]:
                                        item.discard_set_possible_value(x[2])

        # # просмотр строк с 1й по 9ю
        # for r in range(9):
        #     # просмотр строки, ищем ячейки, в которых два возможных значения
        #     result = list()
        #     for c in range(9):
        #         item = self.__field[r][c]
        #         if not item.get_is_done() and len(item.get_possible_values()) == 2:
        #             result.append((r, c, item.get_possible_values()))
        #     # просмотр "двоек"
        #     print('row =', r, ", result =", result)
        #     if len(result) > 1:
        #         i = 0
        #         for x in result[:-1]:
        #             i += 1
        #             for y in result[i:]:
        #                 if x[2] == y[2]:
        #                     print('two finded in column! -', x[0], x[1], '<->', y[0], y[1], ':', x[2])
        #                     # вычеркиваем из других ячеек строки эту "двойку" и выходим из функции, возвращаем True
        #                     for c in range(9):
        #                         item = self.__field[r][c]
        #                         if not item.get_is_done() and item.get_possible_values() != x[2]:
        #                             item.discard_set_possible_value(x[2])
        #
        # # просмотр столбцов с 1го по 9й
        # for c in range(9):
        #     # просмотр столбца, ищем ячейки, в которых два возможных значения
        #     result = list()
        #     for r in range(9):
        #         item = self.__field[r][c]
        #         if not item.get_is_done() and len(item.get_possible_values()) == 2:
        #             result.append((r, c, item.get_possible_values()))
        #     # просмотр "двоек"
        #     print('column =', c, ", result =", result)
        #     if len(result) > 1:
        #         i = 0
        #         for x in result[:-1]:
        #             i += 1
        #             for y in result[i:]:
        #                 if x[2] == y[2]:
        #                     print('two finded in column! -', x[0], x[1], '<->', y[0], y[1], ':', x[2])
        #                     # вычеркиваем из других ячеек столбца эту "двойку"
        #                     for r in range(9):
        #                         item = self.__field[r][c]
        #                         if not item.get_is_done() and item.get_possible_values() != x[2]:
        #                             item.discard_set_possible_value(x[2])
        # return flag



