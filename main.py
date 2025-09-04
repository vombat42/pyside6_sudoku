import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QWidget, QApplication, QMainWindow
from app_window import MainWindow


# ------------------------------------------------------------------


def main():
    app = QApplication(sys.argv)  # Новый экземпляр QApplication
    window =  MainWindow()
    window.show()  # Показываем окно
    app.exec()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()