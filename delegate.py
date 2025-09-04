from PySide6.QtCore import QTimer
from PySide6.QtGui import QIntValidator, QRegularExpressionValidator
from PySide6.QtWidgets import QStyledItemDelegate


class DigitDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)

    def createEditor(self, parent, option, index):
        editor = super().createEditor(parent, option, index)

        # Валидатор для одной цифры

        validator = QRegularExpressionValidator("[1-9]", self)
        editor.setValidator(validator)
        editor.setMaxLength(1)

        # Подключаем обработчик событий редактора
        editor.installEventFilter(self)

        # Подключаем обработчик текста
        editor.textChanged.connect(lambda text: self.on_text_changed(editor, text))

        return editor

    def on_text_changed(self, editor, text):
        """Автоматически завершаем ввод при вводе одного символа"""
        # Пытаемся безопасно закрыть редактор
        try:
            if editor and editor.isVisible() and editor.hasAcceptableInput():
                self.commitData.emit(editor)
                self.closeEditor.emit(editor, QStyledItemDelegate.SubmitModelCache)
        except:
            # Игнорируем ошибки, если редактор уже удален
            pass
