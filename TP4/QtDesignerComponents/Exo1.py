<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>753</width>
    <height>604</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <widget class="QLabel" name="mLabel">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>30</y>
     <width>640</width>
     <height>480</height>
    </rect>
   </property>
   <property name="minimumSize">
    <size>
     <width>640</width>
     <height>480</height>
    </size>
   </property>
   <property name="styleSheet">
    <string notr="true">
background-color: rgb(0, 255, 0);</string>
   </property>
   <property name="text">
    <string/>
   </property>
  </widget>
  <widget class="QWidget" name="">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>560</y>
     <width>641</width>
     <height>25</height>
    </rect>
   </property>
   <layout class="QHBoxLayout" name="horizontalLayout">
    <item>
     <widget class="QLineEdit" name="mLineEdit">
      <property name="readOnly">
       <bool>true</bool>
      </property>
     </widget>
    </item>
    <item>
     <spacer name="spacer">
      <property name="orientation">
       <enum>Qt::Horizontal</enum>
      </property>
      <property name="sizeHint" stdset="0">
       <size>
        <width>288</width>
        <height>20</height>
       </size>
      </property>
     </spacer>
    </item>
    <item>
     <widget class="QPushButton" name="mButtonBrowse">
      <property name="text">
       <string>...</string>
      </property>
     </widget>
    </item>
   </layout>
  </widget>
  <widget class="QWidget" name="">
   <property name="geometry">
    <rect>
     <x>660</x>
     <y>200</y>
     <width>82</width>
     <height>81</height>
    </rect>
   </property>
   <layout class="QVBoxLayout" name="verticalLayout">
    <item>
     <widget class="QPushButton" name="mButtonN">
      <property name="text">
       <string>Next</string>
      </property>
     </widget>
    </item>
    <item>
     <widget class="QPushButton" name="mButtonP">
      <property name="text">
       <string>Previous</string>
      </property>
     </widget>
    </item>
   </layout>
  </widget>
 </widget>
 <resources/>
 <connections>
  <connection>
   <sender>mButtonN</sender>
   <signal>clicked()</signal>
   <receiver>Form</receiver>
   <slot>Next()</slot>
   <hints>
    <hint type="sourcelabel">
     <x>700</x>
     <y>221</y>
    </hint>
    <hint type="destinationlabel">
     <x>376</x>
     <y>301</y>
    </hint>
   </hints>
  </connection>
  <connection>
   <sender>mButtonP</sender>
   <signal>clicked()</signal>
   <receiver>Form</receiver>
   <slot>Previous()</slot>
   <hints>
    <hint type="sourcelabel">
     <x>700</x>
     <y>259</y>
    </hint>
    <hint type="destinationlabel">
     <x>376</x>
     <y>301</y>
    </hint>
   </hints>
  </connection>
  <connection>
   <sender>mButtonBrowse</sender>
   <signal>clicked()</signal>
   <receiver>Form</receiver>
   <slot>LoadFiles()</slot>
   <hints>
    <hint type="sourcelabel">
     <x>609</x>
     <y>572</y>
    </hint>
    <hint type="destinationlabel">
     <x>376</x>
     <y>301</y>
    </hint>
   </hints>
  </connection>
 </connections>
 <slots>
  <slot>LoadFiles()</slot>
  <slot>Next()</slot>
  <slot>Previous()</slot>
 </slots>
</ui>
