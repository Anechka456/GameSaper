import sys

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget

from saper import Saper
from setting import Setting
from lvl import Lvl
from menu import Menu


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Приложение на PyQt6")
        self.setGeometry(100, 100, 1089, 876)  # x, y, width, height
        self.setWindowTitle('Сапёр')
        self.setWindowIcon(QIcon("Img/ikonka_saper.png"))

        # Создаем виджет для переключения между окнами
        self.stacked_widget = QStackedWidget()

        # Создаем окна
        self.menu = self.create_window1()
        self.setting = self.create_window2()
        self.lvl = self.create_window3()
        self.saper_lvl1 = self.create_window4((8, 8), '1')
        self.saper_lvl2 = self.create_window4((10, 10), '2')
        self.saper_lvl3 = self.create_window4((10, 15), '3')
        self.saper_lvl4 = self.create_window4((15, 15), '4')
        # self.time_saper = self.create_window5() в разработке

        # Добавляем окна в QStackedWidget
        self.stacked_widget.addWidget(self.menu)
        self.stacked_widget.addWidget(self.setting)
        self.stacked_widget.addWidget(self.lvl)
        self.stacked_widget.addWidget(self.saper_lvl1)
        self.stacked_widget.addWidget(self.saper_lvl2)
        self.stacked_widget.addWidget(self.saper_lvl3)
        self.stacked_widget.addWidget(self.saper_lvl4)
        # self.stacked_widget.addWidget(self.time_saper)

        # Устанавливаем QStackedWidget как центральный виджет
        self.setCentralWidget(self.stacked_widget)

    def create_window1(self):
        """Создание окна меню"""
        self.menu = Menu()

        level_selection_button = self.menu.level_button()
        level_selection_button.clicked.connect(self.show_window3)

        settings_button = self.menu.setting_button()
        settings_button.clicked.connect(self.show_window2)

        return self.menu

    def create_window2(self):
        """Создание окна настроек"""
        self.setting = Setting()

        back_button = self.setting.exit_button()
        back_button.clicked.connect(self.show_window1)

        return self.setting

    def create_window3(self):
        """Создание окна выбора уровня"""
        self.lvl = Lvl()

        back_button = self.lvl.exit_button()
        back_button.clicked.connect(self.show_window1)

        button_level_1 = self.lvl.level_1()
        button_level_1.clicked.connect(self.show_window4)

        button_level_2 = self.lvl.level_2()
        button_level_2.clicked.connect(self.show_window5)

        button_level_3 = self.lvl.level_3()
        button_level_3.clicked.connect(self.show_window6)

        button_level_4 = self.lvl.level_4()
        button_level_4.clicked.connect(self.show_window7)

        return self.lvl

    def create_window4(self, size, lvl):
        """Создание окна игры сапер"""
        self.saper = Saper(size[0], size[1], lvl)

        back_button = self.saper.exit_button()
        back_button.clicked.connect(self.show_window3)
        return self.saper

    def show_window1(self):
        """Показать первое окно"""
        self.stacked_widget.setCurrentIndex(0)

    def show_window2(self):
        """Показать второе окно"""
        self.stacked_widget.setCurrentIndex(1)

    def show_window3(self):
        """Показать окно выбора уровня"""
        self.stacked_widget.setCurrentIndex(2)

    def show_window4(self):
        """Показать окно 1 уровня"""
        self.stacked_widget.setCurrentIndex(3)

    def show_window5(self):
        """Показать окно 2 уровня"""
        self.stacked_widget.setCurrentIndex(4)

    def show_window6(self):
        """Показать окно 3 уровня"""
        self.stacked_widget.setCurrentIndex(5)

    def show_window7(self):
        """Показать окно 3 уровня"""
        self.stacked_widget.setCurrentIndex(6)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec())
