import sqlite3
import sys

import random
import copy

from PyQt6 import uic
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtWidgets import QWidget, QPushButton, QButtonGroup, QMessageBox, QApplication


class Saper(QWidget):
    def __init__(self, size_row, size_col, lvl, time):
        super().__init__()
        self.size_row = size_row
        self.size_col = size_col
        self.lvl = lvl
        self.time = time
        uic.loadUi("QT_files/untitled_field.ui", self)  # Загружаем дизайн

        if time == '-1':
            self.warning.setVisible(False)
            self.warning2.setVisible(False)
        else:
            self.warning2.setText(f' Чтобы разминировать это поле вам даётся: {self.time}c ')

        self.initUI()

    def initUI(self):
        # задаём размеры поля
        self.size_field = (self.size_row, self.size_col)
        self.size_x = self.size_field[0]
        self.size_y = self.size_field[1]

        self.secondary_field = [[[] for _ in range(self.size_x)] for _ in range(self.size_y)]
        self.hidden_field = [[[] for _ in range(self.size_x)] for _ in range(self.size_y)]
        self.possible_bombs = []  # координаты клеток где можно поставить бомбы
        self.flag_points = []  # координаты клеток где стоит флажок

        for i in range(len(self.secondary_field)):
            for j in range(len(self.secondary_field[i])):
                self.possible_bombs.append((i, j))

        # кол-во бомб
        self.number_bombs = int(self.size_field[0] * self.size_field[1] * 0.2)
        # кол-во закрытых клеток не учитывая бомбы
        self.all_number_cells = self.size_x * self.size_y - self.number_bombs

        self.field_creation_flag = True  # флаг, нужно создовать новое поле или нет

        self.game_active = True

        self.button_coordinates = []

        self.number_open_cells = 0  # кол-во открытых клеток

        self.field_group = QButtonGroup()

        # создаём таймер
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.current_time = 0

        # отображаем поле
        self.gridLayout.setHorizontalSpacing(self.size_field[0])
        self.gridLayout.setVerticalSpacing(self.size_field[1])
        self.gridLayout.setSpacing(0)  # Промежутки между кнопками
        self.gridLayout.setContentsMargins(0, 0, 0, 0)  # Отступы вокруг сетки

        # расставляем кнопки
        x, y = 0, 0
        for i in range(self.size_field[0]):
            row_button_coordinates = []
            for j in range(self.size_field[1]):
                self.button = QPushButton('', self)
                self.button.setStyleSheet("border-image : url(Img/cell.jpg);")
                self.field_group.addButton(self.button)
                row_button_coordinates.append(self.button)
                size_button = int((min(self.width(), self.height()) // max(self.size_field)) / 1.54)
                self.button.setFixedSize(size_button, size_button)
                self.gridLayout.addWidget(self.button, i, j)
                self.button.move(x, y)
                x += 50
            self.button_coordinates.append(row_button_coordinates)
            x = 0
            y += 50

        # обробатываем нажатие кнопок мыши
        for i in self.field_group.buttons():
            i.clicked.connect(self.run_left)  # нажатие левой кнопкой мыши
            i.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
            i.customContextMenuRequested.connect(self.run_right)  # нажатие правой кнопкой мыши

        self.new_game.setStyleSheet("border-image : url(Img/emoji.jpg);")
        self.new_game.clicked.connect(self.func_new_game)

        # отображаем уровень и размер поля
        self.lvl_field.setText(f"Уровень: {self.lvl}")
        self.size_field_label.setText(f"Размер поля: {self.size_x} * {self.size_y}")

    def update_time(self):
        """функция осуществляет таймер"""
        self.current_time += 1
        self.time_field.display(self.current_time)
        if self.current_time == self.time:
            self.end_game()

    def func_new_game(self):
        """функция начинает новую игру"""
        self.timer.stop()
        self.new_game.setStyleSheet("border-image : url(Img/emoji.jpg);")
        self.time_field.display(0)
        self.current_time = 0
        self.number_open_cells = 0
        self.secondary_field = [[[] for _ in range(self.size_x)] for _ in range(self.size_y)]
        self.hidden_field = [[[] for _ in range(self.size_x)] for _ in range(self.size_y)]
        self.progres_field.setValue(0)
        self.possible_bombs = []
        for i in range(len(self.secondary_field)):
            for j in range(len(self.secondary_field[i])):
                self.possible_bombs.append((i, j))
        self.flag_points = []
        self.field_creation_flag = True
        for i in self.button_coordinates:
            for but in i:
                but.setStyleSheet("border-image : url(Img/cell.jpg);")
                but.setEnabled(True)
                but.setText('')
        self.game_active = True

    def creating_field(self, kor):
        """функция создаёт поле"""

        self.field_creation_flag = False

        # рассчитываем кол-во бомб и раставляем их
        del self.possible_bombs[self.possible_bombs.index(kor)]
        self.number_bombs = int(self.size_field[0] * self.size_field[1] * 0.2)
        self.all_number_cells = self.size_x * self.size_y - self.number_bombs
        self.bomb_field.display(self.number_bombs)
        coordinates_bomb = random.sample(self.possible_bombs, self.number_bombs)
        for i in coordinates_bomb:
            self.hidden_field[i[0]][i[1]] = '*'

        # создаем такой же список поля и делаем ему рамку чтобы не писать дополнительные условия
        poleframe = copy.deepcopy(self.hidden_field)
        poleframe.append([[] for _ in range(self.size_x)])
        poleframe.insert(0, [[] for _ in range(self.size_x)])
        for i in poleframe:
            i.append([])
            i.insert(0, [])

        # расставляем цифры
        for row in range(len(self.hidden_field)):
            row = row + 1
            for col in range(len(self.hidden_field[row - 1])):
                kol_bomb = 0
                col = col + 1
                if poleframe[row][col] == '*':
                    continue
                if poleframe[row][col - 1] == '*':
                    kol_bomb += 1
                if poleframe[row - 1][col - 1] == '*':
                    kol_bomb += 1
                if poleframe[row - 1][col] == '*':
                    kol_bomb += 1
                if poleframe[row - 1][col + 1] == '*':
                    kol_bomb += 1
                if poleframe[row][col + 1] == '*':
                    kol_bomb += 1
                if poleframe[row + 1][col + 1] == '*':
                    kol_bomb += 1
                if poleframe[row + 1][col] == '*':
                    kol_bomb += 1
                if poleframe[row + 1][col - 1] == '*':
                    kol_bomb += 1
                self.hidden_field[row - 1][col - 1] = kol_bomb

        self.timer.start(1000)

    def open_cell(self, coordinates):
        # возращаем True если клетка уже открытка
        if self.secondary_field[coordinates[0]][coordinates[1]] != []:
            return True

        self.button_coordinates[coordinates[0]][coordinates[1]].setEnabled(False)  # Отключаем кнопку
        self.number_open_cells += 1

        # открываем клетку
        self.secondary_field[coordinates[0]][coordinates[1]] = self.hidden_field[coordinates[0]][coordinates[1]]
        # меняем изображение кнопки
        self.adding_cell_image(coordinates, self.hidden_field[coordinates[0]][coordinates[1]])

        # открываем соседние клетки если клетка нулевая
        if self.secondary_field[coordinates[0]][coordinates[1]] == 0:
            row, col = coordinates[0], coordinates[1]

            if 0 <= row < self.size_x and 0 <= col - 1 < self.size_y:
                if self.hidden_field[row][col - 1] != '*' and self.secondary_field[row][col - 1] != 'F':
                    self.open_cell((row, col - 1))

            if 0 <= row - 1 < self.size_x and 0 <= col - 1 < self.size_y:
                if self.hidden_field[row - 1][col - 1] != '*' and self.secondary_field[row - 1][col - 1] != 'F':
                    self.open_cell((row - 1, col - 1))

            if 0 <= row - 1 < self.size_x and 0 <= col < self.size_y:
                if self.hidden_field[row - 1][col] != '*' and self.secondary_field[row - 1][col] != 'F':
                    self.open_cell((row - 1, col))

            if 0 <= row - 1 < self.size_x and 0 <= col + 1 < self.size_y:
                if self.hidden_field[row - 1][col + 1] != '*' and self.secondary_field[row - 1][col + 1] != 'F':
                    self.open_cell((row - 1, col + 1))

            if 0 <= row < self.size_x and 0 <= col + 1 < self.size_y:
                if self.hidden_field[row][col + 1] != '*' and self.secondary_field[row][col + 1] != 'F':
                    self.open_cell((row, col + 1))

            if 0 <= row + 1 < self.size_x and 0 <= col + 1 < self.size_y:
                if self.hidden_field[row + 1][col + 1] != '*' and self.secondary_field[row + 1][col + 1] != 'F':
                    self.open_cell((row + 1, col + 1))

            if 0 <= row + 1 < self.size_x and 0 <= col < self.size_y:
                if self.hidden_field[row + 1][col] != '*' and self.secondary_field[row + 1][col] != 'F':
                    self.open_cell((row + 1, col))

            if 0 <= row + 1 < self.size_x and 0 <= col - 1 < self.size_y:
                if self.hidden_field[row + 1][col - 1] != '*' and self.secondary_field[row + 1][col - 1] != 'F':
                    self.open_cell((row + 1, col - 1))

    def flag_cell(self, kor):
        """функция ставит флаг"""
        self.secondary_field[kor[0]][kor[1]] = "F"
        self.button_coordinates[kor[0]][kor[1]].setText('🚩')
        self.bomb_field.display(self.bomb_field.intValue() - 1)

    def open_flag_cell(self, kor):
        """функция убирает флаг"""
        self.secondary_field[kor[0]][kor[1]] = []
        self.button_coordinates[kor[0]][kor[1]].setText('')
        self.bomb_field.display(self.bomb_field.intValue() + 1)

    def print_field(self):
        for row in self.secondary_field:
            st = []
            for col in row:
                if col == []:
                    st.append(col)
                    continue
                el = f"{col}"
                st.append(el.rjust(2, ' '))
            print(*st)

    def print_hidden_field(self):
        for row in self.hidden_field:
            st = []
            for col in row:
                if col == []:
                    st.append(col)
                    continue
                el = f"{col}"
                st.append(el.rjust(2, ' '))
            print(*st)

    def display_hidden_field(self):
        for row in range(len(self.hidden_field)):
            for col in range(len(self.hidden_field[row])):
                if self.hidden_field[row][col] == '*' and self.secondary_field[row][col] != 'F':
                    self.adding_bomb_image((row, col))
                    continue
                self.open_cell((row, col))

    def cheats(self):
        for row in range(len(self.hidden_field)):
            for col in range(len(self.hidden_field[row])):
                self.button_coordinates[row][col].setText(str(self.hidden_field[row][col]))

    def keyPressEvent(self, event):
        try:
            # Проверяем, нажата ли комбинация Ctrl+D
            if event.key() == Qt.Key.Key_D and event.modifiers() == Qt.KeyboardModifier.ControlModifier:
                self.cheats()
        except Exception as e:
            print(f"Ошибка в keyPressEvent: {e}")

    def check_win(self):
        """функция проверяет победил игрок или нет"""
        for row in range(self.size_x):
            for col in range(self.size_y):
                if self.hidden_field[row][col] != '*' and self.secondary_field[row][col] == []:
                    return False
        return True

    def end_game_over(self):
        """функция выводит сообщение о том, что игрок проиграл"""
        self.timer.stop()
        self.new_game.setStyleSheet("border-image : url(Img/emoji_died.jpg);")
        self.current_time = 0
        self.game_active = False
        self.display_hidden_field()
        QMessageBox.information(self, "Game Over", "Вы наткнулись на бомбу!")

    def end_game(self):
        """функция выводит сообщение о том, что игрок не смог разминировать поле за заданное время"""
        self.timer.stop()
        self.new_game.setStyleSheet("border-image : url(Img/emoji_died.jpg);")
        self.current_time = 0
        self.game_active = False
        self.display_hidden_field()
        QMessageBox.information(self, "Game Over", "Время истекло! Попробуйте еще раз.")

    def end_game_win(self):
        """функция выводит сообщение о том, что игрок победил"""
        self.timer.stop()
        self.adding_victory(self.current_time)
        self.current_time = 0
        QMessageBox.information(self, "Поздравляем!", "Вы открыли все безопасные клетки!")
        self.game_active = False

    def completion_progressbar(self):
        """функция отоброжает прогресс"""
        progress = (self.number_open_cells * 100) // self.all_number_cells
        self.progres_field.setValue(progress)

    def run_left(self):
        """функция выпоняет действие при нажатии левой кнопкой мыши"""
        if self.game_active:
            row, col = 0, 0
            for row_b in range(len(self.button_coordinates)):
                for col_b in range(len(self.button_coordinates[row_b])):
                    if self.button_coordinates[row_b][col_b] == self.sender():
                        row, col = row_b, self.button_coordinates[row_b].index(self.sender())
                        break
            if self.field_creation_flag:
                self.creating_field((row, col))
            if self.secondary_field[row][col] == 'F':
                return
            elif self.hidden_field[row][col] != '*':
                self.open_cell((row, col))
                self.completion_progressbar()
            else:
                return self.end_game_over()
            if self.check_win():
                return self.end_game_win()

    def run_right(self):
        """функция выпоняет действие при нажатии правой кнопкой мыши"""
        row, col = 0, 0
        for row_b in range(len(self.button_coordinates)):
            for col_b in range(len(self.button_coordinates[row_b])):
                if self.button_coordinates[row_b][col_b] == self.sender():
                    row, col = row_b, self.button_coordinates[row_b].index(self.sender())
                    break
        if (row, col) not in self.flag_points:
            self.flag_points.append((row, col))
            self.flag_cell((row, col))
        else:
            del self.flag_points[self.flag_points.index((row, col))]
            self.open_flag_cell((row, col))

    def exit_button(self):
        return self.exit

    def adding_victory(self, duration):
        """Функция добавляет в БД запись о победе"""
        con = sqlite3.connect("db/victory_data")
        cur = con.cursor()
        max_id = cur.execute("SELECT max(id) FROM victory").fetchone()[0]
        if max_id is None:
            max_id = 1
        else:
            max_id += 1
        cur.execute(f"""INSERT INTO durations(id, duration) VALUES({max_id}, {duration})""")
        cur.execute(
            f"""INSERT INTO level(id, name, size) VALUES({max_id}, '{self.lvl}', '{self.size_x} * {self.size_y}')""")
        cur.execute(f"""INSERT INTO victory(lvl, time) VALUES({max_id}, {max_id})""")
        con.commit()

    def adding_cell_image(self, coordinates, num):
        """Функция изменят изображение кнопки на определённую цифру"""
        if num == 0:
            self.button_coordinates[coordinates[0]][coordinates[1]].setStyleSheet(
                f"border-image : url(Img/open_cell.jpg);")
            return
        self.button_coordinates[coordinates[0]][coordinates[1]].setStyleSheet(
            f"border-image : url(Img/cell_{num}.jpg);")

    def adding_bomb_image(self, coordinates):
        """Функция изменят изображение кнопки на бомбу"""
        self.button_coordinates[coordinates[0]][coordinates[1]].setStyleSheet(f"border-image : url(Img/cell_bomb.jpg);")


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Saper(8, 8, 1, '-1')
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())