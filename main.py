"""
Windows Debloater: 0.1.0 dev
Windows Debloater aims to allow users to quickly and easily debloat Windows.

Created by LinJuz
"""

from gui import Ui_MainWindow
from registrykeys import Optimizations, Debloat
import sys
import os
import ctypes
import subprocess

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        try:
            super(MyWindow, self).__init__(parent)
            self.setupUi(self)
            self.button_listener()
            print("[+] GUI loaded")
        except Exception:
            print("\n[-] Error: Unable to load GUI.")

    def button_listener(self):
        self.run_button.clicked.connect(self.optimizations)
        self.select_all_button.clicked.connect(self.select_all)

    def optimizations(self):
        self.run_button.setEnabled(False)  # Disable the debloat button.

        if self.dotnet_framework_checkbox.isChecked():  # Install .NET framework 3.5
            Optimizations.dotnet_framework(self)

        if self.disable_mouse_acceleration_checkbox.isChecked():
            Optimizations.disable_mouse_acceleration(self)

        if self.fix_keyboard_input_delay_checkbox.isChecked():  # Fix keyboard delay
            Optimizations.fix_keyboard_input_delay(self)

        if self.restore_ms_photo_viewer_checkbox.isChecked():
            Optimizations.restore_ms_photo_viewer(self)

        if self.ultimate_power_plan_checkbox.isChecked():  # Enable ultimate power plan
            Optimizations.ultimate_power_plan(self)

        if self.performance_tweaks_checkbox.isChecked():
            Optimizations.performance_tweaks(self)

        if self.visual_tweaks_checkbox.isChecked():
            Optimizations.visual_tweaks(self)

        self.debloat()

    def debloat(self):
        if self.disable_bloat_services_checkbox.isChecked():
            Debloat.disable_bloat_services(self)

        if self.disable_gamedvr_checkbox.isChecked():  # Disable GameDVR
            Debloat.disable_gamedvr(self)

        if self.remove_telemetry_keys_checkbox.isChecked():  # Remove telemetry keys
            Debloat.remove_telemetry_keys(self)

        if self.uninstall_ms_apps_checkbox.isChecked():  # Uninstall Microsoft apps
            Debloat.uninstall_ms_apps(self)

        if self.uninstall_ms_onedrive.isChecked():  # Uninstall Microsoft onedrive
            Debloat.uninstall_ms_onedrive(self)

        self.run_button.setEnabled(True)  # Re-enable the debloat button.

    def select_all(self):  # Toggle the state of all checkboxes.
        self.dotnet_framework_checkbox.nextCheckState()
        self.restore_ms_photo_viewer_checkbox.nextCheckState()
        self.disable_bloat_services_checkbox.nextCheckState()
        self.disable_gamedvr_checkbox.nextCheckState()
        self.remove_telemetry_keys_checkbox.nextCheckState()
        self.uninstall_ms_apps_checkbox.nextCheckState()
        self.uninstall_ms_onedrive.nextCheckState()
        self.disable_mouse_acceleration_checkbox.nextCheckState()
        self.fix_keyboard_input_delay_checkbox.nextCheckState()
        self.ultimate_power_plan_checkbox.nextCheckState()
        self.performance_tweaks_checkbox.nextCheckState()
        self.visual_tweaks_checkbox.nextCheckState()


if __name__ == "__main__":

    print("=== Debug Console ===\n\n[+] Loading GUI..")
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    sys.exit(app.exec_())
