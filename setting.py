import io
import sys

from PyQt6 import uic  # Импортируем uic
from PyQt6.QtWidgets import QApplication, QWidget

template_setting = """<?xml version="1.0" encoding="UTF-8"?>
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
     <x>220</x>
     <y>50</y>
     <width>651</width>
     <height>111</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font: 36pt &quot;Ebrima&quot;;
color: rgb(170, 0, 0)</string>
   </property>
   <property name="text">
    <string>Настройки</string>
   </property>
   <property name="alignment">
    <set>Qt::AlignCenter</set>
   </property>
  </widget>
  <widget class="QPushButton" name="dus">
   <property name="geometry">
    <rect>
     <x>110</x>
     <y>430</y>
     <width>201</width>
     <height>41</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font: 24pt &quot;MS UI Gothic&quot;;
color: rgb(170, 0, 0);
background-color: rgb(157, 125, 125);</string>
   </property>
   <property name="text">
    <string>Лес</string>
   </property>
  </widget>
  <widget class="QPushButton" name="mountains">
   <property name="geometry">
    <rect>
     <x>430</x>
     <y>430</y>
     <width>201</width>
     <height>41</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font: 24pt &quot;MS UI Gothic&quot;;
color: rgb(170, 0, 0);
background-color: rgb(157, 125, 125);</string>
   </property>
   <property name="text">
    <string>Горы</string>
   </property>
  </widget>
  <widget class="QPushButton" name="space">
   <property name="geometry">
    <rect>
     <x>770</x>
     <y>430</y>
     <width>201</width>
     <height>41</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font: 24pt &quot;MS UI Gothic&quot;;
color: rgb(170, 0, 0);
background-color: rgb(157, 125, 125);
</string>
   </property>
   <property name="text">
    <string>Космос</string>
   </property>
  </widget>
  <widget class="QPushButton" name="exit">
   <property name="geometry">
    <rect>
     <x>900</x>
     <y>20</y>
     <width>161</width>
     <height>51</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">font: 20pt &quot;MS Shell Dlg 2&quot;;
color: rgb(170, 0, 0);
background-color: rgb(157, 125, 125);</string>
   </property>
   <property name="text">
    <string>Назад</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class Setting(QWidget):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template_setting)
        uic.loadUi(f, self)  # Загружаем дизайн

    def exit_button(self):
        return self.exit

    def login_button(self):
        return self.setting


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Setting()
    ex.show()
    sys.exit(app.exec())

