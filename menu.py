import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget


class Menu(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("QT_files/untitled_menu.ui", self)  # Загружаем дизайн

    def level_button(self):
        return self.lvl

    def statistics_button(self):
        return self.data

    def setting_button(self):
        return self.setting


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Menu()
    ex.show()
    sys.exit(app.exec())

