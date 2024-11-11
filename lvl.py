import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget


class Lvl(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("QT_files/untitled_lvl.ui", self)  # Загружаем дизайн

    def level_1(self):
        return self.lvl1

    def level_2(self):
        return self.lvl2

    def level_3(self):
        return self.lvl3

    def level_4(self):
        return self.lvl4

    def level_time_1(self):
        return self.time_lvl1

    def level_time_2(self):
        return self.time_lvl2

    def level_time_3(self):
        return self.time_lvl3

    def level_time_4(self):
        return self.time_lvl4

    def exit_button(self):
        return self.exit


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Lvl()
    ex.show()
    sys.exit(app.exec())

