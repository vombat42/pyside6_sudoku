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


    def number_unresolved_cells(self, row, column, param=None):
        """Вычисляет число нерешенных ячеек в блоке/строке/столбце (param = b/r/c/) по координатам ячейки"""
        number = 0
        if not param in {'b', 'r', 'c'}:
            return None
        elif param == 'b':
            # задан подсчет в блоке
            r_start = (row // 3) * 3
            c_start = (column // 3) * 3
            for r in range(r_start, r_start + 3):
                for c in range(c_start, c_start + 3):
                    if not self.__field[r][c].get_is_done():
                        number += 1
        elif param == 'r':
            # задан подсчет по строке
            for c in range(9):
                if not self.__field[row][c].get_is_done():
                    number += 1
        elif param == 'c':
            # задан подсчет по столбцу
            for r in range(9):
                if not self.__field[r][column].get_is_done():
                    number += 1
        return number


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
            # print(block, "result", result)
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
                                        if item.discard_set_possible_value(x[2]):
                                            flag = True

        # просмотр строк с 1й по 9ю
        for r in range(9):
            # просмотр строки, ищем ячейки, в которых два возможных значения
            result = list()
            for c in range(9):
                item = self.__field[r][c]
                if not item.get_is_done() and len(item.get_possible_values()) == 2:
                    result.append((r, c, item.get_possible_values()))
            # просмотр "двоек"
            # print('row =', r, ", result =", result)
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
                                    if item.discard_set_possible_value(x[2]):
                                        flag = True

        # просмотр столбцов с 1го по 9й
        for c in range(9):
            # просмотр столбца, ищем ячейки, в которых два возможных значения
            result = list()
            for r in range(9):
                item = self.__field[r][c]
                if not item.get_is_done() and len(item.get_possible_values()) == 2:
                    result.append((r, c, item.get_possible_values()))
            # просмотр "двоек"
            # print('column =', c, ", result =", result)
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
                                    if item.discard_set_possible_value(x[2]):
                                        flag = True
        return flag

    def naked_triple(self) -> bool:
        """Метод 'Голая тройка'"""
        flag = False
        # просмотр блоков с 1го по 9й
        for block in range(9):
            # стартовые координаты блока
            r_start, c_start = Field.block_coordinates(block)
            # просмотр блока, ищем ячейки, в которых три возможных значения
            # result = list()
            for r in range(r_start, r_start + 3):
                for c in range(c_start, c_start + 3):
                    item = self.__field[r][c]
                    result = list()
                    if not item.get_is_done() and len(item.get_possible_values()) == 3:
                        # при нахождении такой ячейки, снова смотрим, есть ли в блоке еще две ячейки, образующие "голую тройку"
                        for r_next in range(r_start, r_start + 3):
                            for c_next in range(c_start, c_start + 3):
                                item_next = self.__field[r_next][c_next]
                                # if not item.get_is_done() and len(item_next.get_possible_values()) <= 3 and not (r_next == r and c_next == c):
                                if not item_next.get_is_done() and item.get_possible_values() >= item_next.get_possible_values():
                                    result.append((r_next, c_next))
                        if len(result) > 3:
                            print('Такого не может быть!!!')
                            return flag
                        if len(result) == 3:
                            # голая тройка обнаружена, значит пробуем вычеркнуть ее значения из остальных ячеек блока
                            for r_out in range(r_start, r_start + 3):
                                for c_out in range(c_start, c_start + 3):
                                    item_out = self.__field[r_out][c_out]
                                    if not item_out.get_is_done() and not (r_out, c_out) in result:
                                        if item_out.discard_set_possible_value(item.get_possible_values()):
                                            print("корректировка заметок в блоке", block)
                                            flag = True

        # просмотр строк с 1й по 9ю
        for r in range(9):
            # просмотр строки, ищем ячейки, в которых три возможных значения
            for c in range(9):
                item = self.__field[r][c]
                result = list()
                if not item.get_is_done() and len(item.get_possible_values()) == 3:
                    for c_next in range(9):
                        item_next = self.__field[r][c_next]
                        if not item_next.get_is_done() and item.get_possible_values() >= item_next.get_possible_values():
                            result.append((r, c_next))
                if len(result) > 3:
                    print('Такого не может быть!!!')
                    return flag
                if len(result) == 3:
                    # голая тройка обнаружена, значит пробуем вычеркнуть ее значения из остальных ячеек строки
                    for c_out in range(9):
                        item_out = self.__field[r][c_out]
                        if not item_out.get_is_done() and not (r, c_out) in result:
                            if item_out.discard_set_possible_value(item.get_possible_values()):
                                print("корректировка заметок в строке", r)
                                flag = True

        # просмотр столбцов с 1го по 9й
        for c in range(9):
            # просмотр столбца, ищем ячейки, в которых три возможных значения
            for r in range(9):
                item = self.__field[r][c]
                result = list()
                if not item.get_is_done() and len(item.get_possible_values()) == 3:
                    for r_next in range(9):
                        item_next = self.__field[r_next][c]
                        if not item_next.get_is_done() and item.get_possible_values() >= item_next.get_possible_values():
                            result.append((r_next, c))
                if len(result) > 3:
                    print('Такого не может быть!!!')
                    return flag
                if len(result) == 3:
                    # голая тройка обнаружена, значит пробуем вычеркнуть ее значения из остальных ячеек столбца
                    for r_out in range(9):
                        item_out = self.__field[r_out][c]
                        if not item_out.get_is_done() and not (r_out, c) in result:
                            if item_out.discard_set_possible_value(item.get_possible_values()):
                                print("корректировка заметок в столбце", c)
                                flag = True
        return flag

    def hidden_pair(self) -> bool:
        """Метод 'Скрытые пары'"""
        n = 2
        flag = False
        # empty_list список из 9 списков
        empty_list = [None] * 9
        for i in range(9):
            empty_list[i] = list()
        # просмотр блоков с 1го по 9й
        for block in range(9):
            # стартовые координаты блока
            r_start, c_start = Field.block_coordinates(block)
            # просмотр блока, ищем значения, которые есть только в двух ячейках блока
            result = empty_list
            for r in range(r_start, r_start + 3):
                for c in range(c_start, c_start + 3):
                    item = self.__field[r][c]
                    if not item.get_is_done():
                        for v in item.get_possible_values():
                            result[v-1].append((r, c))
            # проходимся по result в поисках скрытых пар
            for i in range(8):
                if len(result[i]) == n:
                    for j in range(i+1, 9):
                        if result[i] == result[j]:
                            # скрытая пара найдена, убираем лишние возможные значения (если они не убраны ранее)
                            r_1 = result[i][0][0]
                            r_2 = result[i][0][1]
                            c_1 = result[i][1][0]
                            c_2 = result[i][1][1]
                            item_1 = self.__field[r_1][c_1]
                            item_2 = self.__field[r_2][c_2]
                            values = {i+1, j+1}
                            if item_1.get_possible_values() != values or item_2.get_possible_values() != values:
                                item_1.set_possible_values(values)
                                item_2.set_possible_values(values)
                                flag = True
                            # если скрытая пара в одном блоке и в одной строке, то корректируем возможные значения по всей строке
                            if r_1 == r_2:
                                for col in range(9):
                                    if col not in {c_1, c_2} and not self.__field[r_1][col].get_is_done():
                                        if self.__field[r_1][col].discard_set_possible_value(values):
                                            flag = True
                            # если скрытая пара в одном блоке и в одном столбце, то корректируем возможные значения по всему столбцу
                            if c_1 == c_2:
                                for row in range(9):
                                    if row not in {r_1, r_2} and not self.__field[row][c_1].get_is_done():
                                        if self.__field[row][c_1].discard_set_possible_value(values):
                                            flag = True

        # просмотр строк с 1й по 9ю
        for r in range(9):
            result = empty_list
            # просмотр строки, ищем значения, которые есть только в двух ячейках строки
            for c in range(9):
                item = self.__field[r][c]
                if not item.get_is_done():
                    for v in item.get_possible_values():
                        result[v - 1].append((r, c))
            # проходимся по result в поисках скрытых пар
            for i in range(8):
                if len(result[i]) == n:
                    for j in range(i+1, 9):
                        if result[i] == result[j]:
                            # скрытая пара найдена, убираем лишние возможные значения (если они не убраны ранее)
                            r_1 = result[i][0][0]
                            r_2 = result[i][0][1]
                            c_1 = result[i][1][0]
                            c_2 = result[i][1][1]
                            item_1 = self.__field[r_1][c_1]
                            item_2 = self.__field[r_2][c_2]
                            values = {i+1, j+1}
                            if item_1.get_possible_values() != values or item_2.get_possible_values() != values:
                                item_1.set_possible_values(values)
                                item_2.set_possible_values(values)
                                flag = True

        # просмотр столбцов с 1го по 9й
        for c in range(9):
            result = empty_list
            # просмотр строки, ищем значения, которые есть только в двух ячейках строки
            for r in range(9):
                item = self.__field[r][c]
                if not item.get_is_done():
                    for v in item.get_possible_values():
                        result[v - 1].append((r, c))
            # проходимся по result в поисках скрытых пар
            for i in range(8):
                if len(result[i]) == n:
                    for j in range(i+1, 9):
                        if result[i] == result[j]:
                            # скрытая пара найдена, убираем лишние возможные значения (если они не убраны ранее)
                            r_1 = result[i][0][0]
                            r_2 = result[i][0][1]
                            c_1 = result[i][1][0]
                            c_2 = result[i][1][1]
                            item_1 = self.__field[r_1][c_1]
                            item_2 = self.__field[r_2][c_2]
                            values = {i+1, j+1}
                            if item_1.get_possible_values() != values or item_2.get_possible_values() != values:
                                item_1.set_possible_values(values)
                                item_2.set_possible_values(values)
                                flag = True

        return flag

