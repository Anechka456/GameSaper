from PyQt6 import uic
from PyQt6.QtWidgets import QWidget


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
