import sys
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget

from saper import Saper
from setting import Setting
from lvl import Lvl
from menu import Menu
from statistics import Statistics


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
        self.statistics = self.create_window5()
        self.saper_lvl1 = self.create_window4((8, 8), '1', '-1')
        self.saper_lvl2 = self.create_window4((10, 10), '2', '-1')
        self.saper_lvl3 = self.create_window4((13, 13), '3', '-1')
        self.saper_lvl4 = self.create_window4((15, 15), '4', '-1')
        self.saper_time_lvl1 = self.create_window4((8, 8), '1 time-attack', 60)
        self.saper_time_lvl2 = self.create_window4((10, 10), '2 time-attack', 120)
        self.saper_time_lvl3 = self.create_window4((13, 13), '3 time-attack', 240)
        self.saper_time_lvl4 = self.create_window4((15, 15), '4 time-attack', 300)

        # Добавляем окна в QStackedWidget
        self.stacked_widget.addWidget(self.menu)
        self.stacked_widget.addWidget(self.setting)
        self.stacked_widget.addWidget(self.lvl)
        self.stacked_widget.addWidget(self.saper_lvl1)
        self.stacked_widget.addWidget(self.saper_lvl2)
        self.stacked_widget.addWidget(self.saper_lvl3)
        self.stacked_widget.addWidget(self.saper_lvl4)
        self.stacked_widget.addWidget(self.saper_time_lvl1)
        self.stacked_widget.addWidget(self.saper_time_lvl2)
        self.stacked_widget.addWidget(self.saper_time_lvl3)
        self.stacked_widget.addWidget(self.saper_time_lvl4)
        self.stacked_widget.addWidget(self.statistics)

        # Устанавливаем QStackedWidget как центральный виджет
        self.setCentralWidget(self.stacked_widget)

    def create_window1(self):
        """Создание окна меню"""
        self.menu = Menu()

        level_selection_button = self.menu.level_button()
        level_selection_button.clicked.connect(self.show_window3)

        settings_button = self.menu.setting_button()
        settings_button.clicked.connect(self.show_window2)

        statistics_button = self.menu.statistics_button()
        statistics_button.clicked.connect(self.show_window12)

        return self.menu

    def create_window2(self):
        """Создание окна настроек"""
        self.setting = Setting(self)

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

        button_level_time_1 = self.lvl.level_time_1()
        button_level_time_1.clicked.connect(self.show_window8)

        button_level_time_2 = self.lvl.level_time_2()
        button_level_time_2.clicked.connect(self.show_window9)

        button_level_time_3 = self.lvl.level_time_3()
        button_level_time_3.clicked.connect(self.show_window10)

        button_level_time_4 = self.lvl.level_time_4()
        button_level_time_4.clicked.connect(self.show_window11)

        return self.lvl

    def create_window4(self, size, lvl, time):
        """Создание окна игры сапер"""
        self.saper = Saper(size[0], size[1], lvl, time)

        back_button = self.saper.exit_button()
        back_button.clicked.connect(self.show_window3)
        return self.saper

    def create_window5(self):
        """Создание окна статистики побед"""
        self.statistics = Statistics()

        back_button = self.statistics.exit_button()
        back_button.clicked.connect(self.show_window1)

        return self.statistics

    def show_window1(self):
        """Показать окно меню"""
        self.stacked_widget.setCurrentIndex(0)

    def show_window2(self):
        """Показать окно настроек"""
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
        """Показать окно 4 уровня"""
        self.stacked_widget.setCurrentIndex(6)

    def show_window8(self):
        """Показать окно 1 уровня тайм-атака"""
        self.stacked_widget.setCurrentIndex(7)

    def show_window9(self):
        """Показать окно 2 уровня тайм-атака"""
        self.stacked_widget.setCurrentIndex(8)

    def show_window10(self):
        """Показать окно 3 уровня тайм-атака"""
        self.stacked_widget.setCurrentIndex(9)

    def show_window11(self):
        """Показать окно 4 уровня тайм-атака"""
        self.stacked_widget.setCurrentIndex(10)

    def show_window12(self):
        """Показать окно статистики побед"""
        self.stacked_widget.setCurrentIndex(11)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
