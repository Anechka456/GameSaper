import sys
import io
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QStackedWidget, QWidget, QVBoxLayout, QLabel

from saper import Saper, template_saper
from lvl import Lvl, template_lvl
from menu import Menu, template_menu


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Приложение на PyQt6")
        self.setGeometry(100, 100, 1089, 876)  # x, y, width, height

        # Создаем виджет для переключения между окнами
        self.stacked_widget = QStackedWidget()

        # Создаем два окна
        self.menu = self.create_window1()
        # self.setting = self.create_window2() в разработке
        self.lvl = self.create_window3()
        # self.saper = self.create_window4() в разработке
        # self.time_saper = self.create_window5() в разработке

        # Добавляем окна в QStackedWidget
        self.stacked_widget.addWidget(self.menu)
        # self.stacked_widget.addWidget(self.setting)
        self.stacked_widget.addWidget(self.lvl)
        # self.stacked_widget.addWidget(self.saper)
        # self.stacked_widget.addWidget(self.time_saper)

        # Устанавливаем QStackedWidget как центральный виджет
        self.setCentralWidget(self.stacked_widget)

    def create_window1(self):
        """Создание окна меню"""
        self.menu = Menu()

        level_selection_button = self.menu.login_button()
        level_selection_button.clicked.connect(self.show_window3)  # Переключаем на окно выбор уровня при нажатии

        return self.menu

    # def create_window2(self):
    #     """Создание окна настроек"""
    #     widget = QWidget()
    #     layout = QVBoxLayout()
    #
    #     label = QLabel("Это 1второе окно")
    #     button = QPushButton("Вернуться назад")
    #     button.clicked.connect(self.show_window1)  # Переключаем на первое окно при нажатии
    #
    #     layout.addWidget(label)
    #     layout.addWidget(button)
    #     widget.setLayout(layout)
    #
    #     return widget

    def create_window3(self):
        """Создание окна выбора уровня"""
        self.lvl = Lvl()

        back_button = self.lvl.back_button()
        back_button.clicked.connect(self.show_window1)  # Переключаем на первое окно при нажатии

        return self.lvl

    # def create_window4(self):
    #     """Создание второго окна"""
    #     widget = QWidget()
    #     layout = QVBoxLayout()
    #
    #     label = QLabel("Это 2второе окно")
    #     button = QPushButton("Вернуться назад")
    #     button.clicked.connect(self.show_window1)  # Переключаем на первое окно при нажатии
    #
    #     layout.addWidget(label)
    #     layout.addWidget(button)
    #     widget.setLayout(layout)
    #
    #     return widget

    def show_window1(self):
        """Показать первое окно"""
        self.stacked_widget.setCurrentIndex(0)

    def show_window2(self):
        """Показать второе окно"""
        self.stacked_widget.setCurrentIndex(1)

    def show_window3(self):
        """Показать окно выбора уровня"""
        self.stacked_widget.setCurrentIndex(1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec())
