import io
import sys

import random
import copy

from PyQt6 import uic
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QButtonGroup, QMessageBox


template_saper = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1089</width>
    <height>876</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <widget class="QLabel" name="lvl_field">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>10</y>
     <width>331</width>
     <height>31</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font: 14pt &quot;MS Shell Dlg 2&quot;;
color: rgb(106, 0, 0);</string>
   </property>
   <property name="text">
    <string>Уровень:</string>
   </property>
  </widget>
  <widget class="QLabel" name="size_field_label">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>60</y>
     <width>271</width>
     <height>31</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font: 14pt &quot;MS Shell Dlg 2&quot;;
color: rgb(106, 0, 0);</string>
   </property>
   <property name="text">
    <string>Размер поля:</string>
   </property>
  </widget>
  <widget class="QLabel" name="label_3">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>110</y>
     <width>91</width>
     <height>31</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font: 14pt &quot;MS Shell Dlg 2&quot;;
color: rgb(106, 0, 0);</string>
   </property>
   <property name="text">
    <string>Прогресс:</string>
   </property>
  </widget>
  <widget class="QProgressBar" name="progres_field">
   <property name="geometry">
    <rect>
     <x>110</x>
     <y>120</y>
     <width>351</width>
     <height>23</height>
    </rect>
   </property>
   <property name="value">
    <number>0</number>
   </property>
  </widget>
  <widget class="QPushButton" name="exit">
   <property name="geometry">
    <rect>
     <x>930</x>
     <y>20</y>
     <width>141</width>
     <height>41</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font: 14pt &quot;MS Shell Dlg 2&quot;;
color: rgb(125, 0, 0);
background-color: rgb(170, 114, 114);</string>
   </property>
   <property name="text">
    <string>Выход</string>
   </property>
  </widget>
  <widget class="QLCDNumber" name="time_field">
   <property name="geometry">
    <rect>
     <x>291</x>
     <y>181</y>
     <width>71</width>
     <height>41</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: rgb(0, 0, 0);
color: rgb(202, 0, 0);
font: 16pt &quot;MS Shell Dlg 2&quot;;</string>
   </property>
  </widget>
  <widget class="QLCDNumber" name="bomb_field">
   <property name="geometry">
    <rect>
     <x>780</x>
     <y>180</y>
     <width>71</width>
     <height>41</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: rgb(0, 0, 0);
color: rgb(202, 0, 0);</string>
   </property>
  </widget>
  <widget class="QPushButton" name="new_game">
   <property name="enabled">
    <bool>true</bool>
   </property>
   <property name="geometry">
    <rect>
     <x>550</x>
     <y>170</y>
     <width>51</width>
     <height>51</height>
    </rect>
   </property>
   <property name="text">
    <string>Смайлик</string>
   </property>
  </widget>
  <widget class="QWidget" name="gridLayoutWidget">
   <property name="geometry">
    <rect>
     <x>290</x>
     <y>230</y>
     <width>561</width>
     <height>621</height>
    </rect>
   </property>
   <layout class="QGridLayout" name="gridLayout"/>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class Saper(QWidget):
    def __init__(self, size_row, size_col, lvl):
        super().__init__()
        self.size_row = size_row
        self.size_col = size_col
        self.lvl = lvl
        f = io.StringIO(template_saper)
        uic.loadUi(f, self)  # Загружаем дизайн
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

        self.field_creation_flag = True  # флаг, нужно создовать новое поле или нет

        self.game_active = True

        self.button_coordinates = []

        self.number_open_cells = 0  # кол-во открытых клеток
        self.all_number_cells = 0  # кол-во закрытых клеток не учитывая бомбы

        self.field_group = QButtonGroup()

        # таймер
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.current_time = 0

        # отоброжаем поле
        self.gridLayout.setHorizontalSpacing(self.size_field[0])
        self.gridLayout.setVerticalSpacing(self.size_field[1])
        self.gridLayout.setSpacing(0)  # Промежутки между кнопками
        self.gridLayout.setContentsMargins(0, 0, 0, 0)  # Отступы вокруг сетки

        x, y = 0, 0
        for i in range(self.size_field[0]):
            row_button_coordinates = []
            for j in range(self.size_field[1]):
                self.button = QPushButton('', self)
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

        self.new_game.clicked.connect(self.func_new_game)

        # отоброжаем уровень и размер поля
        self.lvl_field.setText(f"Уровен: {self.lvl}")
        self.size_field_label.setText(f"Размер поля: {self.size_x} * {self.size_y}")

    def update_time(self):
        # таймер
        self.current_time += 1
        self.time_field.display(self.current_time)

    def func_new_game(self):
        # новая игра
        self.timer.stop()
        self.current_time = 0
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
                but.setEnabled(True)
                but.setText('')
        self.game_active = True

    def creating_field(self, kor):
        # создём поле и расставляем бомбы на нем

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

    def open_cell(self, kor):
        # открытие клетки

        # возращаем True если клетка уже открытка
        if self.secondary_field[kor[0]][kor[1]] != []:
            return True

        self.button_coordinates[kor[0]][kor[1]].setEnabled(False)  # Отключаем кнопку
        self.number_open_cells += 1

        # открываем клетку
        self.secondary_field[kor[0]][kor[1]] = self.hidden_field[kor[0]][kor[1]]
        self.button_coordinates[kor[0]][kor[1]].setText(str(self.hidden_field[kor[0]][kor[1]]))

        # открываем соседние клетки если клетка нулевая
        if self.secondary_field[kor[0]][kor[1]] == 0:
            row, col = kor[0], kor[1]

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
        # ставим флаг
        self.secondary_field[kor[0]][kor[1]] = "F"
        self.button_coordinates[kor[0]][kor[1]].setText('🚩')
        self.bomb_field.display(self.bomb_field.intValue() - 1)

    def open_flag_cell(self, kor):
        # убираем флаг
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
                self.button_coordinates[row][col].setText(str(self.hidden_field[row][col]))
                self.button_coordinates[row][col].setEnabled(True)

    def check_win(self):
        # проверка победил игрок или нет
        for row in range(self.size_x):
            for col in range(self.size_y):
                if self.hidden_field[row][col] != '*' and self.secondary_field[row][col] == []:
                    return False
        return True

    def end_game(self):
        # выводим сообщение о том, что игрок проиграл
        self.timer.stop()
        self.current_time = 0
        self.game_active = False
        self.display_hidden_field()
        QMessageBox.information(self, "Game Over", "Вы наткнулись на бомбу!")

    def end_game_win(self):
        # выводим сообщение о победе
        self.timer.stop()
        self.current_time = 0
        QMessageBox.information(self, "Поздравляем!", "Вы открыли все безопасные клетки!")
        self.game_active = False

    def completion_progressbar(self):
        # отоброжаем прогресс
        progress = (self.number_open_cells * 100) // (self.size_field[0] * self.size_field[1] - self.number_bombs)
        self.progres_field.setValue(progress)

    def run_left(self):
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
                return self.end_game()
            if self.check_win():
                return self.end_game_win()

    def run_right(self):
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


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Saper(10, 10, 1)
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
