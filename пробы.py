import sys
from PyQt6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.mouse_button_pressed = None  # Переменная для хранения нажатой кнопки мыши

    def initUI(self):
        layout = QVBoxLayout()

        # Создаем 4 кнопки
        self.button1 = QPushButton("Кнопка 1")
        self.button2 = QPushButton("Кнопка 2")
        self.button3 = QPushButton("Кнопка 3")
        self.button4 = QPushButton("Кнопка 4")

        # Подключаем обработчик нажатий к каждой кнопке
        self.button1.clicked.connect(self.button_clicked)
        self.button2.clicked.connect(self.button_clicked)
        self.button3.clicked.connect(self.button_clicked)
        self.button4.clicked.connect(self.button_clicked)

        # Добавляем кнопки в layout
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)

        self.setLayout(layout)
        self.setWindowTitle("Обработка нажатий кнопок")
        self.setGeometry(100, 100, 300, 200)
        self.show()

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.mouse_button_pressed = "левая"
        elif event.button() == Qt.MouseButton.RightButton:
            self.mouse_button_pressed = "правая"
        elif event.button() == Qt.MouseButton.MiddleButton:
            self.mouse_button_pressed = "средняя"
        else:
            self.mouse_button_pressed = None

    def button_clicked(self):
        # Узнаем, какая кнопка была нажата
        sender = self.sender()  # Получаем объект кнопки
        button_name = sender.text()

        # Используем информацию о нажатой кнопке мыши
        button_pressed = self.mouse_button_pressed if self.mouse_button_pressed else "неизвестная"

        # Выводим результат
        print(f"{button_name} была нажата с {button_pressed} кнопкой мыши.")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())
