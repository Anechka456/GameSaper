import io
import sys

from PyQt6 import uic  # Импортируем uic
from PyQt6.QtWidgets import QApplication, QMainWindow

template_menu = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>984</width>
    <height>789</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>200</x>
      <y>140</y>
      <width>581</width>
      <height>151</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">font: 28pt &quot;MS Shell Dlg 2&quot;;</string>
    </property>
    <property name="text">
     <string>Сапёр</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QPushButton" name="setting">
    <property name="geometry">
     <rect>
      <x>240</x>
      <y>480</y>
      <width>501</width>
      <height>61</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">font: 18pt &quot;MS Shell Dlg 2&quot;;</string>
    </property>
    <property name="text">
     <string>Настройки</string>
    </property>
   </widget>
   <widget class="QPushButton" name="awards">
    <property name="geometry">
     <rect>
      <x>240</x>
      <y>400</y>
      <width>501</width>
      <height>61</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">font: 20pt &quot;MS Shell Dlg 2&quot;;</string>
    </property>
    <property name="text">
     <string>Награды</string>
    </property>
   </widget>
   <widget class="QPushButton" name="lvl">
    <property name="geometry">
     <rect>
      <x>240</x>
      <y>300</y>
      <width>501</width>
      <height>81</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">font: 24pt &quot;MS Shell Dlg 2&quot;;</string>
    </property>
    <property name="text">
     <string>Выбор уровня</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>984</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template_menu)
        uic.loadUi(f, self)  # Загружаем дизайн


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Menu()
    ex.show()
    sys.exit(app.exec())

