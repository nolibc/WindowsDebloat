from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(332, 197)
        MainWindow.setMinimumSize(QtCore.QSize(332, 197))
        MainWindow.setMaximumSize(QtCore.QSize(332, 197))
        font = QtGui.QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: #272727;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 27, 341, 251))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.frame.setFont(font)
        self.frame.setStyleSheet("* {\n"
"    color: white;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    border-radius: 2px;\n"
"    width: 16px;\n"
"    height: 16px;\n"
"}\n"
"\n"
"QCheckBox::indicator::unchecked {\n"
"    border: 1px solid #5A5A5A;\n"
"}\n"
"\n"
"QCheckBox::indicator::checked {\n"
"    border: 1px solid #c49df5;\n"
"    background: #c49df5;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.run_button = QtWidgets.QPushButton(self.frame)
        self.run_button.setGeometry(QtCore.QRect(230, 140, 91, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.run_button.setFont(font)
        self.run_button.setStyleSheet("QPushButton {\n"
"  background-color: #BB86FC;\n"
"  border-radius: 3px;\n"
"  color: #FFFFFF;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover:!pressed {\n"
"  background-color: #c49df5;\n"
"}")
        self.run_button.setObjectName("run_button")
        self.dotnet_framework_checkbox = QtWidgets.QCheckBox(self.frame)
        self.dotnet_framework_checkbox.setGeometry(QtCore.QRect(6, 18, 131, 21))
        self.dotnet_framework_checkbox.setStyleSheet("")
        self.dotnet_framework_checkbox.setObjectName("dotnet_framework_checkbox")
        self.disable_hibernation_checkbox = QtWidgets.QCheckBox(self.frame)
        self.disable_hibernation_checkbox.setGeometry(QtCore.QRect(6, 39, 151, 21))
        self.disable_hibernation_checkbox.setStyleSheet("")
        self.disable_hibernation_checkbox.setObjectName("disable_hibernation_checkbox")
        self.disable_bloat_services_checkbox = QtWidgets.QCheckBox(self.frame)
        self.disable_bloat_services_checkbox.setGeometry(QtCore.QRect(168, 18, 131, 21))
        self.disable_bloat_services_checkbox.setStyleSheet("")
        self.disable_bloat_services_checkbox.setObjectName("disable_bloat_services_checkbox")
        self.disable_gamedvr_checkbox = QtWidgets.QCheckBox(self.frame)
        self.disable_gamedvr_checkbox.setGeometry(QtCore.QRect(168, 39, 131, 21))
        self.disable_gamedvr_checkbox.setStyleSheet("")
        self.disable_gamedvr_checkbox.setObjectName("disable_gamedvr_checkbox")
        self.remove_telemetry_keys_checkbox = QtWidgets.QCheckBox(self.frame)
        self.remove_telemetry_keys_checkbox.setGeometry(QtCore.QRect(168, 60, 151, 21))
        self.remove_telemetry_keys_checkbox.setStyleSheet("")
        self.remove_telemetry_keys_checkbox.setObjectName("remove_telemetry_keys_checkbox")
        self.uninstall_ms_onedrive = QtWidgets.QCheckBox(self.frame)
        self.uninstall_ms_onedrive.setGeometry(QtCore.QRect(168, 102, 161, 21))
        self.uninstall_ms_onedrive.setStyleSheet("")
        self.uninstall_ms_onedrive.setObjectName("uninstall_ms_onedrive")
        self.disable_mouse_acceleration_checkbox = QtWidgets.QCheckBox(self.frame)
        self.disable_mouse_acceleration_checkbox.setGeometry(QtCore.QRect(6, 60, 161, 21))
        self.disable_mouse_acceleration_checkbox.setStyleSheet("")
        self.disable_mouse_acceleration_checkbox.setObjectName("disable_mouse_acceleration_checkbox")
        self.fix_keyboard_input_delay_checkbox = QtWidgets.QCheckBox(self.frame)
        self.fix_keyboard_input_delay_checkbox.setGeometry(QtCore.QRect(6, 81, 151, 21))
        self.fix_keyboard_input_delay_checkbox.setStyleSheet("")
        self.fix_keyboard_input_delay_checkbox.setObjectName("fix_keyboard_input_delay_checkbox")
        self.ultimate_power_plan_checkbox = QtWidgets.QCheckBox(self.frame)
        self.ultimate_power_plan_checkbox.setGeometry(QtCore.QRect(6, 102, 121, 21))
        self.ultimate_power_plan_checkbox.setStyleSheet("")
        self.ultimate_power_plan_checkbox.setObjectName("ultimate_power_plan_checkbox")
        self.visual_tweaks_checkbox = QtWidgets.QCheckBox(self.frame)
        self.visual_tweaks_checkbox.setGeometry(QtCore.QRect(6, 144, 101, 21))
        self.visual_tweaks_checkbox.setStyleSheet("")
        self.visual_tweaks_checkbox.setObjectName("visual_tweaks_checkbox")
        self.select_all_button = QtWidgets.QPushButton(self.frame)
        self.select_all_button.setGeometry(QtCore.QRect(166, 142, 60, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.select_all_button.setFont(font)
        self.select_all_button.setStyleSheet("QPushButton {\n"
"  background-color: #272727;\n"
"  border-radius: 8px;\n"
"  color: #FFFFFF;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover:!pressed {\n"
"  color: #BB86FC;\n"
"}")
        self.select_all_button.setObjectName("select_all_button")
        self.uninstall_ms_apps_checkbox = QtWidgets.QCheckBox(self.frame)
        self.uninstall_ms_apps_checkbox.setGeometry(QtCore.QRect(168, 81, 141, 21))
        self.uninstall_ms_apps_checkbox.setStyleSheet("")
        self.uninstall_ms_apps_checkbox.setObjectName("uninstall_ms_apps_checkbox")
        self.performance_tweaks_checkbox = QtWidgets.QCheckBox(self.frame)
        self.performance_tweaks_checkbox.setGeometry(QtCore.QRect(6, 123, 131, 21))
        self.performance_tweaks_checkbox.setStyleSheet("")
        self.performance_tweaks_checkbox.setObjectName("performance_tweaks_checkbox")
        self.debloat_label = QtWidgets.QLabel(self.frame)
        self.debloat_label.setGeometry(QtCore.QRect(170, 0, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.debloat_label.setFont(font)
        self.debloat_label.setStyleSheet("color: #BB86FC;")
        self.debloat_label.setObjectName("debloat_label")
        self.optimizations_label = QtWidgets.QLabel(self.frame)
        self.optimizations_label.setGeometry(QtCore.QRect(8, -1, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.optimizations_label.setFont(font)
        self.optimizations_label.setStyleSheet("color: #BB86FC;")
        self.optimizations_label.setObjectName("optimizations_label")
        self.header_frame = QtWidgets.QFrame(self.centralwidget)
        self.header_frame.setGeometry(QtCore.QRect(0, 0, 331, 21))
        self.header_frame.setStyleSheet("background-color: #1D1D1D;")
        self.header_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_frame.setObjectName("header_frame")
        self.windows_debloat_label = QtWidgets.QLabel(self.header_frame)
        self.windows_debloat_label.setGeometry(QtCore.QRect(7, 0, 118, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.windows_debloat_label.setFont(font)
        self.windows_debloat_label.setStyleSheet("color: #FFFFFF;")
        self.windows_debloat_label.setObjectName("windows_debloat_label")
        self.close_button = QtWidgets.QPushButton(self.header_frame)
        self.close_button.setGeometry(QtCore.QRect(311, -2, 21, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.close_button.setFont(font)
        self.close_button.setStyleSheet("QPushButton {\n"
"  background-color: #1D1D1D;\n"
"  border-radius: 3px;\n"
"  color: #FFFFFF;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover:!pressed {\n"
"  color: #BB86FC;\n"
"}")
        self.close_button.setObjectName("close_button")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Windows Debloat"))
        self.run_button.setText(_translate("MainWindow", "Run"))
        self.dotnet_framework_checkbox.setText(_translate("MainWindow", ".NET Framework 3.5"))
        self.disable_hibernation_checkbox.setText(_translate("MainWindow", "Disable Hibernation"))
        self.disable_bloat_services_checkbox.setText(_translate("MainWindow", "Disable Bloat Services"))
        self.disable_gamedvr_checkbox.setText(_translate("MainWindow", "Disable GameDVR"))
        self.remove_telemetry_keys_checkbox.setText(_translate("MainWindow", "Remove Telemetry Keys"))
        self.uninstall_ms_onedrive.setText(_translate("MainWindow", "Uninstall Microsoft OneDrive"))
        self.disable_mouse_acceleration_checkbox.setText(_translate("MainWindow", "Disable Mouse Acceleration"))
        self.fix_keyboard_input_delay_checkbox.setText(_translate("MainWindow", "Fix Keyboard Input Delay"))
        self.ultimate_power_plan_checkbox.setText(_translate("MainWindow", "Ultimate Power Plan"))
        self.visual_tweaks_checkbox.setText(_translate("MainWindow", "Visual Tweaks"))
        self.select_all_button.setText(_translate("MainWindow", "Select All"))
        self.uninstall_ms_apps_checkbox.setText(_translate("MainWindow", "Uninstall Microsoft Apps"))
        self.performance_tweaks_checkbox.setText(_translate("MainWindow", "Performance Tweaks"))
        self.debloat_label.setText(_translate("MainWindow", "Debloat"))
        self.optimizations_label.setText(_translate("MainWindow", "Optimizations"))
        self.windows_debloat_label.setText(_translate("MainWindow", "Windows Debloat"))
        self.close_button.setText(_translate("MainWindow", "X"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
