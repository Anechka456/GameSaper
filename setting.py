from PyQt6 import uic
from PyQt6.QtGui import QPixmap, QBrush, QPalette
from PyQt6.QtWidgets import QWidget, QLabel


class Setting(QWidget):
    def __init__(self, windows):
        super().__init__()
        self.main_windows = windows
        uic.loadUi("QT_files/untitled_setting.ui", self)  # Загружаем дизайн
        self.initUI()

    def initUI(self):
        self.pixmap_forest = QPixmap('Img/forest.png')
        self.image_forest = QLabel(self)
        self.pixmap_forest = self.pixmap_forest.scaledToWidth(231)
        self.pixmap_forest = self.pixmap_forest.scaledToHeight(171)
        self.image_forest.move(100, 240)
        self.image_forest.resize(231, 171)
        self.image_forest.setPixmap(self.pixmap_forest)

        self.pixmap_mountains = QPixmap('Img/mountains.jpg')
        self.image_mountains = QLabel(self)
        self.pixmap_mountains = self.pixmap_mountains.scaledToWidth(231)
        self.pixmap_mountains = self.pixmap_mountains.scaledToHeight(171)
        self.image_mountains.move(420, 240)
        self.image_mountains.resize(231, 171)
        self.image_mountains.setPixmap(self.pixmap_mountains)

        self.pixmap_space = QPixmap('Img/space.jpg')
        self.image_space = QLabel(self)
        self.pixmap_space = self.pixmap_space.scaledToWidth(231)
        self.pixmap_space = self.pixmap_space.scaledToHeight(171)
        self.image_space.move(740, 240)
        self.image_space.resize(231, 171)
        self.image_space.setPixmap(self.pixmap_space)

        self.forest.clicked.connect(self.change_background_forest)
        self.mountains.clicked.connect(self.change_background_mountains)
        self.space.clicked.connect(self.change_background_space)

    def change_background_forest(self):
        """Функция устанавливает фон с изображением леса"""
        pixmap = QPixmap("Img/forest.png")
        pixmap = pixmap.scaled(self.size())
        palette = QPalette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(pixmap))
        self.main_windows.setPalette(palette)

    def change_background_mountains(self):
        """Функция устанавливает фон с изображением гор"""
        pixmap = QPixmap("Img/mountains.jpg")
        pixmap = pixmap.scaled(self.size())
        palette = QPalette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(pixmap))
        self.main_windows.setPalette(palette)

    def change_background_space(self):
        """Функция устанавливает фон с изображением космоса"""
        pixmap = QPixmap("Img/space.jpg")
        pixmap = pixmap.scaled(self.size())
        palette = QPalette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(pixmap))
        self.main_windows.setPalette(palette)

    def exit_button(self):
        return self.exit

    def login_button(self):
        return self.setting
