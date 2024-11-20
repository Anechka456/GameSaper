from PyQt6 import uic
from PyQt6.QtWidgets import QWidget

menu_widget = []


class Menu(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("QT_files/untitled_menu.ui", self)  # Загружаем дизайн
        menu_widget.append([self.label, self.lvl, self.data, self.setting, 24])

    def level_button(self):
        return self.lvl

    def statistics_button(self):
        return self.data

    def setting_button(self):
        return self.setting
