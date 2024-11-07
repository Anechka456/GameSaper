import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QStackedWidget, QWidget, QVBoxLayout, QLabel


class MyCustomWidget(QWidget):
    """Представляет собой пользовательский виджет"""

    def __init__(self, title):
        super().__init__()
        layout = QVBoxLayout()
        label = QLabel(title)
        layout.addWidget(label)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Приложение на PyQt6")
        self.setGeometry(100, 100, 300, 200)

        self.stacked_widget = QStackedWidget()

        # Добавляем первый виджет
        self.window1 = self.create_custom_widget("Это первое окно")
        self.stacked_widget.addWidget(self.window1)

        # Добавляем второй виджет
        self.window2 = self.create_custom_widget("Это второе окно")
        self.stacked_widget.addWidget(self.window2)

        # Устанавливаем QStackedWidget как центральный виджет
        self.setCentralWidget(self.stacked_widget)

        self.init_ui()

    def create_custom_widget(self, title):
        """Создает экземпляр MyCustomWidget с заданным заголовком"""
        return MyCustomWidget(title)

    def init_ui(self):
        """Инициализирует пользовательский интерфейс"""
        # Добавление кнопок для переключения между окнами
        button1 = QPushButton("Переключиться на первое окно")
        button1.clicked.connect(self.show_window1)

        button2 = QPushButton("Переключиться на второе окно")
        button2.clicked.connect(self.show_window2)

        # Помещаем кнопки в главное окно
        layout = QVBoxLayout()
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(self.stacked_widget)

        # Устанавливаем основной виджет
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def show_window1(self):
        """Показать первое окно"""
        self.stacked_widget.setCurrentIndex(0)

    def show_window2(self):
        """Показать второе окно"""
        self.stacked_widget.setCurrentIndex(1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec())
