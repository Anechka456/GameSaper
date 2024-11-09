import io
import sys

from PyQt6 import uic  # Импортируем uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget

template_lvl = """<?xml version="1.0" encoding="UTF-8"?>
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
  <widget class="QLabel" name="label_2">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>310</y>
     <width>271</width>
     <height>41</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font: 20pt &quot;MS Shell Dlg 2&quot;;
color: rgb(136, 23, 9);</string>
   </property>
   <property name="text">
    <string>Сапёр тайм-аут</string>
   </property>
  </widget>
  <widget class="QPushButton" name="time_lvl1">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>370</y>
     <width>241</width>
     <height>201</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">color: rgb(93, 0, 1);
font: 16pt &quot;MS Shell Dlg 2&quot;;
background-color: rgb(139, 103, 103);</string>
   </property>
   <property name="text">
    <string>Time attack LVL 1</string>
   </property>
  </widget>
  <widget class="QPushButton" name="lvl3">
   <property name="geometry">
    <rect>
     <x>550</x>
     <y>80</y>
     <width>241</width>
     <height>201</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">color: rgb(93, 0, 1);
font: 16pt &quot;MS Shell Dlg 2&quot;;
background-color: rgb(139, 103, 103);</string>
   </property>
   <property name="text">
    <string>3 LVL</string>
   </property>
  </widget>
  <widget class="QPushButton" name="lvl2">
   <property name="geometry">
    <rect>
     <x>280</x>
     <y>80</y>
     <width>241</width>
     <height>201</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">color: rgb(93, 0, 1);
font: 16pt &quot;MS Shell Dlg 2&quot;;
background-color: rgb(139, 103, 103);</string>
   </property>
   <property name="text">
    <string>2 LVL</string>
   </property>
  </widget>
  <widget class="QLabel" name="label">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>20</y>
     <width>271</width>
     <height>41</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font: 20pt &quot;MS Shell Dlg 2&quot;;
color: rgb(136, 23, 9);</string>
   </property>
   <property name="text">
    <string>Сапёр</string>
   </property>
  </widget>
  <widget class="QPushButton" name="time_lvl2">
   <property name="geometry">
    <rect>
     <x>280</x>
     <y>370</y>
     <width>241</width>
     <height>201</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">color: rgb(93, 0, 1);
font: 16pt &quot;MS Shell Dlg 2&quot;;
background-color: rgb(139, 103, 103);</string>
   </property>
   <property name="text">
    <string>Time attack LVL 2</string>
   </property>
  </widget>
  <widget class="QPushButton" name="lvl1">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>80</y>
     <width>241</width>
     <height>201</height>
    </rect>
   </property>
   <property name="layoutDirection">
    <enum>Qt::LeftToRight</enum>
   </property>
   <property name="styleSheet">
    <string notr="true">color: rgb(93, 0, 1);
font: 16pt &quot;MS Shell Dlg 2&quot;;
background-color: rgb(139, 103, 103);</string>
   </property>
   <property name="text">
    <string>1 LVL</string>
   </property>
   <property name="shortcut">
    <string/>
   </property>
  </widget>
  <widget class="QPushButton" name="time_lvl3">
   <property name="geometry">
    <rect>
     <x>550</x>
     <y>370</y>
     <width>241</width>
     <height>201</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">color: rgb(93, 0, 1);
font: 16pt &quot;MS Shell Dlg 2&quot;;
background-color: rgb(139, 103, 103);</string>
   </property>
   <property name="text">
    <string>Time attack LVL 3</string>
   </property>
  </widget>
  <widget class="QPushButton" name="exit">
   <property name="geometry">
    <rect>
     <x>910</x>
     <y>20</y>
     <width>171</width>
     <height>41</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">color: rgb(93, 0, 1);
font: 14pt &quot;MS Shell Dlg 2&quot;;
background-color: rgb(139, 103, 103);</string>
   </property>
   <property name="text">
    <string>Назад</string>
   </property>
  </widget>
  <widget class="QPushButton" name="lvl4">
   <property name="geometry">
    <rect>
     <x>820</x>
     <y>80</y>
     <width>241</width>
     <height>201</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">color: rgb(93, 0, 1);
font: 16pt &quot;MS Shell Dlg 2&quot;;
background-color: rgb(139, 103, 103);</string>
   </property>
   <property name="text">
    <string>4 LVL</string>
   </property>
  </widget>
  <widget class="QPushButton" name="time_lvl4">
   <property name="geometry">
    <rect>
     <x>820</x>
     <y>370</y>
     <width>241</width>
     <height>201</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">color: rgb(93, 0, 1);
font: 16pt &quot;MS Shell Dlg 2&quot;;
background-color: rgb(139, 103, 103);</string>
   </property>
   <property name="text">
    <string>Time attack LVL 4</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class Lvl(QWidget):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template_lvl)
        uic.loadUi(f, self)  # Загружаем дизайн

    def level_1(self):
        return self.lvl1

    def level_2(self):
        return self.lvl2

    def level_3(self):
        return self.lvl3

    def level_4(self):
        return self.lvl4

    def exit_button(self):
        return self.exit


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Lvl()
    ex.show()
    sys.exit(app.exec())

