
class Cell:
    """Ячейка таблицы"""
    __value = None
    __is_done = False # False - не определено значение ячейки, True - определено

    def __init__(self):
        self.__possible_values = set(range(1, 10))  # от 1 до 9
        pass

    def get_value(self):
        return self.__value

    def get_is_done(self) -> bool:
        return self.__is_done

    def get_possible_values(self):
        return self.__possible_values

    def set_possible_values(self, value):
        self.__possible_values = value

    def set_done(self, value):
        self.__value = value
        if value != None:
            self.__is_done = True
        else:
            self.__is_done = False

    def discard_possible_value(self, value):
        """Убирает из вариантов переданоое значение"""
        self.__possible_values.discard(value)

    def discard_set_possible_value(self, values) -> bool:
        """Убирает из вариантов переданоое множество значений"""
        temp = self.__possible_values - values
        if temp == self.__possible_values:
            # удалаять нечего
            return False
        self.__possible_values = temp
        return True


    def check(self) -> bool:
        """Если остается один вариант, то устанавливает атрибуты и возвращает True"""
        if len(self.__possible_values) == 1:
            self.__is_done = True
            self.__value = self.__possible_values.pop()
            print("check!!!", self.__value, type(self.__value))
        return self.__is_done