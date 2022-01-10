import threading
from gui import Ui_MainWindow
from registrykeys import Optimizations, Debloat
import threading
import subprocess
import ctypes
import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        def moveWindow(e):
            if e.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + e.globalPos() - self.clickPosition)
                self.clickPosition = e.globalPos()
                e.accept()

        self.ui.run_button.clicked.connect(self.call_threads)
        self.ui.select_all_button.clicked.connect(self.select_all)

        self.ui.header_frame.mouseMoveEvent = moveWindow
        self.ui.close_button.clicked.connect(lambda: self.close())
        self.show()

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
    
    def call_threads(self):
        debloat_thread = threading.Thread(target=self.debloat)
        optimizations_thread = threading.Thread(target=self.optimizations)
        debloat_thread.start()
        optimizations_thread.start()
        debloat_thread.join()
        optimizations_thread.join()
        print("\n\n[Debug Console] All tasks finished.")
        self.ui.run_button.setEnabled(True)  # Re-enable the debloat button.

    def optimizations(self):
        self.ui.run_button.setEnabled(False)  # Disable the debloat button.

        if self.ui.dotnet_framework_checkbox.isChecked():  # Install .NET framework 3.5
            Optimizations.dotnet_framework(self)

        if self.ui.disable_mouse_acceleration_checkbox.isChecked():  # Disable mouse acceleration
            Optimizations.disable_mouse_acceleration(self)

        if self.ui.fix_keyboard_input_delay_checkbox.isChecked():  # Fix keyboard delay
            Optimizations.fix_keyboard_input_delay(self)

        if self.ui.disable_hibernation_checkbox.isChecked():  # Disable hibernation
            Optimizations.disable_hibernation(self)

        if self.ui.ultimate_power_plan_checkbox.isChecked():  # Enable ultimate power plan
            Optimizations.ultimate_power_plan(self)

        if self.ui.performance_tweaks_checkbox.isChecked():  # Performance Tweaks
            Optimizations.performance_tweaks(self)

        if self.ui.visual_tweaks_checkbox.isChecked():  # Visual Tweaks 
            Optimizations.visual_tweaks(self)


    def debloat(self):
        if self.ui.disable_bloat_services_checkbox.isChecked():  # Disable bloat services
            Debloat.disable_bloat_services(self)

        if self.ui.disable_gamedvr_checkbox.isChecked():  # Disable GameDVR
            Debloat.disable_gamedvr(self)

        if self.ui.remove_telemetry_keys_checkbox.isChecked():  # Remove telemetry keys
            Debloat.remove_telemetry_keys(self)

        if self.ui.uninstall_ms_apps_checkbox.isChecked():  # Uninstall Microsoft apps
            Debloat.uninstall_ms_apps(self)

        if self.ui.uninstall_ms_onedrive.isChecked():  # Uninstall Microsoft onedrive
            Debloat.uninstall_ms_onedrive(self)

    def select_all(self):  # Toggle the state of all checkboxes.
        self.ui.dotnet_framework_checkbox.nextCheckState()
        self.ui.disable_hibernation_checkbox.nextCheckState()
        self.ui.disable_bloat_services_checkbox.nextCheckState()
        self.ui.disable_gamedvr_checkbox.nextCheckState()
        self.ui.remove_telemetry_keys_checkbox.nextCheckState()
        self.ui.uninstall_ms_apps_checkbox.nextCheckState()
        self.ui.uninstall_ms_onedrive.nextCheckState()
        self.ui.disable_mouse_acceleration_checkbox.nextCheckState()
        self.ui.fix_keyboard_input_delay_checkbox.nextCheckState()
        self.ui.ultimate_power_plan_checkbox.nextCheckState()
        self.ui.performance_tweaks_checkbox.nextCheckState()
        self.ui.visual_tweaks_checkbox.nextCheckState()


if __name__ == "__main__":
    print("=== Debug Console ===\n\n[+] Loading GUI..")
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec()) 
