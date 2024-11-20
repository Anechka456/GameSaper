import sys
import sqlite3

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget, QTableWidgetItem

statistics_widget = []


class Statistics(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("QT_files/untitled_data_victory.ui", self)  # Загружаем дизайн
        statistics_widget.append([self.label, self.exit, self.max_victory, self.update_button, self.best_time,
                                  self.tableWidget, 18])

        self.update_button.clicked.connect(self.run)
        self.run()

    def run(self):
        self.update_results()
        self.number_wins()
        self.time()

    def update_results(self):
        """Функция выводит все результаты побед в таблицу"""
        con = sqlite3.connect("db/victory_data")
        cur = con.cursor()
        result = cur.execute("""SELECT users.name, level.name, level.size, victory.duration FROM victory 
                JOIN level ON victory.lvl = level.id 
                JOIN users ON victory.user = users.id""").fetchall()
        if result:
            # Заполяем размеры таблицы
            self.tableWidget.setRowCount(len(result))
            self.tableWidget.setColumnCount(len(result[0]))
            self.tableWidget.setHorizontalHeaderLabels(
                ['Игрок', 'Уровень', 'Размер поля', 'Время'])
            # Заполняем таблицу полученными элементами
            for i, elem in enumerate(result[::-1]):
                for j, val in enumerate(elem):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        con.close()

    def number_wins(self):
        """Функция высчитывет кол-во побед и выводит результат"""
        con = sqlite3.connect("db/victory_data")
        cur = con.cursor()
        result = cur.execute("""SELECT id FROM victory""").fetchall()
        if result:
            self.max_victory.setText(f' Всего побед: {len(result)}')
        con.close()

    def time(self):
        """Функция высчитывет лучшее время прохождение игры и выводит результат"""
        con = sqlite3.connect("db/victory_data")
        cur = con.cursor()
        result = cur.execute("""SELECT min(duration) FROM victory""").fetchone()[0]
        if result:
            self.best_time.setText(f' Лучшее время: {result}с.')
        con.close()

    def exit_button(self):
        return self.exit


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Statistics()
    ex.show()
    sys.exit(app.exec())

