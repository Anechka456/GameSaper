import io
import sys

from PyQt6 import uic  # Импортируем uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget

template_menu = """<?xml version="1.0" encoding="UTF-8"?>
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
  <widget class="QLabel" name="label">
   <property name="geometry">
    <rect>
     <x>190</x>
     <y>190</y>
     <width>671</width>
     <height>191</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">color: rgb(170, 0, 0);
font: 36pt &quot;MS Shell Dlg 2&quot;;</string>
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
     <x>280</x>
     <y>450</y>
     <width>501</width>
     <height>81</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">color: rgb(74, 18, 11);
background-color: rgb(156, 138, 138);
font: 18pt &quot;MS UI Gothic&quot;;</string>
   </property>
   <property name="text">
    <string>Настройки</string>
   </property>
  </widget>
  <widget class="QPushButton" name="lvl">
   <property name="geometry">
    <rect>
     <x>280</x>
     <y>360</y>
     <width>501</width>
     <height>81</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">color: rgb(118, 0, 0);
background-color: rgb(156, 138, 138);
font: 24pt &quot;MS UI Gothic&quot;;
  
</string>
   </property>
   <property name="text">
    <string>Выбор уровня</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class Menu(QWidget):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template_menu)
        uic.loadUi(f, self)  # Загружаем дизайн

    def level_button(self):
        return self.lvl

    def setting_button(self):
        return self.setting


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Menu()
    ex.show()
    sys.exit(app.exec())

