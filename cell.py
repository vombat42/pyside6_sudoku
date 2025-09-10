
class Cell:
    """Ячейка таблицы"""
    __value = None
    __is_done = False # False - не определено значение ячейки, True - определено
    # __possible_values = set(range(1, 10)) # от 1 до 9
    __possible_values = set() # от 1 до 9


    def __init__(self):
        self.__possible_values = set(range(1, 10))  # от 1 до 9
        pass

    def get_value(self):
        return self.__value

    def get_is_done(self) -> bool:
        return self.__is_done

    def get_possible_values(self):
        return self.__possible_values

    def set_done(self, value):
        self.__value = value
        self.__is_done = True

    def discard_possible_value(self, value) -> bool:
        """Убирает из вариантов переданоое значение"""
        self.__possible_values.discard(value)

    def check(self) -> bool:
        """Если остается один вариант, то устанавливает атрибуты и возвращает True"""
        if len(self.__possible_values) == 1:
            self.__is_done = True
            self.__value = self.__possible_values.pop()
        return self.__is_done